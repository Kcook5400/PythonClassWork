import unittest
from function_parameter_cook import multiply_string

class MyTestCase(unittest.TestCase):
    def test_multiplyString(self):
        self.assertEqual(multiply_string("LOL", 2),'LOL', 'LOL')


if __name__ == '__main__':
    unittest.main()
