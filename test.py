# class Client:
#     def __init__(self, name):
#         self.name = name
        
#     def add_name(self):
#         self.name = input("What is band's name")
#         return self.name
        
#     def print_info(self):
#         print(f"{self.name}")
        
# client = Client.add_name()
# client.print_info()

client_info = {} # start empty

while True:
    new_client = {}
    name = input("what is the band's name? ")
    new_client['name'] = name
    new_client_id = len(client_info) # starts at zero, add 1 if you want the IDs to start at 1
    client_info[new_client_id] = new_client

    print("client added, client_info is now", client_info)


    

        
    
