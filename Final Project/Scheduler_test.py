import unittest
from appt import appt
from calendar_list import calendar



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.appt1 = appt(11, 1, 8, 2, 'AM', 'TEST')
    def tearDown(self):
        del self.appt1
    def test_appt_required_attributes(self):
        self.assertEqual(self.appt1.month, 11)
        self.assertEqual(self.appt1.day, 1)
        self.assertEqual(self.appt1.time, 8)
        self.assertEqual(self.appt1.duration, 2)
        self.assertEqual(self.appt1.am_or_pm, 'AM')
        self.assertEqual(self.appt1.subject, 'TEST')
    def test_object_creation_month_format_value_error(self):
        with self.assertRaises(ValueError):
            appt("ERR", 1, 2, 3, 'AM', 'TEST')
    def test_object_creation_day_value_error(self):
        with self.assertRaises(ValueError):
            appt(7, "ERR", 2, 3, 'AM', 'TEST')
    def test_object_creation_time_value_error(self):
        with self.assertRaises(ValueError):
            appt(7, 12, 'ERR', 3, 'AM', 'TEST')
    def test_object_creation_duration_value_error(self):
        with self.assertRaises(ValueError):
            appt(7, 3, 2, 'ERR', 'AM', 'TEST')
    def test_object_creation_am_or_pm_value_error(self):
        with self.assertRaises(ValueError):
            appt(7, 1, 2, 3, 999.00, 'TEST')
    def test_object_creation_month_range_value_error(self):
        with self.assertRaises(ValueError):
            appt(13, 1, 2, 3, 'AM', 'TEST')
    def test_object_creation_day_range_value_error(self):
        with self.assertRaises(ValueError):
            appt(7, 33, 2, 3, 'AM', 'TEST')
    def test_object_creation_day_range_custom_error(self):
        with self.assertRaises(Exception):
            appt(11, 31, 2, 3, 'AM', 'TEST')
    def test_object_creation_time_range_custom_error(self):
        with self.assertRaises(Exception):
            appt(7, 31, 6, 3, 'AM', 'TEST')
if __name__ == '__main__':
    unittest.main()
