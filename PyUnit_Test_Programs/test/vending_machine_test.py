'''
* @Author: Uthsavi KP
* @Date: 2020-12-29 17:32:32  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-29 17:32:32
* @Title : Test Case for Vending Machine Problem
'''
import unittest
import vending_machine

class VendingMachine(unittest.TestCase):

    def test_currency_count(self):

        self.assertEqual(vending_machine.currency_count(212),("100 : 2,10 : 1,2 : 1,"))
        self.assertEqual(vending_machine.currency_count(5),("5 : 1,"))
        self.assertEqual(vending_machine.currency_count(88),("50 : 1,20 : 1,10 : 1,5 : 1,2 : 1,1 : 1,"))
if __name__ == "__main__":
    unittest.main()        