# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi-iansedano.vercel.app/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

BASE_URL = "https://ghibliapi-iansedano.vercel.app"

import requests


def get_json(url: str):
	response = requests.get(url, timeout=15)
	response.raise_for_status()
	return response.json()


def main() -> None:
	species_url = f"{BASE_URL}/api/species"
	all_species = get_json(species_url)

	cat_species = [
		species
		for species in all_species
		if "cat" in species.get("name", "").lower()
	]

	if not cat_species:
		print("No cat-related species found.")
		return

	film_cache = {}

	for species in cat_species:
		species_name = species.get("name", "Unknown species")
		print(f"\n=== Species: {species_name} ===")

		people_urls = species.get("people", [])
		if not people_urls:
			print("No related characters.")
			continue

		for person_url in people_urls:
			if not person_url.startswith("http"):
				person_url = f"{BASE_URL}{person_url}"

			person = get_json(person_url)
			person_name = person.get("name", "Unknown")

			film_titles = []
			for film_url in person.get("films", []):
				if not film_url.startswith("http"):
					film_url = f"{BASE_URL}{film_url}"

				if film_url not in film_cache:
					film_cache[film_url] = get_json(film_url).get("title", "Unknown film")
				film_titles.append(film_cache[film_url])

			print(f"Character: {person_name}")
			if film_titles:
				print(f"Films: {', '.join(film_titles)}")
			else:
				print("Films: none listed")


if __name__ == "__main__":
	main()
