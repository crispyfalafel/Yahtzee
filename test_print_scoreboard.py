import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import print_scoreboard


class TestPrintScoreboard(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scoreboard(self, mock_output):
        value = {'name': 'j', 'extra_rolls': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 6, 'threes': 4, 'fours': 4, 'fives': 5, 'sixes': 0,
                                '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': 30,
                                'large straight': 0, 'yahtzee!': 50, 'chance': 17}}
        print_scoreboard(value)
        expected = "J's Scoreboard\n" \
                   "Aces           3         3 Of A Kind       17\n" \
                   "Twos           6         4 Of A Kind       25\n" \
                   "Threes         4         Full House        0\n" \
                   "Fours          4         Small Straight    30\n" \
                   "Fives          5         Large Straight    0\n" \
                   "Sixes          0         Yahtzee!          50\n" \
                   "Upper Bonus    0         Chance            17\n" \
                   "                         Yahtzee Bonuses   0 x 100\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scoreboard_with_none(self, mock_output):
        value = {'name': 'player', 'extra_rolls': 0, 'yahtzee bonuses': 0, 'upper bonus': 0,
                 'scoreboard': {'aces': 3, 'twos': 6, 'threes': None, 'fours': None, 'fives': 5, 'sixes': 0,
                                '3 of a kind': 17, '4 of a kind': 25, 'full house': 0, 'small straight': None,
                                'large straight': 0, 'yahtzee!': 50, 'chance': 17}}
        print_scoreboard(value)
        expected = "Player's Scoreboard\n" \
                   "Aces           3         3 Of A Kind       17\n" \
                   "Twos           6         4 Of A Kind       25\n" \
                   "Threes                   Full House        0\n" \
                   "Fours                    Small Straight    \n" \
                   "Fives          5         Large Straight    0\n" \
                   "Sixes          0         Yahtzee!          50\n" \
                   "Upper Bonus    0         Chance            17\n" \
                   "                         Yahtzee Bonuses   0 x 100\n"
        self.assertEqual(expected, mock_output.getvalue())
