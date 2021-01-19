from unittest import TestCase
from unittest.mock import patch
from yahtzee import get_valid_score_type


class TestGetValidScoreType(TestCase):

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'large straight'])
    @patch('builtins.input', side_effect=['1'])
    def test_get_valid_score_type_valid_aces(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "aces"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'twos', 'fours', 'large straight'])
    @patch('builtins.input', side_effect=['2'])
    def test_get_valid_score_type_twos(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': None, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "twos"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'threes', 'fours', 'large straight'])
    @patch('builtins.input', side_effect=['3'])
    def test_get_valid_score_type_threes(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': None, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "threes"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['fours', 'large straight'])
    @patch('builtins.input', side_effect=['4'])
    def test_get_valid_score_type_fours(self, mock_input, valid_categories):
        value = {'aces': 3, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "fours"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'fives', 'large straight'])
    @patch('builtins.input', side_effect=['5'])
    def test_get_valid_score_type_fives(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': None, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "fives"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'sixes', 'large straight'])
    @patch('builtins.input', side_effect=['6'])
    def test_get_valid_score_type_sixes(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': None,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "sixes"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', '3 of a kind', 'large straight'])
    @patch('builtins.input', side_effect=['7'])
    def test_get_valid_score_type_3_of_a_kind(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': None, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "3 of a kind"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', '4 of a kind', 'large straight'])
    @patch('builtins.input', side_effect=['8'])
    def test_get_valid_score_type_4_of_a_kind(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': None, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "4 of a kind"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'full house', 'large straight'])
    @patch('builtins.input', side_effect=['9'])
    def test_get_valid_score_type_full_house(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': None, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "full house"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'small straight', 'large straight'])
    @patch('builtins.input', side_effect=['10'])
    def test_get_valid_score_type_small_straight(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': None,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "small straight"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'large straight'])
    @patch('builtins.input', side_effect=['11'])
    def test_get_valid_score_type_large_straight(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 8, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "large straight"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'large straight', 'yahtzee!'])
    @patch('builtins.input', side_effect=['12'])
    def test_get_valid_score_type_first_yahtzee(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': None, 'chance': 17}
        dice = [3, 3, 3, 3, 3]
        expected = "yahtzee!"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'large straight', 'chance'])
    @patch('builtins.input', side_effect=['13'])
    def test_get_valid_score_type_valid_chance(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 0, 'chance': None}
        dice = [3, 3, 3, 3, 3]
        expected = "chance"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'large straight', 'chance'])
    @patch('builtins.input', side_effect=['16'])
    def test_get_valid_score_type_invalid_number_out_of_range(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 6, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 0, 'chance': None}
        dice = [3, 3, 3, 3, 3]
        actual = get_valid_score_type(value, dice)
        self.assertIsNone(actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'large straight', 'chance'])
    @patch('builtins.input', side_effect=['one'])
    def test_get_valid_score_type_invalid_not_a_number(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 4, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': None}
        dice = [3, 3, 3, 3, 3]
        actual = get_valid_score_type(value, dice)
        self.assertIsNone(actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['fours', 'large straight', 'chance'])
    @patch('builtins.input', side_effect=['1'])
    def test_get_valid_score_type_invalid_score_already_filled(self, mock_input, valid_categories):
        value = {'aces': 2, 'twos': 4, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 0, 'chance': None}
        dice = [3, 3, 3, 3, 3]
        actual = get_valid_score_type(value, dice)
        self.assertIsNone(actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'large straight', 'yahtzee!'])
    @patch('builtins.input', side_effect=['12'])
    def test_get_valid_score_type_valid_second_yahtzee(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': 4}
        dice = [3, 3, 3, 3, 3]
        expected = "yahtzee!"
        actual = get_valid_score_type(value, dice)
        self.assertEqual(expected, actual)

    @patch('yahtzee.find_valid_score_categories', return_value=['aces', 'fours', 'large straight', 'chance'])
    @patch('builtins.input', side_effect=['12'])
    def test_get_valid_score_type_invalid_second_yahtzee_attempt(self, mock_input, valid_categories):
        value = {'aces': None, 'twos': 6, 'threes': 4, 'fours': None, 'fives': 5, 'sixes': 0,
                 '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                 'large straight': None, 'yahtzee!': 50, 'chance': None}
        dice = [2, 3, 3, 3, 3]
        actual = get_valid_score_type(value, dice)
        self.assertIsNone(actual)
