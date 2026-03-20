# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import unittest


# PSEUDOCODE (approche TDD):
# 1) Ecrire un test qui decrit le comportement attendu.
# 2) Lancer les tests (ils echouent au debut: phase RED).
# 3) Implementer ensuite le minimum de code pour faire passer les tests.
#
# Fonctions prevues (non implementees ici volontairement):
# - add_numbers(a, b) -> somme de deux nombres
# - subtract_numbers(a, b) -> difference de deux nombres


class TestBasicMathTDD(unittest.TestCase):
	# Cas nominal: addition simple
	def test_add_numbers_with_integers(self):
		self.assertEqual(add_numbers(2, 3), 5)

	# Cas nominal: soustraction simple
	def test_subtract_numbers_with_integers(self):
		self.assertEqual(subtract_numbers(10, 4), 6)

	# Cas d'erreur: type invalide pour l'addition
	def test_add_numbers_raises_type_error_for_invalid_type(self):
		with self.assertRaises(TypeError):
			add_numbers("2", 3)

	# Cas d'erreur: type invalide pour la soustraction
	def test_subtract_numbers_raises_type_error_for_invalid_type(self):
		with self.assertRaises(TypeError):
			subtract_numbers(None, 3)


if __name__ == "__main__":
	unittest.main()
