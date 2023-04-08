client_info = {} # start empty

while True:
    new_client = {}
    name = input("what is the band's name? ")
    new_client['name'] = name
    new_client_id = len(client_info) # starts at zero, add 1 if you want the IDs to start at 1
    client_info[new_client_id] = new_client

    print("client added, client_info is now", client_info)