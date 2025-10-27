import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):  #fixed mutable default logs=[] to None to avoid shared mutable state bw fn calls
    """Add an item and its quantity to the inventory."""
    if logs is None:  
        logs = []

    # Added input validation for item and qty
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input: item must be a string and qty must be an integer.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")  #Changed to f-string (readability)

def remove_item(item, qty):
    """Remove a quantity of an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:  #Changed bare except to specific KeyError
        print(f"Item '{item}' not found in inventory.")

def get_qty(item):
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        # Added with-statement and encoding for safe file handling
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"File {file} not found. Starting with empty inventory.")
        stock_data = {}

def save_data(file="inventory.json"):
    """Save inventory data to a JSON file."""
    # Added with-statement and encoding for writing
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)

def print_data():
    """Print all inventory items and their quantities."""
    print("Items Report:")
    for i, qty in stock_data.items():
        print(f"{i} -> {qty}")

def check_low_items(threshold=5):
    """Return a list of items below the given threshold."""
    return [i for i, qty in stock_data.items() if qty < threshold]

def main():
    """Main execution block."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, now handled safely
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()
    # Removed "dangerous" eval() call bcz it could execute arbitrary code

if __name__ == "__main__":
    main()