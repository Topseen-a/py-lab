import unittest
from model.cart import Cart

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
