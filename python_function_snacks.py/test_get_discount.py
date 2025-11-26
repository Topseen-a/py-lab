import unittest
import get_discount

class TestGetDiscount(unittest.TestCase):
    def test_that_get_discount_exist(self):
        get_discount.get_discount('item name', 50, 'promo code')

    def test_that_get_discount_returns_discount_save10(self):
        actual = get_discount.get_discount('item name', 50, 'promocode')
        expected = 45
        self.assertEqual(actual,expected)
