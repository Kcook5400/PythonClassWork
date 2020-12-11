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
    def test_object_creation_format_value_error(self):
        with self.assertRaises(ValueError):
            appt("ERR", 1, 2, 3, 'AM', 'TEST')
            appt(11, "ERR", 2, 3, 'AM', 'TEST')
            appt(11, 12, 'ERR', 3, 'AM', 'TEST')
            appt(11, 3, 2, 'ERR', 'AM', 'TEST')
            appt(11, 1, 2, 3, 999, 'TEST')
            appt(11, 1, 2, 3, 'AM', 999)
    def test_object_creation_range_value_error(self):
        with self.assertRaises(ValueError):
            appt(13, 1, 2, 3, 'AM', 'TEST')
if __name__ == '__main__':
    unittest.main()
