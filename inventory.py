# import base Product class and grocery subclass
from product import Product, Grocery

# import custom exceptions
from exceptions import DuplicateProductIDError, ProductNotFoundError

# JSON is imported in case its needed for serialization
import json

class Inventory:
    def __init__(self):
        # dictionary to hold products using product id as the key
        self._products = {}

    def add_product(self, product: Product):
        """
        adds a new product to the inventory.
        raises DuplicateProductIDError if product id already exists.
        """
        if product._product_id in self._products:
            raise DuplicateProductIDError("Duplicate product ID.")
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        """
        removes a product by id.
        raises ProductNotFoundError if product id does not exist.
        """
        if product_id not in self._products:
            raise ProductNotFoundError("Product not found.")
        del self._products[product_id]

    def search_by_name(self, name):
        """
        returns a list of products whose names contain the given substring (case-insensitive).
        """
        return [p for p in self._products.values() if name.lower() in p._name.lower()]

    def search_by_type(self, product_type):
        """
        returns a list of products that match the given class/type name (case-insensitive).
        """
        return [p for p in self._products.values() if p.__class__.__name__.lower() == product_type.lower()]

    def list_all_products(self):
        """
        returns a list of all products in the inventory.
        """
        return list(self._products.values())

    def sell_product(self, product_id, quantity):
        """
        sells a specified quantity of a product.
        raises ProductNotFoundError if product id is not found.
        """
        if product_id not in self._products:
            raise ProductNotFoundError("Product not found.")
        self._products[product_id].sell(quantity)

    def restock_product(self, product_id, quantity):
        """
        increases stock of a product by the specified quantity.
        raises ProductNotFoundError if product id is not found.
        """
        if product_id not in self._products:
            raise ProductNotFoundError("Product not found.")
        self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        """
        calculates the total value of all products in inventory.
        """
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        """
        removes expired grocery products from the inventory.
        only checks for instances of grocery and calls their is_expired() method.
        """
        self._products = {
            pid: p for pid, p in self._products.items()
            if not (isinstance(p, Grocery) and p.is_expired())
        }
