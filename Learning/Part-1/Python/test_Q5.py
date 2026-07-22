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

    def test_acmTeam_two_people(self):
        topic = ['101', '010']
        result = acmTeam(topic)
        self.assertEqual(result, [3, 1])

    def test_acmTeam_disjoint_topics(self):
        topic = ['1000', '0100', '0010', '0001']
        result = acmTeam(topic)
        # Combinations: (1,2)->2, (1,3)->2, (1,4)->2, (2,3)->2, (2,4)->2, (3,4)->2
        # Max topics = 2, number of teams = 6
        self.assertEqual(result, [2, 6])

    def test_acmTeam_mixed_overlap(self):
        topic = ['10101', '11111', '00000', '11001']
        result = acmTeam(topic)
        # person 2 + anyone -> 5 topics
        # (1,2) -> 5
        # (2,3) -> 5
        # (2,4) -> 5
        # Max topics = 5, number of teams = 3
        self.assertEqual(result, [5, 3])

    def test_acmTeam_large_strings(self):
        topic = ['1' * 500, '0' * 500, '1' * 250 + '0' * 250, '0' * 250 + '1' * 250]
        result = acmTeam(topic)
        # (1,2) -> 500
        # (1,3) -> 500
        # (1,4) -> 500
        # (3,4) -> 500
        # Max topics = 500, number of teams = 4
        self.assertEqual(result, [500, 4])

if __name__ == '__main__':
    unittest.main()
