'''
* @Author: Uthsavi KP
* @Date: 2020-12-30 11:58:19  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-30 11:58:19
* @Title : To Convert Temperature From Fahrenheit To Celsius Or Viceversa.
'''
import unittest
from PyUnit_Test_Programs.main import temperature_conversion

class TemperatureConversion(unittest.TestCase):

    def test_temperature_conversion(self):

        self.assertEqual(temperature_conversion.get_temperature_conversion('45F',45,'F'),7)
        self.assertEqual(temperature_conversion.get_temperature_conversion('320f',320,'f'),160)
        self.assertEqual(temperature_conversion.get_temperature_conversion('99c',99,'c'),210)
        self.assertEqual(temperature_conversion.get_temperature_conversion('0C',0,'C'),32)
       

if __name__ == "__main__":
    unittest.main()
