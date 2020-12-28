'''
* @Author: Uthsavi KP
* @Date: 2020-12-28 17:05:27
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-28 17:05:27
* @Title:To calculate euclidean distance of x and y co-ordinates.
'''


import math
class Distance:
    @staticmethod
    def euclidean_distance():
        try:
            x_point = int(input("Enter The Number For X-Point : ")) 
            y_point = int(input("Enter The Number For Y-Point : "))
            
            distance=math.sqrt((x_point*x_point) + (y_point*y_point)) #Formula To Calculate Euclidean Distance
            print("Euclidean Distance From The Points (x,y) Is :",distance)
        except Exception as err:
            print("** Error **", err) 
            print("Enter Only Numbers")
Distance.euclidean_distance()   