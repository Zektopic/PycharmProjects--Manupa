import unittest
import importlib.util
import os

module_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Basic Program.py')
spec = importlib.util.spec_from_file_location('basic_program', module_path)
basic_program = importlib.util.module_from_spec(spec)
spec.loader.exec_module(basic_program)

max_num = basic_program.max_num

class TestMaxNum(unittest.TestCase):
    def test_max_num_first(self):
        self.assertEqual(max_num(5, 4, 3), 5)

    def test_max_num_second(self):
        self.assertEqual(max_num(3, 5, 4), 5)

    def test_max_num_third(self):
        self.assertEqual(max_num(3, 4, 5), 5)

    def test_max_num_all_equal(self):
        self.assertEqual(max_num(5, 5, 5), 5)

    def test_max_num_two_equal(self):
        self.assertEqual(max_num(5, 5, 3), 5)
        self.assertEqual(max_num(3, 5, 5), 5)
        self.assertEqual(max_num(5, 3, 5), 5)

    def test_max_num_negative(self):
        self.assertEqual(max_num(-1, -2, -3), -1)
        self.assertEqual(max_num(-3, -1, -2), -1)
        self.assertEqual(max_num(-3, -2, -1), -1)

if __name__ == '__main__':
    unittest.main()
