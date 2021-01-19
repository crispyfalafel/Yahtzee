from unittest import TestCase
from yahtzee import check_for_yahtzee


class TestCheckForYahtzee(TestCase):
    def test_check_for_yahtzee_true(self):
        value = [3, 3, 3, 3, 3]
        actual = check_for_yahtzee(value)
        self.assertTrue(actual)

    def test_check_for_yahtzee_false(self):
        value = [3, 3, 3, 3, 6]
        actual = check_for_yahtzee(value)
        self.assertFalse(actual)
