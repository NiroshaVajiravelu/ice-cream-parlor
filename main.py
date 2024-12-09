from database import IceCreamDatabase
from models import Flavor, Ingredient, Allergen, Cart
import sys

class IceCreamParlor:
    def __init__(self):
        self.db = IceCreamDatabase()
        self.cart = Cart()

    def run(self):
        while True:
            print("\n--- Ice Cream Parlor Management ---")
            print("1. Add Flavor")
            print("2. View Flavors")
            print("3. Search Flavors")
            print("4. Add Ingredient")
            print("5. Add Allergen")
            print("6. Manage Cart")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                self.add_flavor()
            elif choice == '2':
                self.view_flavors()
            elif choice == '3':
                self.search_flavors()
            elif choice == '4':
                self.add_ingredient()
            elif choice == '5':
                self.add_allergen()
            elif choice == '6':
                self.manage_cart()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Try again.")

    def add_flavor(self):
        name = input("Enter flavor name: ")
        description = input("Enter flavor description: ")
        is_seasonal = input("Is this a seasonal flavor? (y/n): ").lower() == 'y'
        price = float(input("Enter price: "))

        flavor = Flavor(name=name, description=description, is_seasonal=is_seasonal, price=price)
        flavor_id = self.db.add_flavor(flavor)
        if flavor_id:
            print(f"Flavor {name} added successfully!")

    def view_flavors(self):
        seasonal = input("View seasonal flavors only? (y/n): ").lower() == 'y'
        flavors = self.db.get_flavors(is_seasonal=seasonal)
        
        for flavor in flavors:
            print(f"ID: {flavor.id}, Name: {flavor.name}, Description: {flavor.description}, "
                  f"Seasonal: {'Yes' if flavor.is_seasonal else 'No'}, Price: ${flavor.price:.2f}")

    def search_flavors(self):
        keyword = input("Enter search keyword: ")
        flavors = self.db.search_flavors(keyword)
        
        for flavor in flavors:
            print(f"ID: {flavor.id}, Name: {flavor.name}, Description: {flavor.description}")

    def add_ingredient(self):
        name = input("Enter ingredient name: ")
        quantity = int(input("Enter quantity: "))
        unit = input("Enter unit (e.g., kg, lbs): ")

        ingredient = Ingredient(name=name, quantity=quantity, unit=unit)
        ingredient_id = self.db.add_ingredient(ingredient)
        if ingredient_id:
            print(f"Ingredient {name} added successfully!")

    def add_allergen(self):
        name = input("Enter allergen name: ")
        allergen = Allergen(name=name)
        allergen_id = self.db.add_allergen(allergen)
        if allergen_id:
            print(f"Allergen {name} added successfully!")

    def manage_cart(self):
        while True:
            print("\n--- Cart Management ---")
            print("1. Add Flavor to Cart")
            print("2. Remove Flavor from Cart")
            print("3. View Cart")
            print("4. Clear Cart")
            print("5. Return to Main Menu")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                flavor_id = int(input("Enter flavor ID to add: "))
                flavors = self.db.get_flavors()
                selected_flavor = next((f for f in flavors if f.id == flavor_id), None)
                if selected_flavor:
                    self.cart.add_item(selected_flavor)
                    print(f"{selected_flavor.name} added to cart!")
                else:
                    print("Flavor not found.")
            elif choice == '2':
                flavor_id = int(input("Enter flavor ID to remove: "))
                remove_flavor = next((f for f in self.cart.items if f.id == flavor_id), None)
                if remove_flavor:
                    self.cart.remove_item(remove_flavor)
                    print(f"{remove_flavor.name} removed from cart!")
                else:
                    print("Flavor not in cart.")
            elif choice == '3':
                print("\n--- Current Cart ---")
                for flavor in self.cart.items:
                    print(f"Name: {flavor.name}, Price: ${flavor.price:.2f}")
                print(f"Total Price: ${self.cart.total_price:.2f}")
            elif choice == '4':
                self.cart.clear()
                print("Cart cleared!")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Try again.")

def main():
    parlor = IceCreamParlor()
    parlor.run()

if __name__ == "__main__":
    main()