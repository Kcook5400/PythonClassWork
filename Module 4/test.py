import unittest
from CouponDealsCook import calculate_price

class TestSetOne(unittest.TestCase):
    def test_pass(self):
        pass
    def test_price_under_10_5_cash_10_discount(self):
        self.assertEquals(calculate_price(9, 5, 10), 9.33)

    def test_price_under_10_5_cash_15_discount(self):
        self.assertEquals(calculate_price(9, 5, 15), 9.15)

    def test_price_under_10_5_cash_20_discount(self):
        self.assertEquals(calculate_price(9, 5, 20), 8.96)

    def test_price_under_10_10_cash_10_discount(self):
            self.assertEquals(calculate_price(9, 10, 10), 5.10)

    def test_price_under_10_10_cash_15_discount(self):
            self.assertEquals(calculate_price(9, 10, 15), 5.15)

    def test_price_under_10_10_cash_20_discount(self):
            self.assertEquals(calculate_price(9, 10, 20), 5.20)

class TestSetTwo(unittest.TestCase):
    def test_pass(self):
        pass
    def test_price_under_30_5_cash_10_discount(self):
        self.assertEquals(calculate_price(11, 5, 10), 13.03)

    def test_price_under_30_5_cash_15_discount(self):
        self.assertEquals(calculate_price(11, 5, 15), 12.74)

    def test_price_under_30_5_cash_20_discount(self):
        self.assertEquals(calculate_price(11, 5, 20), 12.46)

    def test_price_under_30_10_cash_10_discount(self):
            self.assertEquals(calculate_price(11, 10, 10), 8.80)

    def test_price_under_30_10_cash_15_discount(self):
            self.assertEquals(calculate_price(11, 10, 15), 8.75)

    def test_price_under_30_10_cash_20_discount(self):
            self.assertEquals(calculate_price(11, 10, 20), 8.70)

class TestSetThree(unittest.TestCase):
    def test_pass(self):
        pass
    def test_price_under_50_5_cash_10_discount(self):
        self.assertEquals(calculate_price(31, 5, 10), 33.95)

    def test_price_under_50_5_cash_15_discount(self):
        self.assertEquals(calculate_price(31, 5, 15), 32.72)

    def test_price_under_50_5_cash_20_discount(self):
        self.assertEquals(calculate_price(31, 5, 20), 31.50)

    def test_price_under_50_10_cash_10_discount(self):
            self.assertEquals(calculate_price(31, 10, 10), 29.72)

    def test_price_under_50_10_cash_15_discount(self):
            self.assertEquals(calculate_price(31, 10, 15), 28.73)

    def test_price_under_10_10_cash_20_discount(self):
            self.assertEquals(calculate_price(31, 10, 20), 27.74)

class TestSetFour(unittest.TestCase):
    def test_pass(self):
        pass
    def test_price_over_50_5_cash_10_discount(self):
        self.assertEquals(calculate_price(51, 5, 10), 38.92)

    def test_price_over_50_5_cash_15_discount(self):
        self.assertEquals(calculate_price(51, 5, 15), 36.75)

    def test_price_over_505_cash_20_discount(self):
        self.assertEquals(calculate_price(51, 5, 20), 34.59)

    def test_price_over_50_10_cash_10_discount(self):
            self.assertEquals(calculate_price(51, 10, 10), 34.69)

    def test_price_over_50_10_cash_15_discount(self):
            self.assertEquals(calculate_price(51, 10, 15), 32.76)

    def test_price_over_50_10_cash_20_discount(self):
            self.assertEquals(calculate_price(51, 10, 20), 30.83)

if __name__ == '__main__':
    unittest.main()
