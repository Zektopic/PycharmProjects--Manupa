import unittest
import io
import sys
from unittest.mock import patch
from knight import isSafe, printSolution, solveKT, solveKTUtil, main

class TestKnight(unittest.TestCase):
    def test_isSafe_valid(self):
        board = [[-1, -1], [-1, -1]]
        self.assertTrue(isSafe(0, 0, board))
        self.assertTrue(isSafe(1, 1, board))

    def test_isSafe_invalid_bounds(self):
        board = [[-1, -1], [-1, -1]]
        self.assertFalse(isSafe(-1, 0, board))
        self.assertFalse(isSafe(0, -1, board))
        self.assertFalse(isSafe(2, 0, board))
        self.assertFalse(isSafe(0, 2, board))

    def test_isSafe_already_visited(self):
        board = [[0, -1], [-1, -1]]
        self.assertFalse(isSafe(0, 0, board))

    def test_printSolution(self):
        board = [[0, 1], [2, 3]]
        expected_output = "0 1 \n2 3 \n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            printSolution(2, board)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_solveKT_valid_solution(self):
        # A 5x5 board has a valid knight's tour
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            result = solveKT(5)
            self.assertTrue(result)
            output = fake_out.getvalue()
            # We expect 5 lines of output, one for each row
            self.assertEqual(len(output.strip().split('\n')), 5)

    def test_solveKT_no_solution(self):
        # A 3x3 board has no valid knight's tour
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            result = solveKT(3)
            self.assertFalse(result)
            self.assertEqual(fake_out.getvalue().strip(), "Solution does not exist")

    def test_main(self):
        # Test main function with input '3'
        with patch('builtins.input', return_value='3'):
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                main()
                self.assertEqual(fake_out.getvalue().strip(), "Solution does not exist")

if __name__ == '__main__':
    unittest.main()
