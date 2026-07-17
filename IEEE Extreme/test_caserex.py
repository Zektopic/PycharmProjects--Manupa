import unittest
from unittest.mock import patch
import io
import importlib.util
import os

class TestCaserex(unittest.TestCase):
    def test_decrypt(self):
        # We need to dynamically load the module because it has spaces in the directory path
        module_name = 'caserex'
        file_path = os.path.join(os.path.dirname(__file__), 'caserex.py')

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        caserex = importlib.util.module_from_spec(spec)

        # Test case: input "ifmmp" with key 1 should decrypt to "hello"
        inputs = ["ifmmp\n", "1\n"]

        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                # Load module (which won't execute decrypt() because of __name__ == '__main__' check)
                spec.loader.exec_module(caserex)

                # Execute the function
                caserex.decrypt()

                output = mock_stdout.getvalue()

                self.assertIn("hello", output)

if __name__ == '__main__':
    unittest.main()
