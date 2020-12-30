'''
* @Author: Uthsavi KP
* @Date: 2020-12-30 1:16:53  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-30 1:16:53
* @Title : To Get Square Root Of A Number Using Newton"s Method
'''

def square_root(number):
    
    root=number 
    epsilon = 1e-15
    while abs(root - number/root) > epsilon*root: #finding square root of a number 
        root = round((number/root + root)/2,2)
        print(root)
    return root

if __name__ == "__main__":
    number = int(input("Enter A number You Want The Square Root Of: "))
    root=number 
    square_root(number)