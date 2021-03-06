"""
PEP: 8
Title: test_dict_membership
Author: Kevin Cook
Status: Active
Type: Process
Created: 12-October-2020
Post: 12-October-2020
History:
"""
import unittest
from dict_membership import dict_membership


class MyTestCase(unittest.TestCase):
    def test_set_true(self):
        self.assertTrue(dict_membership(1), True)
    def test_set_false(self):
        self.assertFalse(dict_membership('AB'), False)


if __name__ == '__main__':
    unittest.main()
