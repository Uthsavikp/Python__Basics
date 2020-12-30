'''
* @Author: Uthsavi KP
* @Date: 2020-12-31 03:25:12  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-31 03:25:12
* @Title : To Convert An Integer To Binary And Swap Nibbles
'''

def integer_to_binary(number): 
    if number > 1: 
        integer_to_binary(number // 2)  #floor division 
    print(number % 2, end = '')

    return (get_swap_nibbles(number))

def get_swap_nibbles(number):
    return ((number & 0x0F)<<4 | (number & 0xF0)>>4)


if __name__ == '__main__': 
      
    integer_number = int(input("Enter A Number:"))       
    integer_to_binary(integer_number) # Calling function
    print(": Is The Binary Number")
    print(get_swap_nibbles(integer_number),": Swap Nibbles") 