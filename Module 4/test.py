import unittest
from CouponDealsCook import calculate_price

class TestSetOne(unittest.TestCase):
    def test_pass(self):
        pass
    def test_price_under_10_5_cash_10_discount(self):
        self.assertEquals(calculate_price(9, 5, 10), 18.65)

    def test_price_under_10_5_cash_15_discount(self):
        self.assertEquals(calculate_price(9, 5, 15), 18.65)

    def test_price_under_10_5_cash_20_discount(self):
        self.assertEquals(calculate_price(9, 5, 20), 18.65)

    def test_price_under_10_10_cash_10_discount(self):
            self.assertEquals(calculate_price(9, 5, 10), 18.65)

    def test_price_under_10_10_cash_15_discount(self):
            self.assertEquals(calculate_price(9, 5, 15), 18.65)

    def test_price_under_10_10_cash_20_discount(self):
            self.assertEquals(calculate_price(9, 5, 20), 18.65)

class TestSetTwo(unittest.TestCase):
    def test_pass(self):
        pass
    def test_price_under_30_5_cash_10_discount(self):
        self.assertEquals(calculate_price(11, 5, 10), 18.65)

    def test_price_under_30_5_cash_15_discount(self):
        self.assertEquals(calculate_price(11, 5, 15), 18.65)

    def test_price_under_30_5_cash_20_discount(self):
        self.assertEquals(calculate_price(11, 5, 20), 18.65)

    def test_price_under_30_10_cash_10_discount(self):
            self.assertEquals(calculate_price(11, 5, 10), 18.65)

    def test_price_under_30_10_cash_15_discount(self):
            self.assertEquals(calculate_price(11, 5, 15), 18.65)

    def test_price_under_30_10_cash_20_discount(self):
            self.assertEquals(calculate_price(11, 5, 20), 18.65)

if __name__ == '__main__':
    unittest.main()
