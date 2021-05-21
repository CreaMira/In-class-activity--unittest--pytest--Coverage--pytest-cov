import unittest
import leap_year


class testCase_4_F(unittest.TestCase):
    #devide by 4 is false
    def test_empty(self):
        self.assertEqual(leap_year.is_leap_year(1), False)

class testCase_4_T_100_T(unittest.TestCase):
    #devide by 4 is true, devide by 100 is ture
    def test_empty(self):
        self.assertEqual(leap_year.is_leap_year(100), False)

class testCase_4_T_100_F(unittest.TestCase):
    #devide by 4 is true, devide by 100 is false, devide by 400 is true
    def test_empty(self):
        self.assertEqual(leap_year.is_leap_year(8), True)

class testCase_4_T_100_F_400_T(unittest.TestCase):
    #devide by 4 is true, devide by 100 is false, devide by 400 is True
    def test_empty(self):
        self.assertEqual(leap_year.is_leap_year(400), True)

if __name__ == '__main__':
    unittest.main()