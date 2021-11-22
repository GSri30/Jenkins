#!/usr/bin/python3
# Test case for calculating mean of list of numbers
import unittest

from program import mean

class TestMean(unittest.TestCase):
    def test_list_int(self):
        """
        Test case for calculating mean of list of numbers
        """
        data1 = [1,2,3]
        result = mean(data1)
        self.assertEqual(result, 2)

        data1 = [0,0,0]
        result = mean(data1)
        self.assertEqual(result, 0)

        data1 = [4,5,6]
        result = mean(data1)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()