# 59005
Application team project
# Shopping List Program in Python

This Python program allows you to manage a shopping list. You can add items with their name, price, quantity, and unit, remove items, view the list, calculate the total spending, and delete all items in the list.

## Features

- Add items with name, price, quantity, and unit
- Remove items by name
- Display all items and total spending
- Calculate total amount spent
- Delete all items from the list

## How to Use

1. Follow the on-screen instructions to manage your shopping list:
    - **add**: Add a new item to the list
    - **remove**: Remove an item by name
    - **show**: Display the current shopping list
    - **total**: Show the total amount spent
    - **delete all**: Remove all items from the list
    - **quit**: Exit the program

### Example Usage

- **Add an item**:
    ```sh
    Enter the item details (name, price, quantity, unit) separated by commas: Apple, 0.5, 2, kg
    ```

- **Remove an item**:
    ```sh
    Enter the item name to remove: Apple
    ```

- **Show the list**:
    ```sh
    - Apple: 2.0 kg at $0.50 each
    Total spent: $1.00
    ```

- **Delete all items**:
    ```sh
    All items have been deleted.
    ```

## Code Overview

### ShoppingList Class

- `__init__(self)`: Initializes an empty shopping list.
- `add_item(self, name, price, quantity, unit)`: Adds an item to the list.
- `remove_item(self, name)`: Removes an item by name.
- `delete_all(self)`: Deletes all items from the list.
- `get_total_spent(self)`: Calculates the total amount spent.
- `show_list(self)`: Displays all items and the total amount spent.

### Main Function

- Provides a user interface to interact with the shopping list.
- Options include adding, removing, showing the list, calculating the total, deleting all items, and quitting the program.
- Includes error handling for invalid input.
