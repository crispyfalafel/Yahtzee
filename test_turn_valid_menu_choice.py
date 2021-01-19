from unittest import TestCase
from unittest.mock import patch
from yahtzee import turn_valid_menu_choice


class TestValidMenuChoice(TestCase):

    @patch('yahtzee.get_menu_choice', return_value=1)
    def test_turn_valid_menu_choice_keep(self, menu_choice):
        expected = "keep"
        actual = turn_valid_menu_choice()
        self.assertEqual(expected, actual)

    @patch('yahtzee.get_menu_choice', return_value=2)
    def test_turn_valid_menu_choice_score(self, menu_choice):
        expected = "score"
        actual = turn_valid_menu_choice()
        self.assertEqual(expected, actual)

