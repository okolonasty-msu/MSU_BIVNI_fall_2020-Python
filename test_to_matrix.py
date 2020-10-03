import to_matrix
import unittest
import numpy as np


class ToMatrixTest(unittest.TestCase):
    def test_to_matrix_false(self):
        self.assertFalse(to_matrix.to_matrix([1,1,0]))
        self.assertFalse(to_matrix.to_matrix(99*[0]))
    def test_to_matrix_eq(self):      
        self.assertEqual(to_matrix.to_matrix([1,1,0,0]).shape,(2,2))
        self.assertEqual(to_matrix.to_matrix([2]).shape,(1,1))

if __name__ == "__main__": 
    unittest.main()
