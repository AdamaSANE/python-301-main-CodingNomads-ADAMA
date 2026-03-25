# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

import re


def censor(*bad_words):
	# On normalise les mots interdits en minuscules pour une censure insensible a la casse.
	blocked = {word.lower() for word in bad_words}

	# Si aucun mot n'est passe, le decorateur laisse le texte intact.
	if not blocked:
		def passthrough_decorator(func):
			return func

		return passthrough_decorator

	# Fonction utilitaire: conserve la premiere lettre et masque le reste.
	def mask_word(word):
		if len(word) <= 1:
			return "*"
		return word[0] + "*" * (len(word) - 1)

	# Ce niveau recoit la fonction a decorer.
	def decorator(func):
		# Le wrapper execute la fonction puis filtre son texte de sortie.
		def wrapper(*args, **kwargs):
			original_text = str(func(*args, **kwargs))

			# Fonction appelee pour chaque mot trouve par la regex.
			def replace_match(match):
				found_word = match.group(0)
				if found_word.lower() in blocked:
					return mask_word(found_word)
				return found_word

			# \b\w+\b capture les mots sans detruire la ponctuation.
			return re.sub(r"\b\w+\b", replace_match, original_text)

		return wrapper

	return decorator


# Exemple: on censure plusieurs mots en meme temps.
@censor("shoot", "crab")
def frustrated_sentence():
	return "I bumped my toe! Shoot! Holy crab..."


# Resultat attendu: I bumped my toe! S****! Holy c***...
print(frustrated_sentence())
