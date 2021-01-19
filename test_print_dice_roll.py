import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import print_dice_roll


class TestPrintDiceRoll(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dice_roll(self, mock_output):
        value = [1, 3, 3, 4, 5]
        print_dice_roll(value)
        expected = "Your dice rolls: 1 3 3 4 5\n"
        self.assertEqual(expected, mock_output.getvalue())

