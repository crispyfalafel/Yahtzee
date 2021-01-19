from unittest import TestCase
from unittest.mock import patch
from yahtzee import get_dice_to_keep


class TestGetDiceToKeep(TestCase):

    @patch("builtins.input", side_effect=["1 2 3 4 5"])
    def test_get_dice_to_keep_keep_all_dice(self, mock_input):
        value = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        actual = get_dice_to_keep(value)
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=[""])
    def test_get_dice_to_keep_keep_no_dice(self, mock_input):
        value = [1, 2, 3, 4, 5]
        expected = []
        actual = get_dice_to_keep(value)
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["2 4 3"])
    def test_get_dice_to_keep_keep_some_dice(self, mock_input):
        value = [1, 2, 3, 4, 6]
        expected = [2, 3, 4]
        actual = get_dice_to_keep(value)
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["3 3 3"])
    def test_get_dice_to_keep_keep_all_repeating_dice(self, mock_input):
        value = [3, 3, 3, 4, 6]
        expected = [3, 3, 3]
        actual = get_dice_to_keep(value)
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["2 2"])
    def test_get_dice_to_keep_keep_some_repeating_dice(self, mock_input):
        value = [2, 2, 2, 2, 4]
        expected = [2, 2]
        actual = get_dice_to_keep(value)
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["1 5 5"])
    def test_get_dice_to_keep_invalid_not_in_list(self, mock_input):
        value = [3, 3, 3, 4, 6]
        actual = get_dice_to_keep(value)
        self.assertIsNone(actual)

    @patch("builtins.input", side_effect=["sf"])
    def test_get_dice_to_keep_invalid_not_number(self, mock_input):
        value = [3, 3, 3, 4, 6]
        actual = get_dice_to_keep(value)
        self.assertIsNone(actual)
