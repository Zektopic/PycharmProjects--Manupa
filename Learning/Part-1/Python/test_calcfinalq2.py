import unittest
from calcfinalq2 import add

class TestCalcAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(10.5, 2.5), 13.0)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10.5, -2.5), -13.0)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(10.5, -2.5), 8.0)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, -3), -3)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
