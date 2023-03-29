#Fungsi input transaction_id
#fungsi input item
#fungsi input quantity
#fungsi input price
from function import Operation
from display import Display

while True:
    Display.opening()
    item_name = input('Enter item name (or enter "done" to finish): ')
    if item_name == 'done':
        Display.closing()
        break

# idVAR = f"Your transaction id is {random_digits(5)}"
# itemVAR = input("Please input your item:")
# qtyVAR = input("Please item quantity : ")

# test1 = Operation(idVAR, itemVAR, qtyVAR)

