''''
* @Author: Uthsavi KP
* @Date: 2020-12-31 2:13:38  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-31 2:13:38
* @Title : To Convert Decimal To Binary
'''

def binary(num): 
    if num > 1: 
        binary(num // 2)  #floor division 
    print(num % 2, end = '') #getting the reminder
    return num
  
if __name__ == '__main__': 
      
    decimal_number = int(input("Enter A Number:"))    
     
    binary(decimal_number) # Calling function
    print(" : Is The Binary Number")