import unittest
import leap_year


class testCaseAdd(unittest.TestCase):
    #devide by 4 is false
    def test_empty(self):
        test_year = 1
        self.assertEqual(leap_year.is_leap_year(test_year), True)

    #devide by 4 is true, devide by 100 is ture
    def test_empty(self):
        test_year = 100
        self.assertEqual(leap_year.is_leap_year(test_year), False)

    #devide by 4 is true, devide by 100 is false, devide by 400 is true
    def test_empty(self):
        test_year = 400
        self.assertEqual(leap_year.is_leap_year(test_year), True)

    #devide by 4 is true, devide by 100 is false, devide by 400 is false
    def test_empty(self):
        test_year = 300
        self.assertEqual(leap_year.is_leap_year(test_year), False)

if __name__ == '__main__':
    unittest.main()