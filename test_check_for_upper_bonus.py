from unittest import TestCase
from yahtzee import check_for_upper_bonus


class TestCheckForUpperBonus(TestCase):
    def test_check_for_upper_bonus_below_63(self):
        value = {'name': 'Jolin', 'extra_rolls': 0, 'yahtzee bonuses': 2, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                                '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                                'large straight': None, 'yahtzee!': 50, 'chance': 17}}
        check_for_upper_bonus(value)
        expected = 0
        actual = value['upper bonus']
        self.assertEqual(expected, actual)

    def test_check_for_upper_bonus_equals_63(self):
        value = {'name': 'Jolin', 'extra_rolls': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 6, 'threes': 9, 'fours': 12, 'fives': 15, 'sixes': 18,
                                '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                                'large straight': None, 'yahtzee!': 50, 'chance': 17}}
        check_for_upper_bonus(value)
        expected = 35
        actual = value['upper bonus']
        self.assertEqual(expected, actual)

    def test_check_for_upper_bonus_above_63(self):
        value = {'name': 'Jolin', 'extra_rolls': 0, 'yahtzee bonuses': 1, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 7, 'threes': 9, 'fours': 20, 'fives': 15, 'sixes': 18,
                                '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                                'large straight': None, 'yahtzee!': 50, 'chance': 17}}
        check_for_upper_bonus(value)
        expected = 35
        actual = value['upper bonus']
        self.assertEqual(expected, actual)

    def test_check_for_upper_bonus_with_empty_scores(self):
        value = {'name': 'Jolin', 'extra_rolls': 3, 'yahtzee bonuses': 1, 'upper bonus': 0,
                 'scoreboard': {'aces': None, 'twos': 10, 'threes': None, 'fours': 20, 'fives': 25, 'sixes': 18,
                                '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                                'large straight': None, 'yahtzee!': 50, 'chance': 17}}
        check_for_upper_bonus(value)
        expected = 35
        actual = value['upper bonus']
        self.assertEqual(expected, actual)

