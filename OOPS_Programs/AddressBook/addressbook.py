'''
* @Author: Uthsavi KP
* @Date: 2021-01-02 4:44:23  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2021-01-02 4:44:23
'''
import os
 
class AddressBook:
    def __init__(self, first_name, last_name, address, city, state, zip, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
 
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
 
    def __str__(self):     #converting to string
         return f"{self.first_name} {self.last_name} : {self.address} : {self.city} : {self.state} : {self.zip} :{self.phone_number}"
 
addressbook = list()
 
if os.path.isfile("addressbook.csv"):
    with open("addressbook.csv") as file:
        csv_list = file.readlines()
        for contact_line in csv_list:
            contact_data = contact_line.rstrip().split(",")
            contact = AddressBook(contact_data[0],
                             contact_data[1], 
                             contact_data[2],
                             contact_data[3],
                             contact_data[4],
                             contact_data[5],
                             contact_data[5])
            addressbook.append(contact)
        
user_input = ""
 
 
print("Welcome to the address book program")
 
while user_input != "e":
    print("Please select the below options")
    print("1 - Add a person to the addressbook")
    print("2 - Display all contacts")
    print("3 - Find a contact")
    print("e - Exit the  program")
    user_input = input("Select option: ")
    
    if user_input == "1":
        print("Enter the below information")
 
        first_name = input("First name = ")
        last_name = input("Last name = ")
        address = input("address = ")
        city = input("city = ")
        state = input("state = ")
        zip = input("zip = ")
        phone_number = input("Phone number = ")
 
        our_contact = AddressBook(first_name, last_name, address, city, state,zip, phone_number)
        addressbook.append(our_contact)
        print("Information added successfully")
    elif user_input == "2":
        for contact in addressbook:
            print(contact)
        input("All contacts displayed. Hit enter to continue.")
    elif user_input == "3":
        to_lookup = input("Enter contact's name to lookup\n")
        for contact in addressbook:
            if to_lookup in contact.full_name():
                print(contact)
            else:
                print("person does not exist")    
    elif user_input.lower() == "q":
        break
 
with open("addressbook.csv", "w") as file:
    for contact in addressbook:
        file.write(f"{contact.first_name},{contact.last_name},{contact.address},{contact.city},{contact.state},{contact.zip}{contact.phone_number}\n")
 
print("Thank you for using the address book")

if __name__ == "__main__":
    AddressBook