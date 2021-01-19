import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import print_score_categories


class TestPrintScoreCategories(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_score_categories(self, mock_output):
        expected = "1. Aces         7. 3 of a Kind\n" \
                   "2. Twos         8. 4 of a Kind\n" \
                   "3. Threes       9. Full House\n" \
                   "4. Fours       10. Small Straight\n" \
                   "5. Fives       11. Large Straight\n" \
                   "6. Sixes       12. Yahtzee!\n" \
                   "               13. Chance\n"
        print_score_categories()
        self.assertEqual(expected, mock_output.getvalue())