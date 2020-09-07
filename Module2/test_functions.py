import unittest
from camper_age_input import convert_to_months


class FunctionTestCase(unittest.TestCase):
    def test_month(self):
        self.assertEqual(convert_to_months(6), 72)


if __name__ == '__main__':
    unittest.main()