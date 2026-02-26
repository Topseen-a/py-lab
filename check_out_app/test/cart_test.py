import unittest

from model.cart import Cart


class CartTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_that_cart_should_be_empty_at_initial(self):
        self.assertEqual(self.cart.get_quantity_of_products(), 0)

    def test_that_items_can_be_added_to_cart(self):
        self.assertEqual(self.cart.get_quantity_of_products(), 0)

        self.cart.add_product("Rice", 200, 1)
        self.cart.add_product("Beans", 200, 1)

        self.assertEqual(self.cart.get_quantity_of_products(), 2)

    def test_that_product_cannot_be_added_to_cart_with_invalid_name(self):
        self.assertEqual(self.cart.get_quantity_of_products(), 0)

        with self.assertRaises(ValueError):
            self.cart.add_product(" ", 200, 2)

    def test_that_product_cannot_be_added_to_the_cart_with_invalid_price_(self):
        self.assertEqual(self.cart.get_quantity_of_products(), 0)

        with self.assertRaises(ValueError):
            self.cart.add_product("Beans", 50, 2)

    def test_that_product_cannot_be_added__to_the_cart_with_invalid_quantity(self):
        self.assertEqual(self.cart.get_quantity_of_products(), 0)

        with self.assertRaises(ValueError):
            self.cart.add_product("Beans", 200, -1)

    def test_that_product_can_be_removed_from_cart_with_valid_id(self):
        self.assertEqual(self.cart.get_quantity_of_products(), 0)
        self.cart.add_product("Rice", 200, 1)
        self.cart.add_product("Beans", 200, 1)
        self.cart.add_product("Egg", 200, 1)

        self.cart.remove_product(1)
        self.assertEqual(self.cart.get_quantity_of_products(), 2)

    def test_that_product_cannot_be_removed_from_cart_with_invalid_id(self):
        self.assertEqual(self.cart.get_quantity_of_products(), 0)
        self.cart.add_product("Rice", 200, 1)
        self.cart.add_product("Beans", 200, 1)
        self.cart.add_product("Egg", 200, 1)

        with self.assertRaises(ValueError):
            self.cart.remove_product(4)

    def test_that_product_can_be_gotten_from_the_cart(self):
        self.assertEqual(self.cart.get_quantity_of_products(), 0)

        self.cart.add_product("Rice", 200, 1)
        self.cart.add_product("Beans", 200, 1)
        self.cart.add_product("Egg", 200, 1)

        products = self.cart.get_products()

        self.assertEqual(len(products), 3)
        self.assertEqual(self.cart.get_quantity_of_products(), 3)




