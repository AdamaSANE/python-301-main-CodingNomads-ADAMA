# In three lines of code, fetch the HTML text from CodingNomads'
# main page and print it to your console.
#
# If you run into encoding/decoding errors, you're experiencing something
# very common. head over to StackOverflow and find a solution!

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://codingnomads.github.io/recipes/"


def extract_recipe_text(soup: BeautifulSoup) -> str:
	"""Return the recipe body text using the first matching container."""
	selectors = [
		("div", {"class": "recipe-body"}),
		("article", {}),
		("main", {}),
	]
	for tag, attrs in selectors:
		container = soup.find(tag, attrs=attrs)
		if container:
			return container.get_text(" ", strip=True)
	return ""


index_page = requests.get(BASE_URL, timeout=15)
index_page.raise_for_status()
index_soup = BeautifulSoup(index_page.text, "html.parser")

links = index_soup.find_all("a", href=True)
urls = [link["href"] for link in links if link["href"].startswith("recipes/")]

for relative_url in urls:
	full_url = BASE_URL + relative_url
	recipe_page = requests.get(full_url, timeout=15)
	recipe_page.raise_for_status()
	recipe_soup = BeautifulSoup(recipe_page.text, "html.parser")

	h1 = recipe_soup.find("h1")
	title = h1.get_text(strip=True) if h1 else "Untitled"
	recipe = extract_recipe_text(recipe_soup)

	print(f"Title: {title}")
	print(f"Recipe: {recipe[:200]}...")
	print("-" * 60)
