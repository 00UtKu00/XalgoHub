1. What is the Core Purpose of the System?
XalgoHub is a deterministic simulation sandbox built directly upon X's (formerly Twitter) open-source recommendation algorithm (the-algorithm). The live system can be accessed at xalgohub.vercel.app.

Its primary purpose is to allow users to test a tweet before publishing it. By using mathematical models, the system predicts how a post will interact with algorithm filters, estimates its potential reach (impressions), and identifies critical errors that could cause it to be shadowbanned or suppressed. It operates entirely client-side, requiring no user logins or paid API keys.

2. How the Input Panel Works (Left Side)
When a user enters the site, they define the raw inputs that the algorithm processes:

Account Profile Blueprint: The algorithm treats different accounts differently. A brand-new account has a different "trust score" compared to a verified account with 100k followers. The system applies a Base Trust Multiplier based on the selected tier. If a "bot-suspicious" account is selected, the multiplier drops near zero, crippling the tweet's reach regardless of its quality.

Tweet Editor & Character Check: The system monitors character limits in real-time (280 for standard, 4000 for Premium). Exceeding the limit appropriate for the account tier results in algorithmic cropping or penalty margins in X's actual system.

Media Attachment Simulator: A text-only tweet carries a different algorithmic weight than one with a video. Selecting "Video" activates the Dwell-Time Multiplier. Since videos force users to stay on the screen longer, the algorithm rewards this behavior with higher visibility.

Target Engagement Sliders: The user selects their expected number of likes, retweets, replies, and bookmarks. This acts as the mathematical brain of the simulation.

3. The Scoring Engine Logic (Algorithm Mathematics)
When the user hits "Simulate," the backend engine calculates the output using the official, leaked weights of X's open-source algorithm. Every interaction has a specific point value:

Like: The baseline metric (1 point).

Retweet: Highly valuable because it broadcasts content to secondary networks (20 points).

Bookmark: A strong signal of long-term value and user retention (30 points).

Reply: The most valuable interaction, as X prioritizes deep conversational threads (54 points).

The system multiplies the user's targeted sliders by these weights to generate a Raw Score. It then multiplies this raw score by the Account Multiplier and Media Multiplier to calculate the Estimated Impression Range.

System Penalties & Heuristic Rules
The engine also scans the text line-by-line to apply hardcoded platform rules:

Outbound Link Penalty: If the tweet contains an external link (e.g., YouTube, a personal blog), the system slashes the predicted reach by 50%. X penalizes content that drives traffic away from its platform.

Hashtag Filter: If the text contains more than 3 hashtags, the system flags it as "tag spam" and applies a numerical penalty. It gives a green light for the optimal 1-3 hashtag range.

4. Dynamic Algorithm File Uploader
Since X can update its algorithm weights at any time (e.g., reducing retweet value and increasing likes), this module future-proofs the system.

Users can upload a raw configuration file (.json, .txt, .py) containing target variables. The system runs a Text Parser (Regex) that scans the uploaded code. The moment it detects new coefficients, it overrides the default baseline values (like the 54 points for a reply) and recalculates the entire mathematical matrix on the fly.

5. Advanced Analytics Modules (Right Side)
Beyond pure math, the system analyzes the semantic structure and psychological tone of the text:

AI A/B Testing (Hook Optimizer): Analyzes the first sentence (the hook). It suggests structural line breaks and punchier formatting to maximize scrolling friction (dwell time), generating alternative versions of the text.

With https://github.com/xai-org/x-algorithm.git

Echo Chamber (Topic Clustering): Scans for specific keywords. If it detects "BTC, ETH," it flags the Crypto cluster; if it sees "AI, code," it flags Tech. It then calculates a localized visibility boost based on current platform macro-trends.

Troll & Outrage Risk Meter: Analyzes the emotional polarization of the text. Highly controversial or aggressive text drastically increases the likelihood of getting "Replies," which skyrockets algorithmic reach. However, the system visually warns the user that this simultaneously spikes the risk of mass reporting and potential shadowbanning.
