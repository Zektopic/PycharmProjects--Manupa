import unittest
import importlib.util
import os
import sys

# Add the directory containing the module to sys.path to resolve any internal imports if they existed
module_dir = os.path.dirname(os.path.abspath(__file__))
if module_dir not in sys.path:
    sys.path.append(module_dir)

# Import the module with spaces in its filename
module_name = "Fibonacci Numbers (fast)"
module_path = os.path.join(module_dir, module_name + ".py")

spec = importlib.util.spec_from_file_location(module_name, module_path)
fib_module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = fib_module
spec.loader.exec_module(fib_module)

class TestFibonacci(unittest.TestCase):
    def test_base_cases(self):
        """Test the base cases n=1 and n=2"""
        self.assertEqual(fib_module.fibonnaci(1), 1)
        self.assertEqual(fib_module.fibonnaci(2), 1)

    def test_recursive_cases(self):
        """Test known recursive cases"""
        self.assertEqual(fib_module.fibonnaci(3), 2)
        self.assertEqual(fib_module.fibonnaci(4), 3)
        self.assertEqual(fib_module.fibonnaci(5), 5)
        self.assertEqual(fib_module.fibonnaci(10), 55)

    def test_edge_cases(self):
        """Test edge cases like n=0 or negative numbers.
        The current implementation returns None for these."""
        self.assertIsNone(fib_module.fibonnaci(0))
        self.assertIsNone(fib_module.fibonnaci(-1))
        self.assertIsNone(fib_module.fibonnaci(-10))

    def test_large_case(self):
        """Test a larger case to verify lru_cache performance and correctness"""
        # 100th Fibonacci number is known: 354224848179261915075
        self.assertEqual(fib_module.fibonnaci(100), 354224848179261915075)

    def test_type_error(self):
        """Test that it raises TypeError for non-integer inputs like strings"""
        with self.assertRaises(TypeError):
            fib_module.fibonnaci("string")

if __name__ == "__main__":
    unittest.main()
