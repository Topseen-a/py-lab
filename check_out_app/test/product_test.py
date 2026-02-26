import unittest

from model.product import Product


class ProductTest(unittest.TestCase):

    def test_that_product_name_can_be_set(self):
        self.product = Product("Egg", 200, 1, 1)
        self.assertEqual("Egg", self.product.get_product_name())

    def test_that_product_price_can_be_set(self):
        self.product = Product("Egg", 200, 1, 1)
        self.assertEqual(200, self.product.get_price())

    def test_that_product_quantity_can_be_set(self):
        self.product = Product("Egg", 200, 1, 1)
        self.assertEqual(1, self.product.get_product_quantity())

    def test_that_product_id_can_be_set(self):
        self.product = Product("Egg", 200, 1, 1)
        self.assertEqual(1, self.product.get_id())
