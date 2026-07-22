import unittest
from unittest.mock import patch
import io
import importlib.util
import sys

# Need to import Test_2 dynamically if it is needed, but we can also use absolute imports with PYTHONPATH
# The user requires to create test script using unittest and mock patch.

class TestTest2(unittest.TestCase):
    @patch('builtins.input', side_effect=['start', 'stop', 'help', 'invalid', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main(self, mock_stdout, mock_input):
        importlib.invalidate_caches()
        spec = importlib.util.spec_from_file_location("Test_2", "Part-1/wHATTA/Basics/Test_2.py")
        test_2_module = importlib.util.module_from_spec(spec)
        sys.modules["Test_2"] = test_2_module
        spec.loader.exec_module(test_2_module)

        test_2_module.main()

        expected_output = """The car is started moving..
The car stopped moving.
start - start the car
    stop = to stop the car
    quit - to exit
I don't understand?
 App closing ..... Press ENTER
"""
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
