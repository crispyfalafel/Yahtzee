from unittest import TestCase
from yahtzee import calculate_score_straights, LOWER_SCORE_REGEXES


class TestCalculateScoreStraights(TestCase):
    def test_calculate_score_straights_small_straight_valid_start_from_1(self):
        value = [1, 2, 3, 4, 4]
        expected = 30
        actual = calculate_score_straights(value, "small straight")
        self.assertEqual(expected, actual)

    def test_calculate_score_straights_small_straight_valid_start_from_2(self):
        value = [2, 2, 3, 4, 5]
        expected = 30
        actual = calculate_score_straights(value, "small straight")
        self.assertEqual(expected, actual)

    def test_calculate_score_straights_small_straight_valid_start_from_3(self):
        value = [1, 3, 4, 5, 6]
        expected = 30
        actual = calculate_score_straights(value, "small straight")
        self.assertEqual(expected, actual)

    def test_calculate_score_straights_large_straight_valid_start_from_1(self):
        value = [1, 2, 3, 4, 5]
        expected = 40
        actual = calculate_score_straights(value, "large straight")
        self.assertEqual(expected, actual)

    def test_calculate_score_straights_large_straight_valid_start_from_2(self):
        value = [2, 3, 4, 5, 6]
        expected = 40
        actual = calculate_score_straights(value, "large straight")
        self.assertEqual(expected, actual)

    def test_calculate_score_straights_small_straight_invalid(self):
        value = [1, 3, 3, 5, 6]
        expected = 0
        actual = calculate_score_straights(value, "small straight")
        self.assertEqual(expected, actual)

    def test_calculate_score_straights_large_straight_invalid(self):
        value = [2, 4, 4, 4, 5]
        expected = 0
        actual = calculate_score_straights(value, "large straight")
        self.assertEqual(expected, actual)
