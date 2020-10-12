"""
PEP: 8
Title: search_list_test
Author: Kevin Cook
Status: Active
Type: Process
Created: 12-October-2020
Post: 12-October-2020
History:
"""
import unittest
from search_and_sort_array import *


class MyTestCase(unittest.TestCase):
    def test_found(self):
        self.assertEqual(search_list(1), 0)
    def test_not_found(self):
        self.assertEqual(search_list("Z"), -1)
    def test_sort(self):
        self.assertEqual(sort_list(), [8,7,6,5,4,3,1])

if __name__ == '__main__':
    unittest.main()
