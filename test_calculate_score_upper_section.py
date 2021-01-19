from unittest import TestCase
from yahtzee import calculate_score_upper_section


class TestCalculateScoreUpperSection(TestCase):
    def test_calculate_score_upper_section_aces(self):
        value = [1, 1, 1, 3, 4]
        expected = 3
        actual = calculate_score_upper_section(value, "aces")
        self.assertEqual(expected, actual)

    def test_calculate_score_upper_section_sixes(self):
        value = [1, 1, 1, 6, 6]
        expected = 12
        actual = calculate_score_upper_section(value, "sixes")
        self.assertEqual(expected, actual)

    def test_calculate_score_upper_section_threes(self):
        value = [1, 1, 1, 3, 4]
        expected = 3
        actual = calculate_score_upper_section(value, "threes")
        self.assertEqual(expected, actual)

    def test_calculate_score_upper_section_zero_score(self):
        value = [1, 1, 1, 3, 4]
        expected = 0
        actual = calculate_score_upper_section(value, "twos")
        self.assertEqual(expected, actual)

    def test_calculate_score_upper_section_max_score(self):
        value = [5, 5, 5, 5, 5]
        expected = 25
        actual = calculate_score_upper_section(value, "fives")
        self.assertEqual(expected, actual)
