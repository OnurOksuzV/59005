class ShoppingList:
    def __init__(self):
        # Initializes an empty shopping list
        self.items = []

    def add_item(self, name, price, quantity, unit):
        # Adds an item to the shopping list
        self.items.append({"name": name, "price": price, "quantity": quantity, "unit": unit})
        print(f'Added {name} - {quantity} {unit} at ${price:.2f} each')

    def remove_item(self, name):
        # Removes an item by name from the shopping list
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                print(f'Removed {name}')
                return
        print(f'Item {name} not found')

    def delete_all(self):
        # Deletes all items from the shopping list
        self.items.clear()
        print("All items have been deleted.")

    def get_total_spent(self):
        # Calculates the total amount spent
        total = sum(item["price"] * item["quantity"] for item in self.items)
        return total

    def show_list(self):
        # Displays the shopping list and total spent
        if not self.items:
            print("The shopping list is empty.")
        else:
            print("Shopping List:")
            for item in self.items:
                print(f' - {item["name"]}: {item["quantity"]} {item["unit"]} at ${item["price"]:.2f} each')
            print(f'Total spent: ${self.get_total_spent():.2f}')


def main():
    shopping_list = ShoppingList()
    while True:
        # Main user interaction loop
        print("\nOptions: add, remove, show, total, delete all, quit")
        choice = input("What would you like to do? ").strip().lower()

        if choice == "add":
            while True:
                # Prompts user to add item details
                user_input = input("Enter the item details (name, price, quantity, unit) separated by commas: ").strip()
                try:
                    # Processes and adds the item
                    name, price, quantity, unit = [x.strip() for x in user_input.split(',')]
                    price = float(price)
                    quantity = float(quantity)
                    shopping_list.add_item(name, price, quantity, unit)
                    break
                except ValueError:
                    # Handles invalid input
                    print("Invalid input format. Please try again.")
                except Exception as e:
                    # Handles unexpected errors
                    print(f"An error occurred: {e}. Please try again.")

        elif choice == "remove":
            while True:
                # Prompts user to remove an item by name
                name = input("Enter the item name to remove: ").strip()
                if any(item["name"] == name for item in shopping_list.items):
                    shopping_list.remove_item(name)
                    break
                else:
                    # Handles item not found
                    print(f'Item {name} not found. Please try again.')

        elif choice == "show":
            # Shows the current shopping list
            shopping_list.show_list()
        elif choice == "total":
            # Displays the total amount spent
            total = shopping_list.get_total_spent()
            print(f'Total spent: ${total:.2f}')
        elif choice == "delete all":
            # Deletes all items from the shopping list
            shopping_list.delete_all()
        elif choice == "quit":
            # Exits the program
            print("Exiting the program. Goodbye!")
            break
        else:
            # Handles invalid menu options
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()