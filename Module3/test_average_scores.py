import unittest

from average_scores import average

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(average(1,3,8),4)


if __name__ == '__main__':

    unittest.main()

