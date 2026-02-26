from abc import ABC

from e_store.address import Address


class User(ABC):
    name: str
    age: str
    email: str
    password: str
    phone: str
    home_address: Address