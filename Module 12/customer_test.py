import unittest

from customer import Customer

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Cust1 = Customer("Smith", "John", "555-123-5555", 1200)
    def tearDown(self):
        del self.Cust1
    def test_cust_id(self):
        self.assertEqual(self.Cust1.customer_id, 1200)
    def test_last_name(self):
        self.assertEqual(self.Cust1.last_name, "Smith")
    def test_first_name(self):
        self.assertEqual(self.Cust1.first_name, "John")
    def test_phone_number(self):
        self.assertEqual(self.Cust1.phone_number, "555-123-5555")
    def test_bad_cust_id(self):
        with self.assertRaises(Exception):
            self.Cust1 = Customer("Smith", "John", "555-123-5555", 12)
    def test_bad_last_name(self):
        with self.assertRaises(Exception):
            self.Cust1 = Customer("Sm99ith", "John", "555-123-5555", 1200)
    def test_bad_first_name(self):
        with self.assertRaises(Exception):
            self.Cust1 = Customer("Smith", "Jo99hn", "555-123-5555", 1200)
    def test_bad_phone_number(self):
        with self.assertRaises(Exception):
            self.Cust1 = Customer("Smith", "John", "555123-5555", 1200)
if __name__ == '__main__':
    unittest.main()
