import unittest

from Student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Student = Student('Smith', 'John', "English", 4.0)

    def tearDown(self):
        del self.Student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.Student.last_name, 'Smith')
        self.assertEqual(self.Student.first_name, 'John')
        self.assertEqual(self.Student.major, 'English')


    def test_object_created_all_attributes(self):
        self.assertEqual(self.Student.last_name, 'Smith')
        self.assertEqual(self.Student.first_name, 'John')
        self.assertEqual(self.Student.major, 'English')
        self.assertEqual(self.Student.gpa, 4.0)

    def test_student_str(self):
        self.assertEqual(str(self.Student), 'Smith, John has major Englishwith gpa: 4.0')

    def test_object_not_created_error_last_name(self):
        pass

    def test_object_not_created_error_first_name(self):
        pass

    def test_object_not_created_error_major(self):
        pass

    def test_object_not_created_error_gpa(self):
        pass


if __name__ == '__main__':
    unittest.main()
