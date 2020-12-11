import unittest
from appt import appt
from calendar_list import calendar



class MyTestCase(unittest.TestCase):
    """Set up function"""
    def setUp(self):
        self.appt1 = appt("January", 1, 8, 2, 'AM', 'TEST')
        self.calendar1 = calendar()
    """"tear down function"""
    def tearDown(self):
        del self.appt1

    """Creating test cases for Appt class"""
    def test_appt_required_attributes(self):
        self.assertEqual(self.appt1.month, "January")
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
    def test_object_creation_day_range_custom_exception(self):
        with self.assertRaises(Exception):
            appt(11, 31, 2, 3, 'AM', 'TEST')
    def test_object_creation_time_range_custom_exception(self):
        with self.assertRaises(Exception):
            appt(7, 31, 6, 3, 'AM', 'TEST')
    def test_object_creation_str_return(self):
        self.assertEqual(str(self.appt1), "Month 11 Day 1 Time 8AM Duration 2")

    """ Creating Test Cases for calendar_list class"""
    def test_calendar_object_creation_str_return(self):
        self.assertEqual(str(self.calendar1), '[]')
    def test_calendar_enter_appt(self):
        self.assertTrue(self.calendar1.add_appt(self.appt1))
    def test_calendar_enter_existing_appt(self):
        self.calendar1.add_appt(self.appt1)
        self.assertFalse(self.calendar1.add_appt(self.appt1))
    def test_calendar_display_appt(self):
        self.calendar1.add_appt(self.appt1)
        self.assertEqual(self.calendar1.display_appt(), ['Appointment: 11 1 at 8AM Subject: TEST'])


if __name__ == '__main__':
    unittest.main()
