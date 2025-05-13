# import necessary modules
from abc import ABC, abstractmethod  # for creating abstract base classes
from datetime import datetime        # for handling expiry dates in grocery

# abstract base class for all products
class Product(ABC):
    def __init__(self, product_id, name, price, quantity_in_stock):
        # encapsulated attributes (prefix with underscore)
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    def restock(self, amount):
        """
        increase stock by the given amount.
        """
        self._quantity_in_stock += amount

    def sell(self, quantity):
        """
        reduce stock by the given quantity.
        raises ValueError if there is not enough stock.
        """
        if quantity > self._quantity_in_stock:
            raise ValueError("Not enough stock to sell.")
        self._quantity_in_stock -= quantity

    def get_total_value(self):
        """
        return total value of product in stock (price * quantity).
        """
        return self._price * self._quantity_in_stock

    @abstractmethod
    def __str__(self):
        """
        abstract method to return a string representation of the product.
        must be implemented in subclasses.
        """
        pass

# subclass: electronics product
class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, warranty_years, brand):
        # initialize base class attributes
        super().__init__(product_id, name, price, quantity_in_stock)
        # additional attributes for electronics
        self.warranty_years = warranty_years
        self.brand = brand

    def __str__(self):
        """
        return string with product info including brand and warranty.
        """
        return f"[Electronics] {self._name} ({self.brand}) - ${self._price}, Qty: {self._quantity_in_stock}, Warranty: {self.warranty_years} years"

# subclass: grocery product
class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        # initialize base class attributes
        super().__init__(product_id, name, price, quantity_in_stock)
        # convert expiry_date string to datetime object
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")

    def is_expired(self):
        """
        check if the grocery item is expired based on current date.
        """
        return datetime.now() > self.expiry_date

    def __str__(self):
        """
        return string with product info including expiry date.
        """
        return f"[Grocery] {self._name} - ${self._price}, Qty: {self._quantity_in_stock}, Exp: {self.expiry_date.date()}"

# subclass: clothing product
class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        # initialize base class attributes
        super().__init__(product_id, name, price, quantity_in_stock)
        # additional attributes for clothing
        self.size = size
        self.material = material

    def __str__(self):
        """
        return string with product info including size and material.
        """
        return f"[Clothing] {self._name} ({self.size}, {self.material}) - ${self._price}, Qty: {self._quantity_in_stock}"
