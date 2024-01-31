import json
from pymongo import MongoClient
import threading


uri = "mongodb://localhost:27017"
client = MongoClient(uri)


def load_json(file_name):
    try:
        with open(f'{file_name}.json') as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        print("no such file or directory")

def process_menus(d):
      for d in stores:
            for menus in d.get('menus', []):
                for category in menus.get('categories', []):
                    for product in category.get('menu_item_list', []):
                        with open(f"{product['product_id'][:40]}.json", 'w') as pd_write:
                            json.dump(product, pd_write, indent=2)

                    category.pop('menu_item_list')



try:
    client.admin.command('ping')
    # print("Pinged your deployment. You successfully connected to MongoDB!")

    db = client['anish']
    collection = db['sample']

    search = input("If you wanna search product then type yes otherwise no:  ")
    if search == "yes":
        while search == "yes":
            product_id = input("Give me your product ID :->  ")

            get_product_id = product_id[:40]
            # print(get_product_id)

        
            try:
                with open(f'{get_product_id}.json', 'r') as pd_read:
                    json_data = json.load(pd_read)
                    print(json_data)
            except Exception as e:
                print("Not Found")
        
            search = input("If you wanna search product then type yes otherwise no:  ")
            

            

        
    if search == "no":
        print("------------------\n")
        pass

    
    wanna_load = input("Do you wanna load json(yes/no)? ")

    if wanna_load == "yes":

        
        load_data = input('Please Give the name of json file which you wanna upload?') 
        data = load_json(load_data)
            
        
        stores = data['stores']

        menu_thread = threading.Thread(target=process_menus, args=(stores,))
        menu_thread.start()
        menu_thread.join()

        ### we can perform other task while thread is running
        print("thread is running")

        try:
            abc = collection.insert_many(stores)
        except Exception as e:
            print("Already feeded")
    
    else:
        print("Not Load Json")
  


except Exception as e:
    print(e)


client.close()






