import unittest
import importlib.util
import os
import sys

# Add the directory to the path so we can import the module with spaces in the name
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import io
from unittest.mock import patch

# Import the module with spaces in the filename
spec = importlib.util.spec_from_file_location("super_factorial", os.path.join(current_dir, "Super factorial.py"))
super_factorial = importlib.util.module_from_spec(spec)
with patch('sys.stdout', new_callable=io.StringIO):
    spec.loader.exec_module(super_factorial)

class TestSuperFactorial(unittest.TestCase):
    def test_part1_zero(self):
        self.assertEqual(super_factorial.part1(0), 1)

    def test_part1_one(self):
        self.assertEqual(super_factorial.part1(1), 1)

    def test_part1_small_numbers(self):
        self.assertEqual(super_factorial.part1(2), 2)
        self.assertEqual(super_factorial.part1(3), 6)
        self.assertEqual(super_factorial.part1(4), 24)
        self.assertEqual(super_factorial.part1(5), 120)

    def test_part1_large_number(self):
        # 10! = 3628800
        self.assertEqual(super_factorial.part1(10), 3628800)

    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_valid_input(self, mock_stdout, mock_input):
        super_factorial.main()
        # part1(3) = 6
        # then total_1 *= 3, count_1 times (3 times)
        # 6 * 3 * 3 * 3 = 162
        self.assertEqual(mock_stdout.getvalue().strip(), "162")

    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_boundary_valid_input(self, mock_stdout, mock_input):
        super_factorial.main()
        # part1(0) = 1
        # while loop doesn't run since count_1 (0) is not > 0
        self.assertEqual(mock_stdout.getvalue().strip(), "1")

    @patch('builtins.input', return_value='-1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_invalid_input_negative(self, mock_stdout, mock_input):
        super_factorial.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid answer.")

    @patch('builtins.input', return_value='751')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_invalid_input_too_large(self, mock_stdout, mock_input):
        super_factorial.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid answer.")

if __name__ == '__main__':
    unittest.main()
