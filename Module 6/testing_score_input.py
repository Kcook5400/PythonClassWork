import unittest
from score_input import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        with self.assertRaises(ValueError):
            score_input("test")

    def test_score_input_test_score_valid(self):
        self.assertEqual(score_input("test", 80), ("test", 80))

    def test_score_input_test_score_below_range(self):
        with self.assertRaises(ValueError):
            score_input("test", test_score=-1)

    def test_score_input_test_score_above_range(self):
        with self.assertRaises(ValueError):
            score_input("test", test_score=101)

    def test_score_input_test_non_numeric(self):
        with self.assertRaises(ValueError):
            score_input("test", test_score="*")

if __name__ == '__main__':
    unittest
