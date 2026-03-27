import unittest
from calcfinalq2 import add, subtract, multiply, divide, power, remainder

class TestCalcOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        # Testing division by zero
        # Current behavior: prints error and returns None
        self.assertIsNone(divide(10, 0))

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_remainder(self):
        self.assertEqual(remainder(10, 3), 1)

    def test_divide_invalid_input(self):
        # Now that we catch only ZeroDivisionError, passing a string should raise TypeError
        with self.assertRaises(TypeError):
            divide("10", 2)

if __name__ == '__main__':
    unittest.main()
