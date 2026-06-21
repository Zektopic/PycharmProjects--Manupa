import unittest
import importlib.util
import os
import io
from unittest.mock import patch

class TestCalexpected(unittest.TestCase):
    def setUp(self):
        module_name = 'calexpected'
        file_path = os.path.join(os.path.dirname(__file__), 'Calexpected by author.py')
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        self.calc_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.calc_module)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_divide_by_zero_error_path(self, mock_stdout):
        # The divide function tries a/b and catches Exception e, printing e
        result = self.calc_module.divide(10, 0)
        output = mock_stdout.getvalue()

        # When printing Exception("division by zero"), it's printed to stdout
        self.assertIsNone(result)
        self.assertIn("division by zero", output.lower())

if __name__ == '__main__':
    unittest.main()
