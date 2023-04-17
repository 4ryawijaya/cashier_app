def run(self):
        # Main loop to receive input and operate methods until checkout
        while True:
            print("Choose an option:")
            print("1. Add item")
            print("2. Display last input")
            print("3. Display all inputs")
            print("4. Checkout")
            print("5. Reset inputs")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                item_name = input("Enter item name: ")
                item_price = float(input("Enter item price: "))
                item_quantity = int(input("Enter item quantity: "))
                self.addItem(item_name, item_price, item_quantity)
                print("Item added.")
                print()

            elif choice == '2':
                self.displayLastInput()

            elif choice == '3':
                self.displayAllInputs()

            elif choice == '4':
                self.checkout()
                break  # Exit loop after checkout

            elif choice == '5':
                self.resetInputs()
                print("Inputs reset.")
                print()

            elif choice == '6':
                index = int(input("Enter item index to edit: "))
                new_name = input("Enter new item name: ")
                self.editItemName(index, new_name)
            
            elif choice == '7':
                index = int(input("Enter item index to edit: "))
                new_quantity = int(input("Enter new item quantity: "))
                self.editItemQuantity(index, new_quantity)

            elif choice == '8':
                index = int(input("Enter item index to edit: "))
                new_price = float(input("Enter new item price: "))
                self.editItemPrice(index, new_price)

            elif choice == '9':
                print("Goodbye!")
                break  # Exit loop and end script

            else:
                print("Invalid choice. Try again.")
                print()
