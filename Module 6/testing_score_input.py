import unittest
from score_input import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertTrue(score_input("test"))

if __name__ == '__main__':
    unittest.main()
