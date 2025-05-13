# import modules for JSON handling and product classes
import json
from product import Electronics, Grocery, Clothing
from exceptions import InvalidProductDataError

# helper function to convert a product object into a dictionary for JSON storage
def serialize_product(product):
    # base dictionary with common product attributes
    base = {
        "product_id": product._product_id,
        "name": product._name,
        "price": product._price,
        "quantity_in_stock": product._quantity_in_stock,
        "type": product.__class__.__name__  # store the class name to identify the type later
    }

    # add type-specific attributes
    if isinstance(product, Electronics):
        base.update({
            "warranty_years": product.warranty_years,
            "brand": product.brand
        })
    elif isinstance(product, Grocery):
        base.update({
            "expiry_date": product.expiry_date.strftime("%Y-%m-%d")  # Convert date to string
        })
    elif isinstance(product, Clothing):
        base.update({
            "size": product.size,
            "material": product.material
        })
    
    return base  # return the full product dictionary

# function to save the inventory data to a JSON file
def save_to_file(filename, inventory):
    with open(filename, 'w') as f:
        # convert all products to dictionaries and write to file with indentation
        json.dump([serialize_product(p) for p in inventory.list_all_products()], f, indent=2)

# function to load inventory data from a JSON file
def load_from_file(filename):
    from inventory import Inventory  # local import to avoid circular dependency
    inventory = Inventory()  # create a new empty inventory

    with open(filename, 'r') as f:
        data = json.load(f)  # load JSON data from file
        
        for item in data:
            product_type = item.pop('type', None)  # extract the type of product
            
            try:
                # based on the type, create the appropriate product object
                if product_type == "Electronics":
                    p = Electronics(
                        product_id=item["product_id"],
                        name=item["name"],
                        price=item["price"],
                        quantity_in_stock=item["quantity_in_stock"],
                        warranty_years=item["warranty_years"],
                        brand=item["brand"]
                    )
                elif product_type == "Grocery":
                    p = Grocery(
                        product_id=item["product_id"],
                        name=item["name"],
                        price=item["price"],
                        quantity_in_stock=item["quantity_in_stock"],
                        expiry_date=item["expiry_date"]
                    )
                elif product_type == "Clothing":
                    p = Clothing(
                        product_id=item["product_id"],
                        name=item["name"],
                        price=item["price"],
                        quantity_in_stock=item["quantity_in_stock"],
                        size=item["size"],
                        material=item["material"]
                    )
                else:
                    # if the type is unknown, raise a custom exception
                    raise InvalidProductDataError("Unknown product type.")

                # add the product to the inventory
                inventory.add_product(p)

            except Exception as e:
                # print error message if any issue occurs during loading
                print(f"Error loading product: {e}")

    return inventory  # return the populated inventory
