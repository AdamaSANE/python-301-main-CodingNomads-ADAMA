# Demonstrate how you can log in to the Reddit API to receive content that
# requires authentication, using only `requests` and your credentials.

import os

import requests
from requests.auth import HTTPBasicAuth


TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
ME_URL = "https://oauth.reddit.com/api/v1/me"


def get_access_token():
	"""Request an OAuth token using Reddit script-app credentials."""
	client_id = os.getenv("REDDIT_CLIENT_ID")
	client_secret = os.getenv("REDDIT_CLIENT_SECRET")
	username = os.getenv("REDDIT_USERNAME")
	password = os.getenv("REDDIT_PASSWORD")
	user_agent = os.getenv("REDDIT_USER_AGENT", "codingnomads-token-demo/1.0")

	if not all([client_id, client_secret, username, password]):
		raise RuntimeError(
			"Missing environment variables. Set REDDIT_CLIENT_ID, "
			"REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD."
		)

	# Password grant is suitable for script apps in local/learning scenarios.
	response = requests.post(
		TOKEN_URL,
		auth=HTTPBasicAuth(client_id, client_secret),
		data={
			"grant_type": "password",
			"username": username,
			"password": password,
		},
		headers={"User-Agent": user_agent},
		timeout=30,
	)
	response.raise_for_status()

	payload = response.json()
	token = payload.get("access_token")
	token_type = payload.get("token_type", "bearer")

	if not token:
		raise RuntimeError(f"Token not found in response: {payload}")

	return token_type, token, user_agent


def fetch_authenticated_profile(token_type, token, user_agent):
	"""Call an endpoint that requires authentication to verify login."""
	headers = {
		"Authorization": f"{token_type.capitalize()} {token}",
		"User-Agent": user_agent,
	}
	response = requests.get(ME_URL, headers=headers, timeout=30)
	response.raise_for_status()
	return response.json()


def main():
	token_type, token, user_agent = get_access_token()

	# Affiche seulement un extrait pour eviter de divulguer le token complet.
	print(f"Token acquired: {token[:10]}... ({token_type})")

	me = fetch_authenticated_profile(token_type, token, user_agent)
	print(f"Authenticated as: {me.get('name', 'unknown')}")


if __name__ == "__main__":
	main()
