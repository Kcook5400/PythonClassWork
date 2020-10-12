import unittest


class MyTestCase(unittest.TestCase):
    def test_set_true(self):
        self.assertTrue(set_membership(), True)
    def test_set_false(self):
        self.assertFalse(set_membership(), False)


if __name__ == '__main__':
    unittest.main()
