'''
* @Author: Uthsavi KP
* @Date: 2020-12-28 14:29:38
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-28 14:29:38
* @Title:Function to print 2 Dimensional Array.
'''

def two_dimentional_array():
    try:
        rows = int(input("Enter The Number Of Rows:")) 
        columns = int(input("Enter The Number Of Columns:"))
    
        array_one = [] 
        print("Enter The Numbers:") 
  
        for number in range(rows):          
            array_two =[]   
            for element in range(columns):       
                array_two.append(int(input())) 
            array_one.append(array_two) #adding the elements

        # Printing the array elements
        print("The Array Elements Are:")
    
        for number in range(rows): 
            for element in range(columns): 
                print(array_one[number][element], end = " ")
            print("\n")
    except Exception as err:
        print("Enter Only Numbers:",err)         
    
two_dimentional_array() #function call