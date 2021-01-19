from unittest import TestCase
from unittest.mock import patch
from yahtzee import get_menu_choice


class TestGetMenuChoice(TestCase):

    @patch("builtins.input", side_effect=["1"])
    def test_get_menu_choice_keep(self, mock_input):
        actual = get_menu_choice()
        expected = 1
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["2"])
    def test_get_menu_choice_score(self, mock_input):
        actual = get_menu_choice()
        expected = 2
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["3"])
    def test_get_menu_choice_out_of_range(self, mock_input):
        actual = get_menu_choice()
        self.assertIsNone(actual)

    @patch("builtins.input", side_effect=["e"])
    def test_get_menu_choice_not_a_number(self, mock_input):
        actual = get_menu_choice()
        self.assertIsNone(actual)
