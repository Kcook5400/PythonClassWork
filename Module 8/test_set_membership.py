import unittest
from set_membership import set_membership

class MyTestCase(unittest.TestCase):
    def test_set_true(self):
        self.assertTrue(set_membership('a'), True)
    def test_set_false(self):
        self.assertFalse(set_membership('j'), False)


if __name__ == '__main__':
    unittest.main()
