import list_avg
import unittest

class ListAvgTest(unittest.TestCase):
    def test_list_avg(self):
        self.assertEqual(list_avg.list_avg([1,1,0,0]),0.5)
        self.assertEqual(list_avg.list_avg([2,0,0,-2]),0)
        self.assertEqual(list_avg.list_avg([100,1000,0.7,-32]),267.175)
        self.assertEqual(list_avg.list_avg([5]),5)

        
if __name__ == "__main__": 
    unittest.main() 
