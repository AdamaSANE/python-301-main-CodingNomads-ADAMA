# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.


def quote_wrap(func):
	# Le wrapper intercepte le resultat de la fonction et l'entoure de guillemets.
	def wrapper(*args, **kwargs):
		text = func(*args, **kwargs)
		return f'"{text}"'

	# On retourne la nouvelle fonction qui remplace temporairement l'originale.
	return wrapper


# Cette fonction retourne du texte normal, puis le decorateur ajoute les guillemets.
@quote_wrap
def greet(name):
	return f"Hello {name}!"


# Affiche le texte final deja enveloppe de guillemets.
print(greet("world"))
