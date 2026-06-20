import unittest
import io
import sys
import calcfinalq2

class TestCalcHistory(unittest.TestCase):
    def setUp(self):
        # Reset the global history list before each test
        calcfinalq2.hist = []

    def test_history_append(self):
        # Initial state should be empty
        self.assertEqual(len(calcfinalq2.hist), 0)

        # Test adding a single calculation
        calc_string_1 = "5 + 5 = 10.0"
        calcfinalq2.history(calc_string_1)

        self.assertEqual(len(calcfinalq2.hist), 1)
        self.assertEqual(calcfinalq2.hist[0], calc_string_1)

        # Test adding a second calculation
        calc_string_2 = "10 - 2 = 8.0"
        calcfinalq2.history(calc_string_2)

        self.assertEqual(len(calcfinalq2.hist), 2)
        self.assertEqual(calcfinalq2.hist[1], calc_string_2)

    def test_history_print_empty(self):
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            calcfinalq2.history_print()
            self.assertEqual(captured_output.getvalue().strip(), "No past calculations to show")
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__

    def test_history_print_with_items(self):
        # Add some items to history
        calcfinalq2.hist = ["5 + 5 = 10.0", "10 - 2 = 8.0"]

        # Redirect stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            calcfinalq2.history_print()
            output = captured_output.getvalue().strip().split('\n')
            self.assertEqual(len(output), 2)
            self.assertEqual(output[0], "5 + 5 = 10.0")
            self.assertEqual(output[1], "10 - 2 = 8.0")
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__

class TestCalcOperations(unittest.TestCase):
    def test_divide_by_zero(self):
        # Redirect stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            # Test int division
            result = calcfinalq2.divide(10, 0)
            self.assertIsNone(result)
            self.assertEqual(captured_output.getvalue().strip(), "division by zero")

            # Reset stdout for the next check
            captured_output.truncate(0)
            captured_output.seek(0)

            # Test float division
            result_float = calcfinalq2.divide(10.0, 0.0)
            self.assertIsNone(result_float)
            self.assertEqual(captured_output.getvalue().strip(), "float division by zero")
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__

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
