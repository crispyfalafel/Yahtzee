from unittest import TestCase
from unittest.mock import patch
from yahtzee import calculate_yahtzee_score_or_bonus


class TestRecordYahtzeeScoreOrBonus(TestCase):

    @patch('yahtzee.check_for_yahtzee', return_value=True)
    def test_record_yahtzee_score_or_bonus_successful_bonus(self, check_for_yahtzee):
        value = {'name': 'player', 'rolls_left': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                                '3 of a kind': 17, '4 of a kind': 25, 'small straight': 30, 'large straight': None,
                                'yahtzee!': 50, 'chance': 17}}
        dice = [4, 4, 4, 4, 4]

        actual = calculate_yahtzee_score_or_bonus(value, dice)
        expected = 100
        self.assertEqual(expected, actual)

    @patch('yahtzee.check_for_yahtzee', return_value=True)
    def test_record_yahtzee_score_or_bonus_record_first_yahtzee(self, check_for_yahtzee):
        value = {'name': 'Jolin', 'rolls_left': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                                '3 of a kind': 17, '4 of a kind': 25, 'small straight': 30, 'large straight': None,
                                'yahtzee!': None, 'chance': 17}}
        dice = [4, 4, 4, 4, 4]

        actual = calculate_yahtzee_score_or_bonus(value, dice)
        expected = 50
        self.assertEqual(expected, actual)

    @patch('yahtzee.check_for_yahtzee', return_value=False)
    def test_check_for_yahtzee_score_or_bonus_record_unsuccessful_first_yahtzee(self, check_yahtzee):
        value = {'name': 'name', 'rolls_left': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                                '3 of a kind': 17, '4 of a kind': 25, 'small straight': 30, 'large straight': None,
                                'yahtzee!': None, 'chance': 17}}
        expected = 0
        dice = [4, 4, 3, 4, 4]
        actual = calculate_yahtzee_score_or_bonus(value, dice)
        self.assertEqual(expected, actual)
