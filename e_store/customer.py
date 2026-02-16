from typing import List

from e_store.user import User


class Customer(User):
    billing_information: List["BillingInformation"]
    shopping_cart: "ShoppingCart"