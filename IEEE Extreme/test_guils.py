import unittest
import importlib.util
import os
import sys

# Dynamically load guils.py to avoid issues with directory names having spaces
current_dir = os.path.dirname(os.path.abspath(__file__))
guils_path = os.path.join(current_dir, 'guils.py')

spec = importlib.util.spec_from_file_location("guils", guils_path)
guils = importlib.util.module_from_spec(spec)
sys.modules["guils"] = guils
spec.loader.exec_module(guils)

class TestGuilsEncrypt(unittest.TestCase):
    def test_uppercase(self):
        self.assertEqual(guils.encrypt("HELLO", 3), "KHOOR")

    def test_lowercase(self):
        self.assertEqual(guils.encrypt("hello", 3), "khoor")

    def test_mixed_case(self):
        self.assertEqual(guils.encrypt("Hello", 3), "Khoor")

    def test_zero_shift(self):
        self.assertEqual(guils.encrypt("Hello", 0), "Hello")

    def test_wrap_around(self):
        self.assertEqual(guils.encrypt("XYZ", 3), "ABC")
        self.assertEqual(guils.encrypt("xyz", 3), "abc")

    def test_large_shift(self):
        self.assertEqual(guils.encrypt("Hello", 26), "Hello")
        self.assertEqual(guils.encrypt("Hello", 29), "Khoor")

if __name__ == '__main__':
    unittest.main()
