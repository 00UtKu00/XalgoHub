import json, urllib.request, urllib.parse, re
from http.server import BaseHTTPRequestHandler


def scrape_profile(username):
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

    follower_matches = re.findall(r'followers_count["\s:]+(\d+)', html)
    if follower_matches:
        followers = max(int(v) for v in follower_matches)

    following_matches = re.findall(r'friends_count["\s:]+(\d+)', html)
    if following_matches:
        following = max(int(v) for v in following_matches)

    m = re.search(r'"name"\s*:\s*"([^"]+)"', html)
    if m:
        name = m.group(1).encode().decode("unicode_escape")

    m = re.search(r'created_at["\s:]+"([^"]+)"', html)
    if m:
        created_at = m.group(1)

    m = re.search(r'"is_blue_verified"\s*:\s*(true|false)', html)
    if m:
        verified = m.group(1) == "true"
    if not verified:
        m = re.search(r'"verified_type"\s*:\s*"([^"]+)"', html)
        if m and m.group(1) != "none":
            verified = True

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


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
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
