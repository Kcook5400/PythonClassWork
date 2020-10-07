import unittest
from unittest.mock import patch
from basic_list_exception import make_list


class MyTestCase(unittest.TestCase):
    @patch('basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()


if __name__ == '__main__':
    unittest.main()
