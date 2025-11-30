import unittest
import function_snacks

class TestFunctionSnacks(unittest.TestCase):
    def test_that_get_discount_exist(self):
        function_snacks.get_discount('item name', 50, 'promocode')

    def test_that_get_discount_returns_discount_save10(self):
        actual = function_snacks.get_discount('item name', 50, 'SAVE10')
        expected = 45
        self.assertEqual(actual,expected)

    def test_that_get_discount_returns_discount_halfoff(self):
        actual = function_snacks.get_discount('item name', 50, 'HALFOFF')
        expected = 25
        self.assertEqual(actual,expected)

    def test_that_get_discount_returns_no_discount(self):
        actual = function_snacks.get_discount('item name', 50, '')
        expected = 50
        self.assertEqual(actual,expected)


    def test_that_is_palindrome_prime_exist(self):
        function_snacks.is_palindrome_prime(757)

    def test_that_is_palindrome_prime_returns_palindrome_prime(self):
        actual = function_snacks.is_palindrome_prime(757)
        expected = True
        self.assertEqual(actual,expected)
