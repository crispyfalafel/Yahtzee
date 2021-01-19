from unittest import TestCase
from yahtzee import is_scoreboard_full


class TestIsScoreboardFull(TestCase):
    def test_is_scoreboard_full_true(self):
        value = {'name': 'name', 'extra_rolls': 2, 'yahtzee bonuses': 0, 'upper bonus': 0,
                 'scoreboard': {'aces': 9, 'twos': 6, 'threes': 6, 'fours': 5, 'fives': 4, 'sixes': 6,
                                '3 of a kind': 6, '4 of a kind': 6, 'full house': 0, 'small straight': 7,
                                'large straight': 7, 'yahtzee!': 0, 'chance': 0}}
        actual = is_scoreboard_full(value)
        self.assertTrue(actual)

    def test_is_scoreboard_full_false(self):
        value = {'name': 'name', 'extra_rolls': 2, 'yahtzee bonuses': 3, 'upper bonus': 0,
                 'scoreboard': {'aces': 9, 'twos': 6, 'threes': None, 'fours': 5, 'fives': 4, 'sixes': 6,
                                '3 of a kind': 6, '4 of a kind': 6, 'full house': 0, 'small straight': 7,
                                'large straight': 7, 'yahtzee!': 0, 'chance': None}}
        actual = is_scoreboard_full(value)
        self.assertFalse(actual)
