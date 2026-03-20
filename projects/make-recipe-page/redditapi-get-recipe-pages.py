# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

import html
import os
from pathlib import Path

import praw


OUTPUT_FILE = Path(__file__).with_name("recipes_from_reddit.html")


def get_reddit_client():
		"""Create a Reddit client using environment variables."""
		client_id = os.getenv("REDDIT_CLIENT_ID")
		client_secret = os.getenv("REDDIT_CLIENT_SECRET")
		user_agent = os.getenv("REDDIT_USER_AGENT", "codingnomads-recipe-scraper/1.0")

		if not client_id or not client_secret:
				raise RuntimeError(
						"Missing credentials. Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET."
				)

		return praw.Reddit(
				client_id=client_id,
				client_secret=client_secret,
				user_agent=user_agent,
		)


def fetch_recipe_posts(reddit, subreddit_name="recipes", limit=25):
		"""Fetch top recipe posts from a subreddit."""
		posts = []
		subreddit = reddit.subreddit(subreddit_name)

		for post in subreddit.hot(limit=limit):
				# Skip NSFW and non-link/self posts with empty text.
				if post.over_18:
						continue

				post_data = {
						"title": post.title,
						"author": str(post.author) if post.author else "unknown",
						"score": post.score,
						"url": post.url,
						"permalink": f"https://www.reddit.com{post.permalink}",
						"preview": (post.selftext or "").strip()[:250],
				}
				posts.append(post_data)

		return posts


def build_html(posts, heading="Reddit Recipes"):
		"""Build a simple recipes page from post data."""
		cards = []
		for post in posts:
				title = html.escape(post["title"])
				author = html.escape(post["author"])
				url = html.escape(post["url"])
				permalink = html.escape(post["permalink"])
				preview = html.escape(post["preview"])

				cards.append(
						f"""
						<article class=\"recipe-card\">
							<h2>{title}</h2>
							<p><strong>Author:</strong> {author}</p>
							<p><strong>Score:</strong> {post['score']}</p>
							<p><a href=\"{url}\" target=\"_blank\">Open linked recipe</a></p>
							<p><a href=\"{permalink}\" target=\"_blank\">Open Reddit discussion</a></p>
							<p>{preview}</p>
						</article>
						"""
				)

		return f"""<!doctype html>
<html lang=\"en\">
	<head>
		<meta charset=\"utf-8\" />
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
		<title>{html.escape(heading)}</title>
		<style>
			body {{
				font-family: Georgia, serif;
				margin: 0;
				padding: 2rem;
				background: #f8f6f0;
				color: #2c2a28;
			}}
			h1 {{ margin-top: 0; }}
			.grid {{
				display: grid;
				grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
				gap: 1rem;
			}}
			.recipe-card {{
				background: #fff;
				border: 1px solid #ddd7c8;
				border-radius: 12px;
				padding: 1rem;
			}}
		</style>
	</head>
	<body>
		<h1>{html.escape(heading)}</h1>
		<p>Generated from Reddit API using praw.</p>
		<section class=\"grid\">
			{''.join(cards)}
		</section>
	</body>
</html>
"""


def main():
		reddit = get_reddit_client()
		posts = fetch_recipe_posts(reddit)
		page = build_html(posts)
		OUTPUT_FILE.write_text(page, encoding="utf-8")
		print(f"Saved {len(posts)} recipes to {OUTPUT_FILE}")


if __name__ == "__main__":
		main()
