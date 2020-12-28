'''
* @Author: Uthsavi KP
* @Date: 2020-12-28 18:26:15
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-28 18:26:15
* @Title:To calculate euclidean distance of x and y co-ordinates.
'''


import math
class Distance:
    @staticmethod
    def euclidean_distance():
        try:
            x_point = int(input("Enter The Number For X-Point : ")) 
            y_point = int(input("Enter The Number For Y-Point : "))
            
            distance_formula=math.sqrt(math.pow(x_point,2) + math.pow(y_point,2))#Formula To Calculate Euclidean Distance
            print("Euclidean Distance From The Points (x,y) Is :",distance_formula)
        except Exception as err:
            print("** Error **", err) 
            print("Enter Only Numbers")
Distance.euclidean_distance()   