import unittest
import sys
import os
import io
from unittest.mock import patch
from importlib.util import spec_from_file_location, module_from_spec

# Get path to the module, relative to this test file
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "Prime nmbers.py")

# Dynamically load the module because of spaces in filename
spec = spec_from_file_location("prime_numbers", module_path)
prime_numbers = module_from_spec(spec)
with patch('sys.stdout', new=io.StringIO()): # Ignore any print outputs if top-level code ever executes unexpectedly
    spec.loader.exec_module(prime_numbers)


class TestPrimeNumbers(unittest.TestCase):
    def test_prime_numbers(self):
        # Happy path - Primes
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 97]
        for p in primes:
            with self.subTest(p=p):
                self.assertTrue(prime_numbers.isPrime(p))

    def test_composite_numbers(self):
        # Happy path - Composites
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 100]
        for c in composites:
            with self.subTest(c=c):
                self.assertFalse(prime_numbers.isPrime(c))

    def test_perfect_squares(self):
        # Specific check for perfect squares (related to the bug we fixed)
        perfect_squares = [25, 49, 121, 169]
        for ps in perfect_squares:
            with self.subTest(ps=ps):
                self.assertFalse(prime_numbers.isPrime(ps))

    def test_edge_cases(self):
        # Negative numbers, 0, 1
        edge_cases = [-5, -1, 0, 1]
        for ec in edge_cases:
            with self.subTest(ec=ec):
                self.assertFalse(prime_numbers.isPrime(ec))


if __name__ == '__main__':
    unittest.main()
