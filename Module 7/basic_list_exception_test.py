"""
PEP: 8
Title: basic_list
Author: Kevin Cook
Status: Active
Type: Process
Created: 12-October-2020
Post: 12-October-2020
History:
"""
import unittest
from unittest.mock import patch
from basic_list_exception import make_list


class MyTestCase(unittest.TestCase):
    @patch('basic_list_exception.get_input', return_value=51)
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            make_list()


if __name__ == '__main__':
    unittest.main()
