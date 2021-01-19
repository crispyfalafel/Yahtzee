from unittest import TestCase
from yahtzee import calculate_final_score


class TestCalculateFinalScore(TestCase):
    def test_calculate_final_score_no_bonuses(self):
        value = {'name': 'p1', 'extra_rolls': 2, 'yahtzee bonuses': 0, 'upper bonus': 0,
                 'scoreboard': {'aces': 10, 'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10,
                                'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, 'small straight': 10,
                                'large straight': 10, 'yahtzee!': 10, 'chance': 10}}

        expected = 120
        actual = calculate_final_score(value)
        self.assertEqual(expected, actual)

    def test_calculate_final_score_with_upper_bonus(self):
        value = {'name': 'p1', 'extra_rolls': 2, 'yahtzee bonuses': 0, 'upper bonus': 5,
                 'scoreboard': {'aces': 10, 'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10,
                                'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, 'small straight': 10,
                                'large straight': 10, 'yahtzee!': 10, 'chance': 10}}

        expected = 125
        actual = calculate_final_score(value)
        self.assertEqual(expected, actual)

    def test_calculate_final_score_with_yahtzee_bonus(self):
        value = {'name': 'p1', 'extra_rolls': 2, 'yahtzee bonuses': 2, 'upper bonus': 0,
                 'scoreboard': {'aces': 10, 'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10,
                                'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, 'small straight': 10,
                                'large straight': 10, 'yahtzee!': 10, 'chance': 10}}

        expected = 320
        actual = calculate_final_score(value)
        self.assertEqual(expected, actual)
