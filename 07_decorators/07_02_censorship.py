# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

import re


def censor(bad_words=None):
	# Si aucun mot n'est fourni, on utilise une petite liste par defaut.
	if bad_words is None:
		bad_words = ["shoot"]

	# On cree un ensemble en minuscules pour des comparaisons rapides et fiables.
	blocked = {word.lower() for word in bad_words}

	# Fonction utilitaire: garde la premiere lettre et remplace le reste par des *.
	def mask_word(word):
		if len(word) <= 1:
			return "*"
		return word[0] + "*" * (len(word) - 1)

	# Ce niveau recoit la fonction a decorer.
	def decorator(func):
		# Ce wrapper appelle la fonction d'origine puis censure son texte.
		def wrapper(*args, **kwargs):
			original_text = func(*args, **kwargs)

			# Fonction de remplacement pour chaque mot reconnu par la regex.
			def replace_match(match):
				found_word = match.group(0)
				if found_word.lower() in blocked:
					return mask_word(found_word)
				return found_word

			# \b\w+\b trouve les mots et conserve la ponctuation autour.
			return re.sub(r"\b\w+\b", replace_match, original_text)

		return wrapper

	return decorator


# Exemple d'utilisation du decorateur sans argument (liste par defaut).
@censor()
def injured_toe_text():
	return "I bumped my toe! Shoot!"


# Affiche: I bumped my toe! S****!
print(injured_toe_text())
