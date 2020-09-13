import unittest
from average_scores import average

class MyTestCase(unittest.TestCase):
    def test_something(self):
        assert average_scores.average() == 3


if __name__ == '__main__':

    unittest.main()

