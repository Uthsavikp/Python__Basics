'''
* @Author: Uthsavi KP
* @Date: 2021-01-02 4:44:23  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2021-01-02 4:44:23
'''

import json

class Inventory:

    def __init__(self):
        pass

    def invertory_details(self):
        try:
            with open(r"C:\Users\uthsa\Python Files\OOPS_Programs\Inventory_Management\inventory.json", "r") as file:    #reading the json file
                data = json.load(file)
        except Exception as err:
            print("Unable To Open The File:",err)


        rice_list=data['rice']
        for val1 in range(len(rice_list)):
            rice = rice_list[val1].get("weight") * rice_list[val1].get("price_per_kg")

        pulses_list=data['pulses']        
        for val2 in range(len(pulses_list)):
            pulses = pulses_list[val2].get("weight") * pulses_list[val2].get("price_per_kg")

        wheat_list=data['wheat']
        for val3 in range(len(wheat_list)):
            wheat = wheat_list[val3].get("weight") * wheat_list[val3].get("price_per_kg")

        print("Total value of rice is:", rice)
        print("Total value of pulse is:", pulses)
        print("Total value of wheat is:", wheat)    

        try:
            with open(r"C:\Users\uthsa\Python Files\OOPS_Programs\Inventory_Management\updated_inventory.json", "w") as write_file:
                json.dump(data, write_file,indent=4)
        except Exception as err:
            print("Unable To Write The File:", err)

if __name__ == "__main__": 
    inventory = Inventory()           
    inventory.invertory_details()            