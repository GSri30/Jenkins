#!/usr/bin/python3
# Test case for calculating mean of list of numbers

import unittest
from program import mean

class TestMean(unittest.TestCase):
    def test_list_mean1(self):
        """
        Test case 1 for calculating mean of list of numbers
        """
        data1 = [1,2,3]
        result1 = mean(data1)
        self.assertEqual(result1, 2)

    def test_list_mean2(self):
        """
        Test case 2 for calculating mean of list of numbers
        """
        data2 = [0,0,0]
        result2 = mean(data2)
        self.assertEqual(result2, 0)

    def test_list_mean3(self):
        """
        Test case 3 for calculating mean of list of numbers
        """
        data3 = [4,5,6]
        result3 = mean(data3)
        self.assertEqual(result3, 15)
    
    def test_list_mean4(self):
        """
        Test case 4 for calculating mean of list of numbers
        """
        data4 = []
        result4 = mean(data4)
        self.assertEqual(result4, 0)

if __name__ == '__main__':
    unittest.main()
