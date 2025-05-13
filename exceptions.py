# custom exception for handling duplicate product IDs
class DuplicateProductIDError(Exception):
    """
    raised when trying to add a product with an id that already exists in the inventory.
    """
    pass

# custom exception for handling cases where a product is not found
class ProductNotFoundError(Exception):
    """
    raised when trying to access or modify a product that does not exist in the inventory.
    """
    pass

# custom exception for handling invalid product data (e.g., during file loading)
class InvalidProductDataError(Exception):
    """
    raised when product data is invalid or corrupted, such as missing fields or incorrect types.
    """
    pass
