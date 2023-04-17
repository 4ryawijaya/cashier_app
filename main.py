from function import ItemManager
from display import Display
import time

def run():
        # Main loop to receive input and operate methods until checkout
        while True:
            Display.opening()
            time.sleep(5)
            
            print("Choose an option:")
            print("1. Add item")
            print("2. Display last input")
            print("3. Display all inputs")
            print("4. Checkout")
            print("5. Reset inputs")
            print("6. Edit Item Name")
            print("7. Edit Item Quantity")
            print("8. Edit Item Price")
            print("9. Exit Transaction")
            choice = input("Enter your choice: ")

            if choice == '1':
                item_name = input("Enter item name: ")
                item_price = float(input("Enter item price: "))
                item_quantity = int(input("Enter item quantity: "))
                ItemManager.addItem(item_name, item_price, item_quantity)
                print("Item added.")
                print()

            elif choice == '2':
                Display.item_display()
                ItemManager.displayLastInput()

            elif choice == '3':
                Display.item_display()
                ItemManager.displayAllInputs()

            elif choice == '4':
                ItemManager.checkout()
                break  # Exit loop after checkout

            elif choice == '5':
                ItemManager.resetInputs()
                print("Inputs reset.")
                print()

            elif choice == '6':
                index = int(input("Enter item index to edit: "))
                new_name = input("Enter new item name: ")
                ItemManager.editItemName(index, new_name)
            
            elif choice == '7':
                index = int(input("Enter item index to edit: "))
                new_quantity = int(input("Enter new item quantity: "))
                ItemManager.editItemQuantity(index, new_quantity)

            elif choice == '8':
                index = int(input("Enter item index to edit: "))
                new_price = float(input("Enter new item price: "))
                ItemManager.editItemPrice(index, new_price)

            elif choice == '9':
                Display.closing()
                break  # Exit loop and end script

            else:
                print("Invalid choice. Try again.")
                print()

run()