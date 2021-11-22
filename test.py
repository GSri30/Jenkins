#!/usr/bin/python3
# Test case for calculating mean of list of numbers
import unittest

from program import mean

class TestMean(unittest.TestCase):
    def test_list_mean(self):
        """
        Test case for calculating mean of list of numbers
        """
        data1 = [1,2,3]
        result1 = mean(data1)
        self.assertEqual(result1, 2)

        data2 = [0,0,0]
        result2 = mean(data2)
        self.assertEqual(result2, 0)

        data3 = [4,5,6]
        result3 = mean(data3)
        self.assertEqual(result3, 5)

        data4 = []
        result4 = mean(data4)
        self.assertEqual(result4, 0)

if __name__ == '__main__':
    unittest.main()