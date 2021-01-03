''' 
  @Author: Uthsavi KP
  @Date: 2021-01-03 16:07:42
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-03 16:07:42  
'''

import json

class Doctors:
    def __init__(self):
        pass
    def doctor_details(self):
        #reading the file
        doctor_file=open(r"C:\Users\uthsa\Python Files\OOPS_Programs\Clinique_Management_Program\doctors.json","r")
        doctor_data=doctor_file.read()
        doc=json.loads(doctor_data) #parse

    def search_by_name(self):
        pass
    def seach_by_id(self):
        pass
    def search_by_specialization(self):
        pass
    def search_by_availability(self):
        pass

if __name__ == "__main__":
    pass   