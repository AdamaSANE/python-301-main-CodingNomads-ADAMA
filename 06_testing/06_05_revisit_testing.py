# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.

import unittest


class PrinceException(Exception):
	"""Levee quand le mot 'Prince' apparait dans les 100 premiers caracteres."""


# Version refactorisee:
# - Plus concise que la version imperative avec plusieurs blocs try/except.
# - Facile a tester car la logique est isolee dans une fonction pure.
def validate_no_prince_in_first_100(text):
	"""Valide qu'il n'y a pas 'Prince' dans les 100 premiers caracteres."""
	# On limite la recherche au debut du texte et on ignore la casse.
	if "prince" in text[:100].lower():
		raise PrinceException("Le mot 'Prince' est present au debut du texte.")
	return True


class TestValidateNoPrince(unittest.TestCase):
	# Cas nominal: pas de mot interdit au debut
	def test_returns_true_when_prince_not_in_first_100(self):
		text = "Bonjour " * 20
		self.assertTrue(validate_no_prince_in_first_100(text))

	# Cas d'erreur: le mot apparait dans les 100 premiers caracteres
	def test_raises_exception_when_prince_in_first_100(self):
		text = "Il etait une fois un Prince courageux." + ("x" * 80)
		with self.assertRaises(PrinceException):
			validate_no_prince_in_first_100(text)

	# Cas limite: le mot est apres le 100e caractere, donc accepte
	def test_allows_prince_after_first_100_characters(self):
		text = ("x" * 100) + "Prince"
		self.assertTrue(validate_no_prince_in_first_100(text))

	# Cas robustesse: verifie la recherche insensible a la casse
	def test_raises_exception_case_insensitive(self):
		text = "prInCe est ici"
		with self.assertRaises(PrinceException):
			validate_no_prince_in_first_100(text)


if __name__ == "__main__":
	unittest.main()
