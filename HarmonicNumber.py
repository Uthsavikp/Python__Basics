'''
* @Author: Uthsavi KP
* @Date: 2020-12-26 21:08:22
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-26 21:08:22
'''

try:
    number = int(input("Enter A Number: "))
    assert number!=0
except:
    print("Number Is Zero")
else:    
    harmonic=0
    for i in range(1,number+1):
        harmonic=harmonic+1/i
        print(harmonic)