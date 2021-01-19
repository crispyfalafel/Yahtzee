from unittest import TestCase
from unittest.mock import patch
from yahtzee import find_valid_score_categories


class TestFindValidScoreCategories(TestCase):

    @patch('yahtzee.check_for_yahtzee', return_value=False)
    def test_find_valid_score_categories_standard_no_yahtzee(self, check_yahtzee):
        value = {'aces': 9, 'twos': 6, 'threes': 6, 'fours': None, 'fives': None, 'sixes': 6,
                 '3 of a kind': 6, '4 of a kind': 6, 'full house': 0, 'small straight': None,
                 'large straight': 7, 'yahtzee!': 50, 'chance': 0}
        dice = [2, 2, 3, 5, 6]
        expected = ['fours', 'fives', 'small straight']
        actual = find_valid_score_categories(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.check_for_yahtzee', return_value=True)
    def test_find_valid_score_categories_can_record_bonus(self, check_yahtzee):
        value = {'aces': 9, 'twos': None, 'threes': 6, 'fours': 4, 'fives': None, 'sixes': 6,
                 '3 of a kind': 6, '4 of a kind': 6, 'full house': 0, 'small straight': None,
                 'large straight': 7, 'yahtzee!': 50, 'chance': 0}
        dice = [4, 4, 4, 4, 4]
        expected = ['twos', 'fives', 'small straight', 'yahtzee!']
        actual = find_valid_score_categories(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.check_for_yahtzee', return_value=True)
    def test_find_valid_score_categories_yahtzee_score_already_0(self, check_yahtzee):
        value = {'aces': 9, 'twos': 6, 'threes': 6, 'fours': None, 'fives': None, 'sixes': 6,
                 '3 of a kind': 6, '4 of a kind': 6, 'full house': 0, 'small straight': None,
                 'large straight': 7, 'yahtzee!': 0, 'chance': 0}
        dice = [4, 4, 4, 4, 4]
        expected = ['fours', 'fives', 'small straight']
        actual = find_valid_score_categories(value, dice)
        self.assertEqual(expected, actual)
