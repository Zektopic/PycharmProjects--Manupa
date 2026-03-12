import unittest
import sys
import os

# Add the directory to sys.path to import the module with spaces in its name
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import the module
prime_module = __import__("Prime nmbers")
isPrime = prime_module.isPrime

class TestIsPrime(unittest.TestCase):
    def test_negative_numbers(self):
        self.assertFalse(isPrime(-1))
        self.assertFalse(isPrime(-10))

    def test_zero_and_one(self):
        self.assertFalse(isPrime(0))
        self.assertFalse(isPrime(1))

    def test_small_primes(self):
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(3))
        self.assertTrue(isPrime(5))
        self.assertTrue(isPrime(7))
        self.assertTrue(isPrime(11))
        self.assertTrue(isPrime(13))

    def test_small_composites(self):
        self.assertFalse(isPrime(4))
        self.assertFalse(isPrime(6))
        self.assertFalse(isPrime(8))
        self.assertFalse(isPrime(9))
        self.assertFalse(isPrime(10))
        self.assertFalse(isPrime(12))

    def test_squares_of_primes(self):
        self.assertFalse(isPrime(25))
        self.assertFalse(isPrime(49))
        self.assertFalse(isPrime(121))
        self.assertFalse(isPrime(169))

    def test_large_numbers(self):
        self.assertTrue(isPrime(101))
        self.assertTrue(isPrime(103))
        self.assertFalse(isPrime(100))
        self.assertFalse(isPrime(102))

if __name__ == "__main__":
    unittest.main()
