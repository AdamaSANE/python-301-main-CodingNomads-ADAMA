# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)

import unittest


def calculate_discount(price, percent):
	"""Return le prix apres reduction en pourcentage."""
	return price - (price * percent / 100)


class TestCalculateDiscount(unittest.TestCase):
	# Test nominal: une reduction de 20% sur 100 donne 80
	def test_calculate_discount_standard_case(self):
		self.assertEqual(calculate_discount(100, 20), 80)

	# Test decimal: verification avec assertAlmostEqual
	def test_calculate_discount_decimal_result(self):
		self.assertAlmostEqual(calculate_discount(19.99, 10), 17.991)

	# Test volontairement faux pour montrer un echec de test
	def test_intentional_failure(self):
		self.assertEqual(calculate_discount(50, 10), 40)


if __name__ == "__main__":
	unittest.main()
