'''
* @Author: Uthsavi KP
* @Date: 2020-12-31 2:49:51  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-31 2:49:51
* @Title : To Find The Square Root Of A Number
'''
import unittest
import newton_square_root 

class SquareRoot(unittest.TestCase):
        
    def test_newton_square_root(self):
        self.assertEqual(newton_square_root.square_root(144),12)
        self.assertEqual(newton_square_root.square_root(64),8)
        self.assertEqual(newton_square_root.square_root(10000),100)
        self.assertEqual(newton_square_root.square_root(9),3)

if __name__ == "__main__":
    unittest.main()


