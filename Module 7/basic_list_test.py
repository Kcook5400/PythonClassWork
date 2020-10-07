import unittest
from unittest.mock import patch
from basic_list import make_list, get_input


class MyTestCase(unittest.TestCase):
    @patch('basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(make_list(), [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
