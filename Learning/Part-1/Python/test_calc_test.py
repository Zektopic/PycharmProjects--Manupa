import unittest
import importlib.util
import os
from unittest.mock import patch
import io

class TestCalcTest(unittest.TestCase):
    def setUp(self):
        # Dynamically load the calc.test module since its name includes a dot
        module_name = 'calc_test'
        file_path = os.path.join(os.path.dirname(__file__), 'calc.test.py')

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        self.calc_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.calc_module)

    @patch('builtins.input', side_effect=['4', '10', '0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_division_by_zero_prints_error(self, mock_stdout, mock_input):
        self.calc_module.main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Division by zero is not allowed.", output)

    @patch('builtins.input', side_effect=['4', '10', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_division_normal(self, mock_stdout, mock_input):
        self.calc_module.main()
        output = mock_stdout.getvalue()
        self.assertIn("10 / 2 = 5.0", output)
        self.assertNotIn("Error: Division by zero is not allowed.", output)

if __name__ == '__main__':
    unittest.main()
