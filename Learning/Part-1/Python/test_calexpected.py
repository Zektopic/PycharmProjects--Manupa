import unittest
import sys
import io
import os
import importlib.util
from unittest.mock import patch

class TestCalexpected(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Mock input to return '7' (Terminate: #) and exit immediately
        # Mock sys.stdout to prevent printing
        with patch('builtins.input', side_effect=['#']), \
             patch('sys.stdout', new_callable=io.StringIO):

            # Load the module dynamically due to spaces in filename
            module_name = "calexpected_by_author"
            file_path = os.path.join(os.path.dirname(__file__), "Calexpected by author.py")
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            cls.cal_module = importlib.util.module_from_spec(spec)

            try:
                spec.loader.exec_module(cls.cal_module)
            except SystemExit:
                pass

    def test_divide_normal(self):
        result = self.cal_module.divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_by_zero(self):
        # We need to test the printed output
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            result = self.cal_module.divide(10, 0)
            self.assertIsNone(result)
            output = mock_stdout.getvalue().strip()
            # When the raw ZeroDivisionError exception object is printed, it says "division by zero" or "float division by zero"
            # Since we will change it to print "float division by zero", the test will check for that.
            self.assertEqual(output, "float division by zero")

if __name__ == '__main__':
    unittest.main()
