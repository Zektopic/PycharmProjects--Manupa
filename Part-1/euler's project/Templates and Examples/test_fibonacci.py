import unittest
import fibonacci_fast as fib_module

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
