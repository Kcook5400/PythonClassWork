import datetime
import unittest
from half_birthday import half_birthday





class MyTestCase(unittest.TestCase):
    def test_set_true(self):
        mybday=6/25/1988
        self.assertEqual(half_birthday(mybday), 12/25/1988)


if __name__ == '__main__':
    oTime = datetime.datetime.now()
    print(oTime.isoformat())
    unittest.main()