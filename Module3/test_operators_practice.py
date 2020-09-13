import unittest


class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        a = 5
        b = 5
        self.assertTrue(a == b)

    def test_not_equal(self):
        a = 5
        b = 4
        self.assertTrue(a != b)

    def test_greater_than(self):
        a = 6
        b = 5
        self.assertTrue(a > b)

    def test_less_than(self):
        a = 4
        b = 5
        self.assertTrue(a < b)

    def test_greater_than_or_equal_to(self):
        a = 6
        b = 5
        self.assertTrue(a >= b)

    def test_less_than_or_equal_to(self):
        a = 4
        b = 5
        self.assertTrue(a <= b)
    def test_equal2(self):
        a = 4
        b = 5
        self.assertTrue(a == b)

    def test_not_equal2(self):
        a = 4
        b = 4
        self.assertTrue(a != b)

    def test_greater_than2(self):
        a = 4
        b = 5
        self.assertTrue(a > b)

    def test_less_than2(self):
        a = 6
        b = 5
        self.assertTrue(a < b)

    def test_greater_than_or_equal_to2(self):
        a = 1
        b = 5
        self.assertTrue(a >= b)

    def test_less_than_or_equal_to2(self):
        a = 7
        b = 5
        self.assertTrue(a <= b)


if __name__ == '__main__':
    unittest.main()
