from unittest import TestCase
from yahtzee import calculate_score_lower_other, LOWER_SCORE_REGEXES


class TestCalculateScoreLowerSection(TestCase):
    def test_calculate_score_lower_other_full_house_valid_3_2(self):
        value = [2, 2, 2, 4, 4]
        expected = 25
        actual = calculate_score_lower_other(value, "full house")
        self.assertEqual(expected, actual)

    def test_calculate_score_lower_other_full_house_valid_2_3(self):
        value = [1, 1, 6, 6, 6]
        expected = 25
        actual = calculate_score_lower_other(value, "full house")
        self.assertEqual(expected, actual)

    def test_calculate_score_lower_other_full_house_invalid(self):
        value = [1, 2, 2, 4, 5]
        expected = 0
        actual = calculate_score_lower_other(value, "full house")
        self.assertEqual(expected, actual)

    def test_calculate_score_lower_other_3_of_a_kind_valid_beginning(self):
        value = [2, 2, 2, 3, 4]
        expected = 13
        actual = calculate_score_lower_other(value, "3 of a kind")
        self.assertEqual(expected, actual)

    def test_calculate_score_lower_other_3_of_a_kind_valid_end(self):
        value = [1, 2, 3, 3, 3]
        expected = 12
        actual = calculate_score_lower_other(value, "3 of a kind")
        self.assertEqual(expected, actual)

    def test_calculate_score_lower_other_3_of_a_kind_valid_middle(self):
        value = [2, 4, 4, 4, 5]
        expected = 19
        actual = calculate_score_lower_other(value, "3 of a kind")
        self.assertEqual(expected, actual)

    def test_calculate_score_lower_other_3_of_a_kind_invalid(self):
        value = [1, 2, 2, 4, 4]
        expected = 0
        actual = calculate_score_lower_other(value, "3 of a kind")
        self.assertEqual(expected, actual)

    def test_calculate_score_lower_other_4_of_a_kind_valid_beginning(self):
        value = [4, 4, 4, 4, 5]
        expected = 21
        actual = calculate_score_lower_other(value, "4 of a kind")
        self.assertEqual(expected, actual)

    def test_calculate_score_lower_other_4_of_a_kind_valid_end(self):
        value = [3, 6, 6, 6, 6]
        expected = 27
        actual = calculate_score_lower_other(value, "4 of a kind")
        self.assertEqual(expected, actual)

    def test_calculate_score_lower_other_4_of_a_kind_invalid(self):
        value = [3, 4, 4, 4, 5]
        expected = 0
        actual = calculate_score_lower_other(value, "4 of a kind")
        self.assertEqual(expected, actual)
