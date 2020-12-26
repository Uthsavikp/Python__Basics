'''
* @Author: Uthsavi KP
* @Date: 2020-12-26 20:33:08  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-26 20:33:08
'''

try:
    power = int(input("Enter A power:"))
    if power >31:
        raise ValueError("Entered A Number Greater Than 31")
    number = 1
    for i in range(power):
        number = number *2
        print(number)    
except Exception as err: # err is just a variable name
    print("Root cause of exception is::",err)    