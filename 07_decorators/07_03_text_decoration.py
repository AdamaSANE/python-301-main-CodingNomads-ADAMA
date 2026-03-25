# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************


def decorate(symbol):
	# Ce niveau recoit le symbole choisi pour la decoration (ex: "*", "#", "-").
	def decorator(func):
		# Ce wrapper appelle la fonction d'origine puis entoure son texte d'une bordure.
		def wrapper(*args, **kwargs):
			text = func(*args, **kwargs)

			# On convertit en str pour eviter les erreurs si la fonction retourne autre chose.
			text = str(text)

			# Largeur de la bordure: au moins 30 caracteres, ou plus si le texte est plus long.
			border_width = max(30, len(text))
			border = symbol * border_width

			# On retourne le texte final sur 3 lignes: bordure, contenu, bordure.
			return f"{border}\n{text}\n{border}"

		return wrapper

	return decorator


# Exemple d'utilisation du decorateur avec le symbole "*".
@decorate("*")
def say_hello():
	return "Hello"


# Affiche la version "decoree" du texte sur 3 lignes.
print(say_hello())
