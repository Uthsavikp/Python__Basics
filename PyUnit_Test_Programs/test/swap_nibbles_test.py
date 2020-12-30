'''
* @Author: Uthsavi KP
* @Date: 2020-12-31 03:45:00  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-31 03:45:00
* @Title : To Convert An Integer To Binary And Swap Nibbles
'''

import unittest
import swap_nibbles

class SwapNibbles(unittest.TestCase):
    
    def test_swap_nibbles(self):

        self.assertEqual(swap_nibbles.get_swap_nibbles(100),70)
        self.assertEqual(swap_nibbles.get_swap_nibbles(133),88)
        self.assertEqual(swap_nibbles.get_swap_nibbles(70),100)
        self.assertEqual(swap_nibbles.get_swap_nibbles(10),160)
 

if __name__ == "__main__":
    unittest.main()