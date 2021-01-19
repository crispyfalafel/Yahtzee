import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import print_score_recorded


class TestPrintScoreRecorded(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_score_recorded_zero_points(self, mock_output):
        print_score_recorded(0, "full house")
        expected_output = "You recorded 0 pts for Full House.\n"
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_score_recorded_positive_points(self, mock_output):
        print_score_recorded(25, "4 of a kind")
        expected_output = "You recorded 25 pts for 4 Of A Kind.\n"
        self.assertEqual(expected_output, mock_output.getvalue())
