import unittest
import io
import sys
from unittest.mock import patch
import importlib.util

spec = importlib.util.spec_from_file_location("test_module", "Learning/Part-1/Python/test.py")
test_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_module)

class TestArithmeticOperations(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add(self, mock_stdout):
        test_module.add(2, 3)
        self.assertEqual(mock_stdout.getvalue().strip(), "2 + 3 = 5")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_substract(self, mock_stdout):
        test_module.substract(5, 2)
        self.assertEqual(mock_stdout.getvalue().strip(), "5 - 2 = 3")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_multiply(self, mock_stdout):
        test_module.multiply(3, 4)
        self.assertEqual(mock_stdout.getvalue().strip(), "3 * 4 = 12")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_divide(self, mock_stdout):
        test_module.divide(12, 3)
        self.assertEqual(mock_stdout.getvalue().strip(), "12 / 3 = 4.0")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_divide_by_zero(self, mock_stdout):
        test_module.divide(12, 0)
        self.assertEqual(mock_stdout.getvalue().strip(), "float division by zero\n12 / 0 = None")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_power(self, mock_stdout):
        test_module.power(2, 3)
        self.assertEqual(mock_stdout.getvalue().strip(), "2 ^ 3 = 8")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_reminder(self, mock_stdout):
        test_module.reminder(5, 2)
        self.assertEqual(mock_stdout.getvalue().strip(), "5 % 2 = 1")

if __name__ == '__main__':
    unittest.main()
