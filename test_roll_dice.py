from unittest import TestCase
from unittest.mock import patch
from yahtzee import roll_dice


class TestRollDice(TestCase):

    @patch("random.choices", return_value=[1, 1, 1, 1, 1])
    def test_roll_dice_one_side(self, random_sample):
        sides = 1
        dice = 5
        expected = [1, 1, 1, 1, 1]
        actual = roll_dice(dice, sides)
        self.assertEqual(expected, actual)

    @patch("random.choices", return_value=[18])
    def test_roll_dice_one_die(self, random_sample):
        sides = 20
        dice = 1
        expected = [18]
        actual = roll_dice(dice, sides)
        self.assertEqual(expected, actual)

    @patch("random.choices", return_value=[4, 5, 2, 4, 5])
    def test_roll_dice_multiple_dice(self, random_sample):
        sides = 6
        dice = 5
        expected = [2, 4, 4, 5, 5]
        actual = roll_dice(dice, sides)
        self.assertEqual(expected, actual)
