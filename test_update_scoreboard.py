from unittest import TestCase
from yahtzee import update_scoreboard


class TestUpdateScoreboard(TestCase):
    def test_update_scoreboard_regular_score_large_straight(self):
        value = {'name': 'p', 'rolls_left': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                                '3 of a kind': 17, '4 of a kind': 25, 'small straight': 30, 'large straight': None,
                                'yahtzee!': 50, 'chance': 17}}
        update_scoreboard(value, 'large straight', 40)
        expected = {'name': 'p', 'rolls_left': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                    'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                                   '3 of a kind': 17, '4 of a kind': 25, 'small straight': 30, 'large straight': 40,
                                   'yahtzee!': 50, 'chance': 17}}
        self.assertEqual(expected, value)

    def test_update_scoreboard_regular_score_fours(self):
        value = {'name': 'r', 'rolls_left': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                                '3 of a kind': 17, '4 of a kind': 25, 'small straight': 30, 'large straight': None,
                                'yahtzee!': 50, 'chance': 17}}
        update_scoreboard(value, 'fours', 0)
        expected = {'name': 'r', 'rolls_left': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                    'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': 0, 'fives': 5, 'sixes': 0,
                                   '3 of a kind': 17, '4 of a kind': 25, 'small straight': 30, 'large straight': None,
                                   'yahtzee!': 50, 'chance': 17}}
        self.assertEqual(expected, value)

    def test_update_scoreboard_yahtzee_bonus(self):
        value = {'name': 'p', 'rolls_left': 0, 'yahtzee bonuses': 1, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                                '3 of a kind': 17, '4 of a kind': 25, 'small straight': 30, 'large straight': None,
                                'yahtzee!': 50, 'chance': 17}}
        update_scoreboard(value, 'yahtzee!', 100)
        expected = {'name': 'p', 'rolls_left': 0, 'yahtzee bonuses': 2, 'upper bonus': 0,
                    'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                                   '3 of a kind': 17, '4 of a kind': 25, 'small straight': 30, 'large straight': None,
                                   'yahtzee!': 50, 'chance': 17}}
        self.assertEqual(expected, value)