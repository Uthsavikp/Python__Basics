'''
* @Author: Uthsavi KP
* @Date: 2020-12-29 17:32:32  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-29 17:32:32
* @Title : To Convert Temperature From Fahrenheit To Celsius Or Viceversa.
'''

def temperature_convertion():
    #To convert temperature from  °C to °F
    if scale.upper() == "C":
        temperature_convertor = int(round((9 * degree) / 5 + 32)) #Formula to convert temperature from  °C to °F
        temperature_scale = "Fahrenheit"

    #To convert temperature from  °F to °C
    elif scale.upper() == "F":
        temperature_convertor = int(round((degree - 32) * 5 / 9))  #Formula to convert temperature from  °F to °C 
        temperature_scale = "Celsius"
    else:
        print("Invalid Input")
        quit()
    print("The Temperature In", temperature_scale, "Is", temperature_convertor, "degrees.")
    return temperature_convertor

if __name__ == "__main__":
     #calling the function
    temperature = input("Enter The Temperature You Want To Convert (e.g - 45°F, 102°C) : ")
    degree = int(temperature[:-1]) #excludes the index i.e C or F and gets only integer
    scale = temperature[-1] #gets only the last index i.e C or F
    temperature_convertion()
