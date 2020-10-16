import unittest
from assign_average import switch_average


class MyTestCase(unittest.TestCase):
    def test_A(self):
        self.assertEqual(switch_average("A"), 1)
    def test_B(self):
        self.assertEqual(switch_average("B"), 2)
    def test_C(self):
        self.assertEqual(switch_average("C"), 3)
    def test_D(self):
        self.assertEqual(switch_average("D"), 4)
    def test_non_function(self):
        self.assertRaises(switch_average("E"),ValueError )


if __name__ == '__main__':
    unittest.main()
