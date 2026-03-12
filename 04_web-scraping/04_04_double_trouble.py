# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests


# API 1: fournit des profils d'utilisateurs aleatoires.
RANDOM_USER_URL = "https://randomuser.me/api/"
# API 2: estime l'age probable d'une personne a partir de son prenom.
AGIFY_URL = "https://api.agify.io"
# Nombre de profils a comparer dans le rapport final.
NUMBER_OF_USERS = 5


def get_random_users(results: int) -> list[dict]:
	# On demande plusieurs utilisateurs d'un coup pour limiter le nombre d'appels.
	response = requests.get(RANDOM_USER_URL, params={"results": results}, timeout=15)
	response.raise_for_status()
	data = response.json()

	users = []
	for user in data["results"]:
		# On garde uniquement les champs utiles pour la comparaison avec Agify.
		users.append(
			{
				"first_name": user["name"]["first"],
				"last_name": user["name"]["last"],
				"country": user["location"]["country"],
				"actual_age": user["dob"]["age"],
			}
		)

	return users


def get_estimated_age(first_name: str) -> dict:
	# Agify retourne une prediction basee sur les donnees disponibles pour ce prenom.
	response = requests.get(AGIFY_URL, params={"name": first_name}, timeout=15)
	response.raise_for_status()
	return response.json()


def combine_user_and_age_data(users: list[dict]) -> list[dict]:
	# Cette fonction relie les donnees des deux API en une structure unique.
	combined_data = []

	for user in users:
		estimation = get_estimated_age(user["first_name"])
		estimated_age = estimation.get("age")

		combined_data.append(
			{
				# Le nom complet est plus lisible dans le rapport final.
				"full_name": f"{user['first_name']} {user['last_name']}",
				"country": user["country"],
				"actual_age": user["actual_age"],
				"estimated_age": estimated_age,
				# Si Agify ne connait pas ce prenom, on laisse la difference a None.
				"difference": None if estimated_age is None else abs(user["actual_age"] - estimated_age),
			}
		)

	return combined_data


def print_report(combined_data: list[dict]) -> None:
	# Affiche une comparaison simple entre l'age reel et l'age estime.
	print("Random User + Agify")
	print("=" * 50)

	for person in combined_data:
		print(f"Name: {person['full_name']}")
		print(f"Country: {person['country']}")
		print(f"Actual age: {person['actual_age']}")
		if person["estimated_age"] is None:
			print("Estimated age by first name: unavailable")
			print("Difference: unavailable")
		else:
			print(f"Estimated age by first name: {person['estimated_age']}")
			print(f"Difference: {person['difference']} years")
		print("-" * 50)


def main() -> None:
	# 1. Recuperer les utilisateurs.
	users = get_random_users(NUMBER_OF_USERS)
	# 2. Completer chaque utilisateur avec l'estimation d'age.
	combined_data = combine_user_and_age_data(users)
	# 3. Afficher le resultat de la fusion des deux API.
	print_report(combined_data)


if __name__ == "__main__":
	main()
