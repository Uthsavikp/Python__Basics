'''
* @Author: Uthsavi KP
* @Date: 2020-12-30 22:21:02  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-30 22:21:02
* @Title : To Get Day Of Week When Inputed Month,Day And Year.
'''
import day_of_week
import unittest

class DayOfWeek(unittest.TestCase):

    def test_month_day_year(self):

        self.assertEqual(day_of_week.month_day_year(12,29,2020),2)
        self.assertEqual(day_of_week.month_day_year(10,13,2020),0)
        self.assertEqual(day_of_week.month_day_year(3,16,2020),2)
        self.assertEqual(day_of_week.month_day_year(11,5,2008),5)
        self.assertEqual(day_of_week.month_day_year(8,29,2021),1)
        self.assertEqual(day_of_week.month_day_year(1,3,2020),3)
        self.assertEqual(day_of_week.month_day_year(2,20,2021),6)
        self.assertEqual(day_of_week.month_day_year(12,24,2020),4)


if __name__ == "__main__":
    unittest.main()