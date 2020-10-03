import positive_sum
import unittest
import numpy as np

def positive_sum_ans(array):
    array = np.array(array)
    return np.sum(array[array >= 0])

class ToMatrixTest(unittest.TestCase):
    def test_to_matrix_eq(self):      
        self.assertEqual(positive_sum.positive_sum([1,60,-100,500.5]), positive_sum_ans([1,60,-100,500.5]))
        self.assertEqual(positive_sum.positive_sum([0]),0)

if __name__ == "__main__": 
    unittest.main()
