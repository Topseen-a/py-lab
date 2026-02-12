from e_store.product_category import ProductCategory


class Product:
    product_id: str
    product_name: str
    price: float
    product_description: str
    category: ProductCategory