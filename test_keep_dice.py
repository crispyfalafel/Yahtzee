from unittest import TestCase
from unittest.mock import patch
from yahtzee import keep_dice


class TestKeepDice(TestCase):

    @patch("yahtzee.get_dice_to_keep", return_value=[1, 2, 3, 4, 5])
    def test_keep_dice_keep_all(self, get_dice):
        value = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        actual = keep_dice(value)
        self.assertEqual(expected, actual)

    @patch("yahtzee.get_dice_to_keep", return_value=[])
    def test_keep_dice_keep_none(self, get_dice):
        value = [1, 2, 3, 4, 5]
        expected = []
        actual = keep_dice(value)
        self.assertEqual(expected, actual)

    @patch("yahtzee.get_dice_to_keep", return_value=[3, 5])
    def test_keep_dice_keep_some(self, get_dice):
        value = [1, 2, 3, 4, 5]
        expected = [3, 5]
        actual = keep_dice(value)
        self.assertEqual(expected, actual)

    @patch("yahtzee.get_dice_to_keep", return_value=[3, 3, 3])
    def test_keep_dice_repeating(self, get_dice):
        value = [3, 3, 3, 4, 5]
        expected = [3, 3, 3]
        actual = keep_dice(value)
        self.assertEqual(expected, actual)

