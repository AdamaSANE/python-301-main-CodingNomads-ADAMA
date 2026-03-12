# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


# Page d'index qui liste les recettes du site CodingNomads.
BASE_URL = "https://codingnomads.github.io/recipes/"


def get_soup(url: str) -> BeautifulSoup:
	"""Download a page and return it as a BeautifulSoup object."""
	# Cette fonction centralise le telechargement et le parsing HTML.
	response = requests.get(url, timeout=15)
	response.raise_for_status()
	return BeautifulSoup(response.text, "html.parser")


def get_recipe_urls(index_soup: BeautifulSoup) -> list[str]:
	"""Extract recipe links from the index page and convert them to full URLs."""
	recipe_urls = []

	for link in index_soup.find_all("a", href=True):
		href = link["href"]
		# On garde uniquement les liens qui pointent vers des recettes du site.
		if href.startswith("recipes/"):
			recipe_urls.append(urljoin(BASE_URL, href))

	return recipe_urls


def extract_recipe_text(recipe_soup: BeautifulSoup) -> str:
	"""Return the main text content of a recipe page."""
	# On essaie plusieurs conteneurs possibles pour rester robuste.
	selectors = [
		("div", {"class": "recipe-body"}),
		("article", {}),
		("main", {}),
	]

	for tag_name, attrs in selectors:
		container = recipe_soup.find(tag_name, attrs=attrs)
		if container is not None:
			return container.get_text(" ", strip=True)

	return ""


def get_recipe_title(recipe_soup: BeautifulSoup) -> str:
	"""Extract the recipe title from the page."""
	# Le titre principal se trouve normalement dans la balise h1.
	heading = recipe_soup.find("h1")
	return heading.get_text(strip=True) if heading is not None else "Untitled"


def get_recipe_data(recipe_url: str) -> dict:
	"""Fetch one recipe page and return its title, URL, and text."""
	# Cette fonction regroupe toutes les informations utiles pour une recette.
	recipe_soup = get_soup(recipe_url)
	return {
		"title": get_recipe_title(recipe_soup),
		"url": recipe_url,
		"text": extract_recipe_text(recipe_soup),
	}


def collect_recipes() -> list[dict]:
	"""Fetch the index page, then collect data for each linked recipe."""
	# On commence par la page d'accueil des recettes.
	index_soup = get_soup(BASE_URL)
	recipe_urls = get_recipe_urls(index_soup)
	# Puis on visite chaque recette pour en extraire les donnees.
	return [get_recipe_data(recipe_url) for recipe_url in recipe_urls]


def print_recipe_summaries(recipes: list[dict]) -> None:
	"""Print a short preview for each scraped recipe."""
	for recipe in recipes:
		# On limite l'affichage a un extrait pour garder une sortie lisible.
		preview = recipe["text"][:200]
		print(f"Title: {recipe['title']}")
		print(f"URL: {recipe['url']}")
		print(f"Recipe: {preview}...")
		print("-" * 60)


def main() -> None:
	"""Run the refactored recipe scraper from start to finish."""
	# Enchaine toutes les etapes du scraping de facon claire.
	recipes = collect_recipes()
	print_recipe_summaries(recipes)


if __name__ == "__main__":
	main()
