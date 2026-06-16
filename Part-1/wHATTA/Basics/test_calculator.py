import unittest
import subprocess
import os

class TestCalculator(unittest.TestCase):
    def run_calculator(self, input_text):
        script_path = os.path.join(os.path.dirname(__file__), 'Calculator.py')
        process = subprocess.Popen(['python3', script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=input_text)
        return stdout, stderr, process.returncode

    def test_addition(self):
        stdout, stderr, returncode = self.run_calculator("10\n5\na\n")
        self.assertEqual(returncode, 0)
        self.assertIn("The addition is 15", stdout)

    def test_addition_zero_division_avoided(self):
        # Even if num2 is 0, addition should work and not crash
        stdout, stderr, returncode = self.run_calculator("10\n0\na\n")
        self.assertEqual(returncode, 0)
        self.assertIn("The addition is 10", stdout)
        self.assertEqual(stderr, "")

    def test_subtraction(self):
        stdout, stderr, returncode = self.run_calculator("10\n5\ns\n")
        self.assertEqual(returncode, 0)
        self.assertIn("The substraction is 5", stdout)

    def test_multiplication(self):
        stdout, stderr, returncode = self.run_calculator("10\n5\nm\n")
        self.assertEqual(returncode, 0)
        self.assertIn("The multipication is 50", stdout)

    def test_division(self):
        stdout, stderr, returncode = self.run_calculator("10\n5\nd\n")
        self.assertEqual(returncode, 0)
        self.assertIn("The division is 2.0", stdout)

    def test_division_by_zero(self):
        stdout, stderr, returncode = self.run_calculator("10\n0\nd\n")
        self.assertEqual(returncode, 0)
        self.assertIn("Cannot divide by zero", stdout)

if __name__ == '__main__':
    unittest.main()
