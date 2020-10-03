import list_power
import unittest
import numpy as np

def list_power_ans(array, n):
    return np.power(array,n)

class ListPowerTest(unittest.TestCase):
    def test_list_power(self):
        self.assertEqual(list(list_power.list_power([1,1,0,0],5)),list(list_power_ans([1,1,0,0],5)))
        self.assertEqual(list(list_power.list_power([2,0,0,-2],1)),list(list_power_ans([2,0,0,-2],1)))

if __name__ == "__main__": 
    unittest.main()
