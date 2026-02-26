class Product:
    def __init__(self, name, price, quantity, id):
        self.__validate_name(name)
        self.__name = name

        self.__validate_price(price)
        self.__price = price

        self.__validate_quantity(quantity)
        self.__quantity = quantity

        self.__id = id

    def get_id(self):
        return self.__id

    def set_product_name(self, item_name):
        self.__name = item_name

    def get_product_name(self):
        return self.__name

    def set_product_quantity(self, item_quantity):
        self.__quantity = item_quantity

    def get_product_quantity(self):
        return self.__quantity

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def __validate_name(self, name):
        if name is None or str(name).strip() == "":
            raise ValueError("Username cannot be null or empty")

    def __validate_price(self, price):
        if price < 100:
            raise ValueError("Price must be greater than 100")

    def __validate_quantity(self, quantity):
        if quantity < 1:
            raise ValueError("Quantity must be greater than 0")
