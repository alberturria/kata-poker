import unittest

from src.card import Card
from src.enums import SuiteTypes
from src.hand_resolver import HandResolver


class HandResolverTestCase(unittest.TestCase):
    def test_when_there_is_a_royal_flush_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 5), Card(SuiteTypes.HEARTS, 4), Card(SuiteTypes.HEARTS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [[Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                          Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the royal flush one')
