import cnt_over_max
import unittest
import numpy as np

def cnt_over_max_ans(array):
    array = np.array(array)
    return len(array[np.abs(array) > np.max(array)])

class CntOvrMaxTest(unittest.TestCase):
    def test_cnt_over_max_eq(self):      
        self.assertEqual(cnt_over_max.cnt_over_max([1,1,0,0]), cnt_over_max_ans([1,1,0,0]))
        self.assertEqual(cnt_over_max.cnt_over_max([-2, 50, -101, 100, -102, -99 ]), cnt_over_max_ans([-2, 50, -101, 100, -102, -99 ]) )

if __name__ == "__main__": 
    unittest.main()
