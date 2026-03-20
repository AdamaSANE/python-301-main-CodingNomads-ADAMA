# Write a unittest test suite to test the rescrape module

import unittest
from unittest.mock import Mock, patch

import rescrape


class TestRescrape(unittest.TestCase):
	def setUp(self):
		# HTML factice pour tester l'extraction des liens de recettes
		self.index_html = """
		<html>
			<body>
				<a href="recipe-1.html">Recipe 1</a>
				<a href="recipe-2.html">Recipe 2</a>
			</body>
		</html>
		"""

		# HTML factice d'une page recette (auteur + contenu)
		self.recipe_html = """
		<html>
			<body>
				<p class="author">by Ada Lovelace</p>
				<div class="md">Mix, bake, enjoy.</div>
			</body>
		</html>
		"""

	def test_make_soup_returns_beautifulsoup_object(self):
		# Vérifie que make_soup crée un objet parsable
		soup = rescrape.make_soup(self.index_html)
		self.assertIsNotNone(soup.find("a"))

	def test_get_recipe_links_returns_all_links(self):
		# Vérifie l'extraction de tous les href présents
		soup = rescrape.make_soup(self.index_html)
		links = rescrape.get_recipe_links(soup)
		self.assertEqual(links, ["recipe-1.html", "recipe-2.html"])

	def test_get_author_extracts_author_name(self):
		# Vérifie que le préfixe "by " est retiré correctement
		soup = rescrape.make_soup(self.recipe_html)
		author = rescrape.get_author(soup)
		self.assertEqual(author, "Ada Lovelace")

	def test_get_recipe_extracts_recipe_text(self):
		# Vérifie l'extraction du texte de recette
		soup = rescrape.make_soup(self.recipe_html)
		recipe = rescrape.get_recipe(soup)
		self.assertEqual(recipe, "Mix, bake, enjoy.")

	@patch("rescrape.requests.get")
	def test_get_page_content_calls_requests_get(self, mock_get):
		# Mock réseau: on valide l'appel HTTP sans Internet
		mock_response = Mock()
		mock_response.text = "<html></html>"
		mock_get.return_value = mock_response

		page = rescrape.get_page_content("https://example.com")

		mock_get.assert_called_once_with("https://example.com")
		self.assertEqual(page.text, "<html></html>")

	@patch("rescrape.get_page_content")
	def test_get_html_content_returns_text(self, mock_get_page_content):
		# Vérifie que get_html_content renvoie bien la propriété .text
		mock_response = Mock()
		mock_response.text = "<html><body>ok</body></html>"
		mock_get_page_content.return_value = mock_response

		html = rescrape.get_html_content("https://example.com")

		mock_get_page_content.assert_called_once_with("https://example.com")
		self.assertEqual(html, "<html><body>ok</body></html>")


if __name__ == "__main__":
	unittest.main()
