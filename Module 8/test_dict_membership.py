import unittest
from dict_membership import dict_membership


class MyTestCase(unittest.TestCase):
    def test_set_true(self):
        self.assertTrue(dict_membership('AB'), True)
    def test_set_false(self):
        self.assertFalse(dict_membership(''), False)


if __name__ == '__main__':
    unittest.main()
