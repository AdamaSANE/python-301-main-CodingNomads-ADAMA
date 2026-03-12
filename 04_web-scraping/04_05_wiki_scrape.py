# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

import re
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/Web_scraping"
OUTPUT_FILE = Path(__file__).with_name("wiki_article.txt")


def get_soup(url: str) -> BeautifulSoup:
	"""Download a page and return a BeautifulSoup parser for its HTML."""
	response = requests.get(url, timeout=15)
	response.raise_for_status()
	return BeautifulSoup(response.text, "html.parser")


def extract_article_links(soup: BeautifulSoup) -> list[str]:
	"""Return article links from the main content area, excluding navigation links."""
	content = soup.find("div", class_="mw-parser-output")
	if content is None:
		return []

	article_links = []
	seen = set()

	for link in content.find_all("a", href=True):
		href = link["href"]

		# We only keep internal Wikipedia article links.
		if not href.startswith("/wiki/"):
			continue

		# Links with ':' usually point to files, help pages, categories, etc.
		if ":" in href or "#" in href:
			continue

		full_url = urljoin("https://en.wikipedia.org", href)
		if full_url not in seen and full_url != URL:
			seen.add(full_url)
			article_links.append(full_url)

	return article_links


def extract_article_text(soup: BeautifulSoup) -> str:
	"""Extract readable paragraph text from a Wikipedia article."""
	content = soup.find("div", class_="mw-parser-output")
	if content is None:
		return ""

	paragraphs = []
	for paragraph in content.find_all("p", recursive=False):
		text = paragraph.get_text(" ", strip=True)
		if text:
			paragraphs.append(text)

	return "\n\n".join(paragraphs)


def save_text_to_file(text: str, output_file: Path) -> None:
	"""Save the extracted article text locally."""
	output_file.write_text(text, encoding="utf-8")


def find_numbers(text: str) -> list[str]:
	"""Find all integer or decimal numbers present in the article text."""
	return re.findall(r"\b\d+(?:\.\d+)?\b", text)


def main() -> None:
	# Fetch the Wikipedia page about web scraping.
	main_soup = get_soup(URL)

	# Extract only article links from the page content.
	article_links = extract_article_links(main_soup)

	if not article_links:
		print("No article links were found.")
		return

	# Follow the first valid Wikipedia article link we found.
	chosen_article_url = article_links[0]
	article_soup = get_soup(chosen_article_url)
	article_text = extract_article_text(article_soup)

	# Save the article text to a local file.
	save_text_to_file(article_text, OUTPUT_FILE)

	# Bonus task: find all numbers in the extracted text.
	numbers = find_numbers(article_text)

	print("Wikipedia web scraping report")
	print("=" * 50)
	print(f"Source page: {URL}")
	print(f"Filtered article links found: {len(article_links)}")
	print(f"Chosen article: {chosen_article_url}")
	print(f"Saved text file: {OUTPUT_FILE.name}")
	print(f"Characters saved: {len(article_text)}")
	print(f"Numbers found: {len(numbers)}")
	if numbers:
		print(f"First numbers found: {numbers[:10]}")


if __name__ == "__main__":
	main()
