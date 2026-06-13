import unittest
import importlib.util
import os
import sys

# Add the directory to the path so we can import the module with spaces in the name
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import the module with spaces in the filename
spec = importlib.util.spec_from_file_location("super_factorial", os.path.join(current_dir, "Super factorial.py"))
super_factorial = importlib.util.module_from_spec(spec)
spec.loader.exec_module(super_factorial)

class TestSuperFactorial(unittest.TestCase):
    def test_part1_zero(self):
        self.assertEqual(super_factorial.part1(0), 1)

    def test_part1_one(self):
        self.assertEqual(super_factorial.part1(1), 1)

    def test_part1_small_numbers(self):
        self.assertEqual(super_factorial.part1(2), 2)
        self.assertEqual(super_factorial.part1(3), 6)
        self.assertEqual(super_factorial.part1(4), 24)
        self.assertEqual(super_factorial.part1(5), 120)

    def test_part1_large_number(self):
        # 10! = 3628800
        self.assertEqual(super_factorial.part1(10), 3628800)

if __name__ == '__main__':
    unittest.main()
