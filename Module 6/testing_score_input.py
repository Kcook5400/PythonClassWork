import unittest
from score_input import score_input


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(score_input("test", 80), ("test", "80"))

if __name__ == '__main__':
    unittest.main()
