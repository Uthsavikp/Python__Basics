'''
* @Author: Uthsavi KP
* @Date: 2020-12-29 17:32:32  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-29 17:32:32
* @Title : To Convert Decimal To Binary
'''

import unittest
import decimal_to_binary 

class Binary(unittest.TestCase):
        
    def test_newton_square_root(self):
        self.assertEqual(decimal_to_binary.binary(100),1100100)
        self.assertEqual(decimal_to_binary.binary(24),11000)
        self.assertEqual(decimal_to_binary.binary(130),10000010)

if __name__ == "__main__":
    unittest.main()