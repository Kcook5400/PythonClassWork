import unittest
from score_input import score_input


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(score_input("test", "test"), "test")

if __name__ == '__main__':
    unittest.main()
