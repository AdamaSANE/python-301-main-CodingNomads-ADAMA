# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

import unittest

from mymath import CustomZeroDivsionError, subtract_divide


class TestSubtractDivide(unittest.TestCase):
	def test_subtract_divide_returns_correct_result(self):
		# Cas nominal: 10 / (6 - 4) = 5
		result = subtract_divide(10, 6, 4)
		self.assertEqual(result, 5)

	def test_subtract_divide_raises_custom_zero_division_error(self):
		# Cas d'erreur: 5 - 5 = 0 doit lever l'exception personnalisée
		with self.assertRaises(CustomZeroDivsionError):
			subtract_divide(10, 5, 5)


if __name__ == "__main__":
	unittest.main()

