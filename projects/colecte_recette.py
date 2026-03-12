"""CLI de recherche de recettes CodingNomads par ingredients.

Ce script :
1) telecharge la collection de recettes (une seule fois),
2) met les pages en cache local pour limiter les requetes,
3) permet a l'utilisateur de saisir des ingredients,
4) retourne les recettes dont le texte contient ces ingredients.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://codingnomads.github.io/recipes/"
PROJECT_DIR = Path(__file__).resolve().parent
CACHE_DIR = PROJECT_DIR / "recipe_cache"
INDEX_CACHE_FILE = CACHE_DIR / "index.html"
RECIPES_JSON_FILE = CACHE_DIR / "recipes.json"


@dataclass
class Ingredient:
	"""Represente un ingredient saisi par l'utilisateur."""

	name: str

	def normalized(self) -> str:
		"""Version normalisee pour les comparaisons (minuscule + sans espaces inutiles)."""
		return self.name.strip().lower()


@dataclass
class Recipe:
	"""Represente une recette recuperee depuis le site."""

	title: str
	url: str
	text: str

	def contains_ingredient(self, ingredient: Ingredient) -> bool:
		"""Verifie la presence d'un ingredient dans le texte de recette."""
		# \b force une correspondance sur mot entier (evite les faux positifs).
		pattern = rf"\b{re.escape(ingredient.normalized())}\b"
		return re.search(pattern, self.text.lower()) is not None


def fetch_html(url: str) -> str:
	"""Telecharge le HTML d'une page web."""
	response = requests.get(url, timeout=20)
	response.raise_for_status()
	return response.text


def save_text(path: Path, content: str) -> None:
	"""Ecrit du texte dans un fichier, en creant les dossiers si besoin."""
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_text(content, encoding="utf-8")


def read_text(path: Path) -> str:
	"""Lit un fichier texte UTF-8."""
	return path.read_text(encoding="utf-8")


def get_index_html(force_refresh: bool = False) -> str:
	"""Recupere l'HTML d'index depuis le cache ou le web."""
	if not force_refresh and INDEX_CACHE_FILE.exists():
		return read_text(INDEX_CACHE_FILE)

	index_html = fetch_html(BASE_URL)
	save_text(INDEX_CACHE_FILE, index_html)
	return index_html


def extract_recipe_urls(index_html: str) -> list[str]:
	"""Extrait les URLs de recettes a partir de la page index."""
	soup = BeautifulSoup(index_html, "html.parser")
	urls: list[str] = []

	for link in soup.find_all("a", href=True):
		href = link["href"]
		if href.startswith("recipes/"):
			urls.append(urljoin(BASE_URL, href))

	# dict.fromkeys conserve l'ordre tout en supprimant les doublons.
	return list(dict.fromkeys(urls))


def extract_recipe_text_and_title(recipe_html: str) -> tuple[str, str]:
	"""Extrait le titre et le texte principal d'une page recette."""
	soup = BeautifulSoup(recipe_html, "html.parser")

	heading = soup.find("h1")
	title = heading.get_text(strip=True) if heading else "Untitled"

	# Plusieurs selecteurs sont testes pour rester robuste aux variations HTML.
	selectors = [
		("div", {"class": "recipe-body"}),
		("article", {}),
		("main", {}),
	]

	for tag_name, attrs in selectors:
		container = soup.find(tag_name, attrs=attrs)
		if container:
			return title, container.get_text(" ", strip=True)

	# Fallback si la structure ne correspond pas aux selecteurs ci-dessus.
	return title, soup.get_text(" ", strip=True)


def build_recipe_collection(force_refresh: bool = False) -> list[Recipe]:
	"""Construit la collection de recettes (depuis cache JSON ou via scraping)."""
	if not force_refresh and RECIPES_JSON_FILE.exists():
		cached_data = json.loads(read_text(RECIPES_JSON_FILE))
		return [Recipe(**item) for item in cached_data]

	index_html = get_index_html(force_refresh=force_refresh)
	recipe_urls = extract_recipe_urls(index_html)
	recipes: list[Recipe] = []

	for url in recipe_urls:
		recipe_html = fetch_html(url)
		title, text = extract_recipe_text_and_title(recipe_html)
		recipes.append(Recipe(title=title, url=url, text=text))

	serializable = [recipe.__dict__ for recipe in recipes]
	save_text(RECIPES_JSON_FILE, json.dumps(serializable, ensure_ascii=False, indent=2))
	return recipes


def parse_user_ingredients(raw_input: str) -> list[Ingredient]:
	"""Convertit une saisie CSV en objets Ingredient."""
	parts = [part.strip() for part in raw_input.split(",")]
	clean_names = [name for name in parts if name]
	return [Ingredient(name=name) for name in clean_names]


def find_matching_recipes(recipes: list[Recipe], ingredients: list[Ingredient]) -> list[Recipe]:
	"""Retourne les recettes qui contiennent tous les ingredients saisis."""
	if not ingredients:
		return []

	matches: list[Recipe] = []
	for recipe in recipes:
		if all(recipe.contains_ingredient(ingredient) for ingredient in ingredients):
			matches.append(recipe)

	return matches


def print_results(matches: list[Recipe], ingredients: list[Ingredient]) -> None:
	"""Affiche les resultats de recherche dans la console."""
	search_terms = ", ".join(ing.normalized() for ing in ingredients)
	print("\nRecherche d'ingredients:", search_terms)
	print("=" * 70)

	if not matches:
		print("Aucune recette ne contient tous ces ingredients.")
		return

	print(f"{len(matches)} recette(s) trouvee(s):")
	for idx, recipe in enumerate(matches, start=1):
		preview = recipe.text[:180]
		print(f"\n{idx}. {recipe.title}")
		print(f"URL: {recipe.url}")
		print(f"Extrait: {preview}...")


def parse_args() -> argparse.Namespace:
	"""Parse les arguments de ligne de commande."""
	parser = argparse.ArgumentParser(description="Chercher des recettes par ingredients.")
	parser.add_argument(
		"--ingredients",
		type=str,
		help="Liste d'ingredients separes par des virgules (ex: tomato, onion, garlic)",
	)
	parser.add_argument(
		"--refresh",
		action="store_true",
		help="Force la mise a jour du cache depuis le web.",
	)
	return parser.parse_args()


def main() -> None:
	"""Point d'entree principal de la CLI."""
	args = parse_args()

	# L'utilisateur peut fournir les ingredients via argument ou en interactif.
	if args.ingredients:
		raw_ingredients = args.ingredients
	else:
		raw_ingredients = input("Entrez des ingredients (separes par des virgules): ")

	ingredients = parse_user_ingredients(raw_ingredients)
	if not ingredients:
		print("Aucun ingredient valide saisi.")
		return

	recipes = build_recipe_collection(force_refresh=args.refresh)
	matches = find_matching_recipes(recipes, ingredients)
	print_results(matches, ingredients)


if __name__ == "__main__":
	main()
