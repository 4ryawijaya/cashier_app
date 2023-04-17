class ItemManager:
    def __init__(self):
        self.items = {}

    def addItem(self, item_name, item_price, item_quantity):
        # Save inputs in a dictionary
        item = {
            'name': item_name,
            'price': item_price,
            'quantity': item_quantity
        }
        self.items.append(item)
    
    def editItemName(self, index, new_name):
        # Edit item name based on index
        if index < len(self.items):
            self.items[index]['name'] = new_name
            print(f"Item name at index {index} updated to '{new_name}'")
            print()
        else:
            print("Invalid index. No item found.")
            print()
            
    def editItemQuantity(self, index, new_quantity):
        # Edit item quantity based on index
        if index < len(self.items):
            self.items[index]['quantity'] = new_quantity
            print(f"Item quantity at index {index} updated to {new_quantity}")
            print()
        else:
            print("Invalid index. No item found.")
            print()

    def editItemPrice(self, index, new_price):
        # Edit item price based on index
        if index < len(self.items):
            self.items[index]['price'] = new_price
            print(f"Item price at index {index} updated to {new_price}")
            print()
        else:
            print("Invalid index. No item found.")
            print()

    def displayLastInput(self):
        # Display last input
        if self.items:
            item = self.items[-1]
            print("Last input:")
            print("Item name:", item['name'])
            print("Item price:", item['price'])
            print("Item quantity:", item['quantity'])
            print()
        else:
            print("No inputs yet.")
            print()

    def displayAllInputs(self):
        # Display all inputs
        print("All inputs:")
        for i, item in enumerate(self.items):
            print("Input", i+1)
            print("Item name:", item['name'])
            print("Item price:", item['price'])
            print("Item quantity:", item['quantity'])
            print()

    def getTotalPrice(self):
        # Calculate total price of all items
        total_price = 0
        for item in self.items:
            total_price += item['price'] * item['quantity']
        return total_price

    def checkout(self):
        # Display all input items and their total price
        print("Checkout:")
        for i, item in enumerate(self.items):
            print("Item", i+1)
            print("Item name:", item['name'])
            print("Item price:", item['price'])
            print("Item quantity:", item['quantity'])
            print()
        total_price = self.getTotalPrice()
        print("Total price:", total_price)

    def resetInputs(self):
        # Reset all inputs
        self.items = {}

    