from datetime import datetime
from function import ItemOperation

CURRENT_DATETIME = datetime.now().strftime("%Y-%m-%d")

class Display:
    def opening():
        print(f"""
            ================= WELCOME TO THE STORE =================
               Date: {CURRENT_DATETIME}                     
            ========================================================
            Dapatkan diskon untuk pembelian dengan nominal tertentu.
            Selamat berbelanja!
              """)
    
    def transaction_choice():
        print("""
              Untuk Melanjutkan Transaksi Silahkan Pilih menu berikut:
              1. Add Item               | 5. Delete Item
              2. Update Item Name       | 6. Reset Transaction
              3. Update Item Quantity   | 7. Check Order
              4. Update Item Price      | 8. Check Out
              """)
        
        def operasi(): 
            pilih = input(int("Pilih nomor: "))
            if pilih == 1:
                print("Silahkan menambahkan item anda: ")
                ItemOperation.add_item()
            elif pilih == 2:
                print("Silahkan ubah nama item anda.")
            elif pilih == 3:
                print("Silahkan ubah kuantitas item anda.")
            elif pilih == 6:
                print("Berikut daftar belanja anda")
                ItemOperation.check_order()
            elif pilih == 8:
                pass
            else:
                print("Pilihan anda di luar jangkauan")

            
            operasi()
            
        
        
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
        


        