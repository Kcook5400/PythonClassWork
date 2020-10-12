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
from basic_list import make_list


class MyTestCase(unittest.TestCase):
    @patch('basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(make_list(), [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
