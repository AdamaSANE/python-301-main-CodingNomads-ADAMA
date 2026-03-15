"""Projet Python: gestion des exceptions.

Ce script montre deux cas tres courants:
1) les erreurs reseau lors d'un scraping/API call
2) les erreurs de saisie utilisateur avec exceptions personnalisees
"""


class InvalidMenuChoiceError(Exception):
	"""Le choix de menu n'est pas valide."""


class InvalidPokemonTypeError(Exception):
	"""Le type Pokemon saisi n'est pas autorise."""


class QuitProgram(Exception):
	"""Exception de controle pour sortir proprement du programme."""


def safe_int_input(prompt):
	"""Lit un entier sans faire crasher le programme sur une mauvaise saisie."""
	while True:
		try:
			return int(input(prompt).strip())
		except ValueError:
			print("Entrer un nombre entier valide.")


def choose_menu_option():
	"""Lit le choix du menu et leve une exception personnalisee si besoin."""
	raw = input("Choix (1, 2 ou q): ").strip().lower()
	if raw == "q":
		raise QuitProgram("Arret demande par l'utilisateur.")
	if raw not in {"1", "2"}:
		raise InvalidMenuChoiceError(f"Option inconnue: {raw}")
	return raw


def choose_pokemon_type():
	"""Demande un type Pokemon et valide l'entree."""
	allowed = {"water", "fire", "grass"}
	pokemon_type = input("Type (water/fire/grass): ").strip().lower()

	if pokemon_type not in allowed:
		raise InvalidPokemonTypeError(
			f"Type '{pokemon_type}' invalide. Types autorises: {', '.join(sorted(allowed))}."
		)

	return pokemon_type


def fetch_url_excerpt(url, timeout=5):
	"""Recupere un extrait de page avec gestion robuste des erreurs requests."""
	try:
		import requests
	except ModuleNotFoundError:
		print("Le package requests n'est pas installe. Installer avec: pip install requests")
		return

	try:
		response = requests.get(url, timeout=timeout)
		response.raise_for_status()
	except requests.exceptions.Timeout:
		print("Erreur reseau: delai depasse (timeout).")
		return
	except requests.exceptions.ConnectionError:
		print("Erreur reseau: connexion impossible (internet/site indisponible).")
		return
	except requests.exceptions.HTTPError as exc:
		print(f"Erreur HTTP: {exc}")
		return
	except requests.exceptions.RequestException as exc:
		# Filet de securite pour toute autre erreur specifique a requests.
		print(f"Erreur requests: {exc}")
		return

	# Si aucune exception, on affiche un petit extrait du contenu.
	excerpt = response.text[:160].replace("\n", " ")
	print("Requete reussie. Extrait:")
	print(excerpt)


def demo_custom_exceptions():
	"""Demonstration d'exception personnalisee sur une saisie de type."""
	name = input("Nom du Pokemon: ").strip() or "Pokemon-sans-nom"

	try:
		pokemon_type = choose_pokemon_type()
	except InvalidPokemonTypeError as exc:
		print(f"Erreur de saisie: {exc}")
	else:
		print(f"Pokemon cree: {name} ({pokemon_type})")

	level = safe_int_input("Niveau du Pokemon (entier): ")
	print(f"Niveau enregistre: {level}")


def main():
	"""Boucle principale avec gestion d'erreurs sans traceback utilisateur."""
	print("Projet Exceptions - Demo")
	print("1) Tester les exceptions reseau (requests)")
	print("2) Tester les exceptions personnalisees (jeu CLI)")
	print("q) Quitter")

	while True:
		try:
			option = choose_menu_option()
		except InvalidMenuChoiceError as exc:
			print(f"Choix invalide: {exc}")
			continue
		except QuitProgram as exc:
			print(exc)
			break

		if option == "1":
			url = input("URL a tester (laisser vide pour https://example.com): ").strip()
			if not url:
				url = "https://example.com"
			fetch_url_excerpt(url)
		elif option == "2":
			demo_custom_exceptions()


if __name__ == "__main__":
	main()
