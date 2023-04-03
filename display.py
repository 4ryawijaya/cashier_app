from datetime import datetime
from function import ItemOperation, TransactionId

CURRENT_DATETIME = datetime.now().strftime("%Y-%m-%d")
ID_TRANSAKSI = TransactionId.transaction_id

class Display:
    def opening():
        print(f"""
            ================= WELCOME TO THE STORE =================
               Date: {CURRENT_DATETIME}                     
            ========================================================
            Dapatkan diskon untuk pembelian dengan nominal tertentu.
            Selamat berbelanja!
              """)
        
    def transaction_display():
        print(f"""
            ID Transaksi: {ID_TRANSAKSI} 
            """)
    
    def transaction_choice():
        print("""
              Untuk Melanjutkan Transaksi Silahkan Pilih menu berikut:
              1. Add Item               | 5. Delete Item
              2. Update Item Name       | 6. Reset Transaction
              3. Update Item Quantity   | 7. Check Order
              4. Update Item Price      | 8. Check Out
              """)
        
    def item_display():
        print(f"""
            ====================== ITEM LIST =======================                   
            ========================================================
            
            """)
        
    def checkout_display():
        pass
    
    def closing():
       print(f"""
            ------------ TERIMA KASIH ATAS KUNJUNGANNYA ------------
             """)
        


        