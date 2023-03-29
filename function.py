import pandas as pd

class Operation:
    def __init__(self) -> None:
        self.transaction_id = None
        self.df = pd.DataFrame(columns=['item_name', 'quantity', 'price', 'total'])
    
    def transaction(self, transaction_id):
        self.transaction_id = transaction_id
        
    def add_item(self, item_name, quantity, price):
        self.df = self.df.append({'item_name': item_name, 'quantity': quantity, 'price': price})
        
    def check_order(self):
        print("Silahkan periksa daftar belanja anda.")
        print(self.df)
        
    def update_item_name(self, index, new_item_name):
        self.df.at[index, 'item_name'] = new_item_name
        
    def update_item_quantity(self, index, new_quantity):
        self.df.at[index, 'quantity'] = new_quantity
        
    def update_item_price(self, index, new_price):
        self.df.at[index, 'price'] = new_price
        
    def delete_item(self, index):
        self.df = self.df.drop(index)
        
    def reset_transaction(self):
        self.transaction_id = None
        self.df = pd.DateFrame(columns=['item_name', 'quantity', 'price'])
    
    

        
    
    