from unittest import TestCase
from yahtzee import create_player_information


class TestCreatePlayerInformation(TestCase):
    def test_create_player_information(self):
        actual = create_player_information("Test")
        expected = {'name': 'Test', 'extra_rolls': 2, 'yahtzee bonuses': 0, 'upper bonus': 0,
                    'scoreboard': {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None,
                                   'sixes': None, '3 of a kind': None, '4 of a kind': None, 'full house': None,
                                   'small straight': None, 'large straight': None, 'yahtzee!': None, 'chance': None}}
        self.assertEqual(actual, expected)
