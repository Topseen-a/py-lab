from model.product import Product


class Cart:
    def __init__(self):
        self.__products = []
        self.__quantity_of_products = 0
        self.__id = 0

    def get_quantity_of_products(self):
        return self.__quantity_of_products

    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity, self.__id)
        self.__products.append(new_product)
        self.__quantity_of_products += 1
        self.__id += 1

    def remove_product(self, id):
        for product in self.__products:
            if product.get_id() == id:
                self.__products.remove(product)
                self.__quantity_of_products -= 1
                return product
        self.__validate_id(id)
        return None

    def get_products(self):
        return self.__products

    def __validate_id(self, id):
        for product in self.__products:
            if product.get_id() != id:
                raise ValueError("Product id is invalid")