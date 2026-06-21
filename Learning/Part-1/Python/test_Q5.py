import unittest
from Q5 import acmTeam

class TestQ5(unittest.TestCase):
    def test_acmTeam(self):
        topic = ['10101', '11100', '11010', '00101']
        result = acmTeam(topic)
        self.assertEqual(result, [5, 2])

    def test_acmTeam_all_ones(self):
        topic = ['111', '111', '111']
        result = acmTeam(topic)
        # 3 teams, all know 3 topics
        self.assertEqual(result, [3, 3])

    def test_acmTeam_all_zeros(self):
        topic = ['000', '000']
        result = acmTeam(topic)
        self.assertEqual(result, [0, 1])

if __name__ == '__main__':
    unittest.main()
