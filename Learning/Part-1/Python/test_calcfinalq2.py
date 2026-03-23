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

if __name__ == '__main__':
    unittest.main()
