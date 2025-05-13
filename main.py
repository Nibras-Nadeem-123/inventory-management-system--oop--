# importing necessary classes and functions from other modules
from inventory import Inventory
from product import Electronics, Grocery, Clothing
from utils import save_to_file, load_from_file

# main function for running the CLI
def main():
    # create a new inventory instance
    inventory = Inventory()

    # start the cli loop
    while True:
        # display menu options
        print("\n--- Inventory System Menu ---")
        print("1. Add product")
        print("2. Sell product")
        print("3. View products")
        print("4. Search by name")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Remove expired (grocery)")
        print("8. Exit")

        # ask user to choose an action
        choice = input("Choose an option: ")

        # add product
        if choice == "1":
            print("Which type? (1. Electronics, 2. Grocery, 3. Clothing)")
            ptype = input("Type: ")  # get product type
            id = input("ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            qty = int(input("Stock: "))

            # create product object based on type
            if ptype == "1":
                brand = input("Brand: ")
                warranty = int(input("Warranty (years): "))
                p = Electronics(id, name, price, qty, warranty, brand)
            elif ptype == "2":
                expiry = input("Expiry date (YYYY-MM-DD): ")
                p = Grocery(id, name, price, qty, expiry)
            elif ptype == "3":
                size = input("Size: ")
                material = input("Material: ")
                p = Clothing(id, name, price, qty, size, material)
            else:
                print("Invalid type.")
                continue

            # try adding the product to the inventory
            try:
                inventory.add_product(p)
                print("Product added.")
            except Exception as e:
                print(f"Error: {e}")

        # sell product
        elif choice == "2":
            pid = input("Product ID: ")
            qty = int(input("Quantity to sell: "))
            try:
                inventory.sell_product(pid, qty)
                print("Product sold.")
            except Exception as e:
                print(f"Error: {e}")

        # view all products
        elif choice == "3":
            for p in inventory.list_all_products():
                print(p)

        # search products by name
        elif choice == "4":
            name = input("Search name: ")
            results = inventory.search_by_name(name)
            for p in results:
                print(p)

        # save inventory to JSON file
        elif choice == "5":
            save_to_file("inventory.json", inventory)
            print("Saved.")

        # load inventory from JSON file
        elif choice == "6":
            inventory = load_from_file("inventory.json")
            print("Loaded.")

        # remove expired groceries from inventory
        elif choice == "7":
            inventory.remove_expired_products()
            print("Expired items removed.")

        # exit program
        elif choice == "8":
            print("Goodbye!")
            break

        # handle invalid input
        else:
            print("Invalid option.")

# run the program
if __name__ == "__main__":
    main()
