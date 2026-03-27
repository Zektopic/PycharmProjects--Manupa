import unittest
import math
from benchmark import name_original, name_optimized

class TestBenchmark(unittest.TestCase):
    def test_name_optimized_correctness(self):
        """Test that name_optimized returns the correct factorial of 20."""
        self.assertEqual(name_optimized(1), math.factorial(20))
        self.assertEqual(name_optimized(2), 2 * math.factorial(20))

    def test_name_original_correctness(self):
        """Test that name_original returns the correct factorial of 20."""
        self.assertEqual(name_original(1), math.factorial(20))

    def test_consistency(self):
        """Test that both functions return the same result."""
        input_value = 5
        self.assertEqual(name_original(input_value), name_optimized(input_value))

if __name__ == "__main__":
    unittest.main()
