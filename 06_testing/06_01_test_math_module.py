# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import math
import unittest


class TestMathModule(unittest.TestCase):
	# Vérifie une racine carrée exacte
	def test_sqrt_returns_expected_value(self):
		self.assertEqual(math.sqrt(81), 9)

	# Vérifie un calcul de factorielle connu
	def test_factorial_returns_expected_value(self):
		self.assertEqual(math.factorial(5), 120)

	# Vérifie qu'une valeur négative lève une erreur pour sqrt
	def test_sqrt_raises_value_error_for_negative_input(self):
		with self.assertRaises(ValueError):
			math.sqrt(-1)


if __name__ == "__main__":
	unittest.main()
