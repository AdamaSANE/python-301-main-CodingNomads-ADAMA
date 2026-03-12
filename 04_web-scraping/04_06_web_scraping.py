# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

from pathlib import Path

import requests
from bs4 import BeautifulSoup


# Ce site est volontairement simple et concu pour pratiquer le scraping.
URL = "https://quotes.toscrape.com/"
# On stocke une copie locale du HTML pour eviter des requetes repetees.
HTML_FILE = Path(__file__).with_name("quotes_to_scrape.html")


def download_page(url: str, destination: Path) -> None:
	"""Download the page once and save its HTML locally."""
	response = requests.get(url, timeout=15)
	response.raise_for_status()
	destination.write_text(response.text, encoding="utf-8")


def load_local_html(source: Path) -> str:
	"""Read the saved HTML file and return its content."""
	return source.read_text(encoding="utf-8")


def get_soup_from_file(source: Path) -> BeautifulSoup:
	"""Parse the local HTML file with BeautifulSoup."""
	html = load_local_html(source)
	return BeautifulSoup(html, "html.parser")


def extract_quotes(soup: BeautifulSoup) -> list[dict]:
	"""Extract quote text, author, and tags from the page."""
	quotes = []

	for quote_block in soup.select("div.quote"):
		text_tag = quote_block.select_one("span.text")
		author_tag = quote_block.select_one("small.author")
		tag_elements = quote_block.select("div.tags a.tag")

		if text_tag is None or author_tag is None:
			continue

		quotes.append(
			{
				"text": text_tag.get_text(strip=True),
				"author": author_tag.get_text(strip=True),
				"tags": [tag.get_text(strip=True) for tag in tag_elements],
			}
		)

	return quotes


def print_quotes(quotes: list[dict]) -> None:
	"""Display the scraped information in a readable format."""
	print("Quotes To Scrape")
	print("=" * 60)

	for index, quote in enumerate(quotes, start=1):
		print(f"Quote {index}")
		print(f"Text: {quote['text']}")
		print(f"Author: {quote['author']}")
		print(f"Tags: {', '.join(quote['tags']) if quote['tags'] else 'No tags'}")
		print("-" * 60)


def main() -> None:
	# On telecharge la page seulement si aucune copie locale n'existe encore.
	if not HTML_FILE.exists():
		download_page(URL, HTML_FILE)

	# Ensuite, tout le parsing se fait depuis le fichier local.
	soup = get_soup_from_file(HTML_FILE)
	quotes = extract_quotes(soup)
	print_quotes(quotes)


if __name__ == "__main__":
	main()
