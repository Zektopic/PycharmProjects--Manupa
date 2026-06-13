import unittest
from test2 import add, substract, multiply, divide, power, remainder

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(substract(5, 3), 2)
        self.assertEqual(substract(3, 5), -2)
        self.assertEqual(substract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2.0)
        self.assertEqual(divide(-6, 3), -2.0)
        self.assertEqual(divide(0, 5), 0.0)

        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(2, -1), 0.5)

        with self.assertRaises(ZeroDivisionError):
            power(0, -1)

    def test_remainder(self):
        self.assertEqual(remainder(5, 3), 2)
        self.assertEqual(remainder(-5, 3), 1) # python modulo behavior
        self.assertEqual(remainder(5, -3), -1)

        with self.assertRaises(ZeroDivisionError):
            remainder(5, 0)

if __name__ == "__main__":
    unittest.main()