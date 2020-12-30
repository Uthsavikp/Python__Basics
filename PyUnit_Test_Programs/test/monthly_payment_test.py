'''
* @Author: Uthsavi KP
* @Date: 2020-12-30 17:02:18  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-30 17:02:18
* @Title : To Calculate Monthly Payment To Be Made
'''
import unittest   #importing unittest
import monthly_payment #importing the module

class MonthlyPayment(unittest.TestCase):

    def test_monthly_payment(self):
        self.assertEqual(monthly_payment.get_monthly_payment(96000,2,1), 4041.8)
        self.assertEqual(monthly_payment.get_monthly_payment(2000,1,2),168.48)
        self.assertNotEqual(monthly_payment.get_monthly_payment(9000,1.5,10),1996)

if __name__ == "__main__":
    unittest.main()