import http.server
import json
import os
import re
import urllib.request
import urllib.parse

PORT = int(os.environ.get("PORT", 8888))
DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root (parent of app/)


def scrape_profile(username):
    """Scrape public X/Twitter profile page for account data. No auth needed."""
    url = f"https://twitter.com/{urllib.parse.quote(username)}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    try:
        resp = urllib.request.urlopen(req, timeout=15)
    except Exception:
        return None

    html = resp.read().decode(errors="replace")

    followers = 0
    following = 0
    name = username
    created_at = None
    verified = False
    description = ""

    # Followers count — take the largest match (HTML has multiple values)
    follower_matches = re.findall(r'followers_count["\s:]+(\d+)', html)
    if follower_matches:
        followers = max(int(v) for v in follower_matches)

    # Following count (friends_count in X API)
    following_matches = re.findall(r'friends_count["\s:]+(\d+)', html)
    if following_matches:
        following = max(int(v) for v in following_matches)

    # Display name
    m = re.search(r'"name"\s*:\s*"([^"]+)"', html)
    if m:
        name = m.group(1).encode().decode("unicode_escape")

    # Account creation date
    m = re.search(r'created_at["\s:]+"([^"]+)"', html)
    if m:
        created_at = m.group(1)

    # Verified / blue check
    # Look for verified:true preceded by is_blue_verified or verified_type
    m = re.search(r'"is_blue_verified"\s*:\s*(true|false)', html)
    if m:
        verified = m.group(1) == "true"
    if not verified:
        m = re.search(r'"verified_type"\s*:\s*"([^"]+)"', html)
        if m and m.group(1) != "none":
            verified = True

    # Description
    m = re.search(r'"description"\s*:\s*"((?:[^"\\]|\\.)*)"', html)
    if m:
        description = m.group(1).encode().decode("unicode_escape")

    if followers == 0 and following == 0:
        return None

    return {
        "data": {
            "followers": followers,
            "following": following,
            "created_at": created_at,
            "verified": verified,
            "is_identity_verified": verified,
            "name": name,
            "description": description,
        }
    }


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_GET(self):
        if self.path.startswith("/x-profile"):
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            username = (params.get("username", [""])[0]).strip().replace("@", "")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            if not username:
                self.wfile.write(json.dumps({"error": "username required"}).encode())
                return

            result = scrape_profile(username)
            if not result:
                result = {"error": f"Could not fetch data for @{username}"}

            self.wfile.write(json.dumps(result).encode())
            return
        super().do_GET()

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")


if __name__ == "__main__":
    print(f"XalgoHub server on http://localhost:{PORT}")
    httpd = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("\nServer stopped.")
