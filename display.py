from datetime import datetime

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
           
        
    def item_display():
        print(f"""
            ====================== ITEM LIST =======================                   
            ========================================================
            
            """)

    
    def closing():
       print(f"""
            ------------ TERIMA KASIH ATAS KUNJUNGANNYA ------------
             """)
        


        