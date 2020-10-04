import unittest
from score_input import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEquals(score_input(test_name="Enter your test name"),"test")

if __name__ == '__main__':
    score_input("Enter your test name",1)
