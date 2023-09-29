import unittest
import calc
import sys

class TestCalcMethods(unittest.TestCase):

    def setUp(self) -> None:
        #it will run before each test
        pass
        return super().setUp()
    
    def tearDown(self) -> None:
        #it will run after each test
        pass
        return super().tearDown()

    def test_add(self):
        self.assertEqual(calc.add_func(2, -3), -1)

    def test_subtract(self):
        self.assertEqual(calc.subtract_func(2, -3), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiple_func(2, -3), -6)

    def test_divide(self):
        self.assertEqual(calc.divide_func(2, 2), 1)
        self.assertEqual(calc.divide_func(2, 3), 0.67)

        with self.assertRaises(ValueError):
            calc.divide_func (10, 0)


if __name__ == '__main__':
    unittest.main()


