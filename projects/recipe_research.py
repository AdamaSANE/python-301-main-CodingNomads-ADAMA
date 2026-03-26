"""Build a recipe search URL from available ingredients.

Exercise goal:
- Model available ingredients in an ``Ingredients`` class.
- Convert user input into clean ingredient tokens.
- Build a URL that can be opened in a browser to search recipes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from urllib.parse import quote_plus


@dataclass
class Ingredients:
	"""Store and prepare ingredient names for web searches."""

	items: list[str] = field(default_factory=list)

	def add_from_csv(self, raw_csv: str) -> None:
		"""Parse comma-separated user input and append clean ingredient names."""
		parts = [part.strip().lower() for part in raw_csv.split(",")]
		clean_parts = [part for part in parts if part]
		self.items.extend(clean_parts)

	def unique_items(self) -> list[str]:
		"""Return items without duplicates while preserving insertion order."""
		return list(dict.fromkeys(self.items))

	def build_search_url(self, base_url: str = "https://www.allrecipes.com/search/results/?search=") -> str:
		"""Build a recipe search URL for all available ingredients.

		Raises:
			ValueError: If there are no ingredients to search for.
		"""
		ingredients = self.unique_items()
		if not ingredients:
			raise ValueError("Add at least one ingredient before building a search URL.")

		# Join terms in one query string, then URL-encode for safe web usage.
		query = " ".join(ingredients)
		return f"{base_url}{quote_plus(query)}"


def main() -> None:
	"""Small CLI demo for the exercise."""
	print("Recipe URL builder")
	raw = input("Enter available ingredients (comma-separated): ")

	my_ingredients = Ingredients()
	my_ingredients.add_from_csv(raw)

	try:
		search_url = my_ingredients.build_search_url()
	except ValueError as exc:
		print(f"Error: {exc}")
		return

	print("\nNormalized ingredients:", my_ingredients.unique_items())
	print("Search URL:", search_url)


if __name__ == "__main__":
	main()
