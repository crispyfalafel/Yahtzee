import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import determine_winner


class TestDetermineWinner(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('yahtzee.calculate_final_score', side_effect=[120, 120])
    def test_determine_winner_tie(self, score, mock_output):
        value_1 = {'name': 'p1', 'extra_rolls': 1, 'yahtzee bonuses': 0, 'upper bonus': 0,
                   'scoreboard': {'aces': 10, 'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10,
                                  'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, 'full house': 0,
                                  'small straight': 10, 'large straight': 10, 'yahtzee!': 10, 'chance': 10}}
        value_2 = {'name': 'p2', 'extra_rolls': 2, 'yahtzee bonuses': 0, 'upper bonus': 0,
                   'scoreboard': {'aces': 10, 'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10,
                                  'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, 'full house': 0,
                                  'small straight': 10, 'large straight': 10, 'yahtzee!': 10, 'chance': 10}}

        determine_winner(value_1, value_2)
        expected_output = "P1's Scoreboard\n" \
                          "Aces           10        3 Of A Kind       10\n" \
                          "Twos           10        4 Of A Kind       10\n" \
                          "Threes         10        Full House        0\n" \
                          "Fours          10        Small Straight    10\n" \
                          "Fives          10        Large Straight    10\n" \
                          "Sixes          10        Yahtzee!          10\n" \
                          "Upper Bonus    0         Chance            10\n" \
                          "                         Yahtzee Bonuses   0 x 100\n" \
                          "P1's final score: 120 pts.\n" \
                          "P2's Scoreboard\n" \
                          "Aces           10        3 Of A Kind       10\n" \
                          "Twos           10        4 Of A Kind       10\n" \
                          "Threes         10        Full House        0\n" \
                          "Fours          10        Small Straight    10\n" \
                          "Fives          10        Large Straight    10\n" \
                          "Sixes          10        Yahtzee!          10\n" \
                          "Upper Bonus    0         Chance            10\n" \
                          "                         Yahtzee Bonuses   0 x 100\n" \
                          "P2's final score: 120 pts.\n" \
                          "Tie!\n"
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('yahtzee.calculate_final_score', side_effect=[121, 120])
    def test_calculate_winner_p1_wins(self, score, mock_output):
        value_1 = {'name': 'p1', 'extra_rolls': 2, 'yahtzee bonuses': 0, 'upper bonus': 0,
                   'scoreboard': {'aces': 10, 'twos': 11, 'threes': 10, 'fours': 10, 'fives': 10,
                                  'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, 'full house': 0,
                                  'small straight': 10, 'large straight': 10, 'yahtzee!': 10, 'chance': 10}}
        value_2 = {'name': 'p2', 'extra_rolls': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                   'scoreboard': {'aces': 10, 'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10,
                                  'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, 'full house': 0,
                                  'small straight': 10, 'large straight': 10, 'yahtzee!': 10, 'chance': 10}}
        determine_winner(value_1, value_2)
        expected_output = "P1's Scoreboard\n" \
                          "Aces           10        3 Of A Kind       10\n" \
                          "Twos           11        4 Of A Kind       10\n" \
                          "Threes         10        Full House        0\n" \
                          "Fours          10        Small Straight    10\n" \
                          "Fives          10        Large Straight    10\n" \
                          "Sixes          10        Yahtzee!          10\n" \
                          "Upper Bonus    0         Chance            10\n" \
                          "                         Yahtzee Bonuses   0 x 100\n" \
                          "P1's final score: 121 pts.\n" \
                          "P2's Scoreboard\n" \
                          "Aces           10        3 Of A Kind       10\n" \
                          "Twos           10        4 Of A Kind       10\n" \
                          "Threes         10        Full House        0\n" \
                          "Fours          10        Small Straight    10\n" \
                          "Fives          10        Large Straight    10\n" \
                          "Sixes          10        Yahtzee!          10\n" \
                          "Upper Bonus    0         Chance            10\n" \
                          "                         Yahtzee Bonuses   0 x 100\n" \
                          "P2's final score: 120 pts.\n" \
                          "P1 won!\n"
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('yahtzee.calculate_final_score', side_effect=[120, 155])
    def test_calculate_winner_p2_wins(self, score, mock_output):
        value_1 = {'name': 'p1', 'extra_rolls': 3, 'yahtzee bonuses': 0, 'upper bonus': 0,
                   'scoreboard': {'aces': 10, 'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10,
                                  'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, 'full house': 0,
                                  'small straight': 10, 'large straight': 10, 'yahtzee!': 10, 'chance': 10}}
        value_2 = {'name': 'p2', 'extra_rolls': 1, 'yahtzee bonuses': 0, 'upper bonus': 35,
                   'scoreboard': {'aces': 10, 'twos': 10, 'threes': 10, 'fours': 10, 'fives': 10,
                                  'sixes': 10, '3 of a kind': 10, '4 of a kind': 10, 'full house': 0,
                                  'small straight': 10, 'large straight': 10, 'yahtzee!': 10, 'chance': 10}}
        determine_winner(value_1, value_2)
        expected_output = "P1's Scoreboard\n" \
                          "Aces           10        3 Of A Kind       10\n" \
                          "Twos           10        4 Of A Kind       10\n" \
                          "Threes         10        Full House        0\n" \
                          "Fours          10        Small Straight    10\n" \
                          "Fives          10        Large Straight    10\n" \
                          "Sixes          10        Yahtzee!          10\n" \
                          "Upper Bonus    0         Chance            10\n" \
                          "                         Yahtzee Bonuses   0 x 100\n" \
                          "P1's final score: 120 pts.\n" \
                          "P2's Scoreboard\n" \
                          "Aces           10        3 Of A Kind       10\n" \
                          "Twos           10        4 Of A Kind       10\n" \
                          "Threes         10        Full House        0\n" \
                          "Fours          10        Small Straight    10\n" \
                          "Fives          10        Large Straight    10\n" \
                          "Sixes          10        Yahtzee!          10\n" \
                          "Upper Bonus    35        Chance            10\n" \
                          "                         Yahtzee Bonuses   0 x 100\n" \
                          "P2's final score: 155 pts.\n" \
                          "P2 won!\n"
        self.assertEqual(expected_output, mock_output.getvalue())
