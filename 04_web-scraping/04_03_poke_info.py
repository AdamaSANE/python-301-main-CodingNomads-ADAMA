# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

BASE_URL = "https://pokeapi.co/api/v2/"

import requests

TEAM = ["pikachu", "charizard", "bulbasaur", "squirtle", "gengar", "lucario"]


def get_pokemon_info(name: str) -> dict:
	response = requests.get(f"{BASE_URL}pokemon/{name}", timeout=15)
	response.raise_for_status()
	data = response.json()

	return {
		"name": data["name"],
		"number": data["id"],
		"types": [item["type"]["name"] for item in data["types"]],
	}


def main() -> None:
	team_info = [get_pokemon_info(pokemon) for pokemon in TEAM]

	print("My Pokemon Team")
	print("=" * 40)
	for pokemon in team_info:
		print(f"Name: {pokemon['name'].title()}")
		print(f"Number: #{pokemon['number']}")
		print(f"Types: {', '.join(pokemon['types'])}")
		print("-" * 40)


if __name__ == "__main__":
	main()
