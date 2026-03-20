# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.

from pathlib import Path
import importlib.util

import pytest


# Charge le module rescrape.py depuis son chemin (dossier avec tiret dans le nom).
MODULE_PATH = Path(__file__).parent / "06_05_recipe-scraper" / "rescrape.py"
spec = importlib.util.spec_from_file_location("rescrape", MODULE_PATH)
rescrape = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rescrape)


@pytest.fixture
def index_html():
	# HTML factice pour tester l'extraction des liens
	return """
	<html>
		<body>
			<a href="recipe-1.html">Recipe 1</a>
			<a href="recipe-2.html">Recipe 2</a>
		</body>
	</html>
	"""


@pytest.fixture
def recipe_html():
	# HTML factice pour tester auteur + recette
	return """
	<html>
		<body>
			<p class="author">by Ada Lovelace</p>
			<div class="md">Mix, bake, enjoy.</div>
		</body>
	</html>
	"""


def test_make_soup_returns_parsable_object(index_html):
	# Vérifie que make_soup crée un objet qu'on peut interroger
	soup = rescrape.make_soup(index_html)
	assert soup.find("a") is not None


def test_get_recipe_links_returns_all_links(index_html):
	# Vérifie l'extraction de tous les liens de recette
	soup = rescrape.make_soup(index_html)
	assert rescrape.get_recipe_links(soup) == ["recipe-1.html", "recipe-2.html"]


def test_get_author_extracts_author_name(recipe_html):
	# Vérifie que le préfixe "by " est retiré
	soup = rescrape.make_soup(recipe_html)
	assert rescrape.get_author(soup) == "Ada Lovelace"


def test_get_recipe_extracts_recipe_text(recipe_html):
	# Vérifie l'extraction du texte de recette
	soup = rescrape.make_soup(recipe_html)
	assert rescrape.get_recipe(soup) == "Mix, bake, enjoy."


def test_get_page_content_calls_requests_get(monkeypatch):
	# Mock réseau: on intercepte requests.get pour éviter Internet
	class DummyResponse:
		text = "<html></html>"

	def fake_get(url):
		assert url == "https://example.com"
		return DummyResponse()

	monkeypatch.setattr(rescrape.requests, "get", fake_get)

	page = rescrape.get_page_content("https://example.com")
	assert page.text == "<html></html>"


def test_get_html_content_returns_text(monkeypatch):
	# Vérifie que get_html_content renvoie exactement .text de la réponse
	class DummyResponse:
		text = "<html><body>ok</body></html>"

	def fake_get_page_content(url):
		assert url == "https://example.com"
		return DummyResponse()

	monkeypatch.setattr(rescrape, "get_page_content", fake_get_page_content)

	html = rescrape.get_html_content("https://example.com")
	assert html == "<html><body>ok</body></html>"
