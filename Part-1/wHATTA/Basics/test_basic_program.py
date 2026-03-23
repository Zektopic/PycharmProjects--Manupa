import unittest
import importlib
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
basic_program = importlib.import_module('Basic Program')
max_num = basic_program.max_num

class TestMaxNum(unittest.TestCase):
    def test_max_num_first(self):
        self.assertEqual(max_num(5, 4, 3), 5)

    def test_max_num_second(self):
        self.assertEqual(max_num(3, 5, 4), 5)

    def test_max_num_third(self):
        self.assertEqual(max_num(3, 4, 5), 5)

    def test_max_num_all_equal(self):
        self.assertEqual(max_num(5, 5, 5), 5)

    def test_max_num_two_equal(self):
        self.assertEqual(max_num(5, 5, 3), 5)
        self.assertEqual(max_num(3, 5, 5), 5)
        self.assertEqual(max_num(5, 3, 5), 5)

    def test_max_num_negative(self):
        self.assertEqual(max_num(-1, -2, -3), -1)
        self.assertEqual(max_num(-3, -1, -2), -1)
        self.assertEqual(max_num(-3, -2, -1), -1)

if __name__ == '__main__':
    unittest.main()
