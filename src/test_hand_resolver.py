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
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the royal flush one')

    def test_when_there_are_two_royal_flush_then_the_higher_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 5), Card(SuiteTypes.HEARTS, 4), Card(SuiteTypes.HEARTS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.HEARTS, 9), Card(SuiteTypes.HEARTS, 5), Card(SuiteTypes.HEARTS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                          Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the royal flush one')

    def test_when_there_is_a_poker_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 1), Card(SuiteTypes.DIAMONDS, 1), Card(SuiteTypes.SPADES, 1),
                         Card(SuiteTypes.CLUBS, 1), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the poker one')

    def test_when_there_are_two_pokers_then_the_highest_poker_wins(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 2), Card(SuiteTypes.SPADES, 2),
                         Card(SuiteTypes.CLUBS, 2), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.HEARTS, 3), Card(SuiteTypes.DIAMONDS, 3), Card(SuiteTypes.SPADES, 3),
                         Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the poker one')

    def test_when_there_is_a_full_house_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 10), Card(SuiteTypes.DIAMONDS, 10), Card(SuiteTypes.SPADES, 11),
                         Card(SuiteTypes.CLUBS, 11), Card(SuiteTypes.HEARTS, 11)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the full house one')

    def test_when_there_are_two_full_house_as_a_higher_hands_then_the_three_highest_repeated_cards_are_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 10), Card(SuiteTypes.DIAMONDS, 10), Card(SuiteTypes.SPADES, 11),
                         Card(SuiteTypes.CLUBS, 11), Card(SuiteTypes.HEARTS, 11)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 12), Card(SuiteTypes.HEARTS, 12), Card(SuiteTypes.DIAMONDS, 12),
                         Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.CLUBS, 2)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the full house one')

    def test_when_there_is_a_color_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 10), Card(SuiteTypes.HEARTS, 1), Card(SuiteTypes.HEARTS, 7),
                         Card(SuiteTypes.HEARTS, 6), Card(SuiteTypes.HEARTS, 4)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the full house one')

    def test_when_there_are_two_colors_as_a_higher_hands_then_the_higher_value_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 10), Card(SuiteTypes.HEARTS, 1), Card(SuiteTypes.HEARTS, 7),
                         Card(SuiteTypes.HEARTS, 6), Card(SuiteTypes.HEARTS, 4)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 1), Card(SuiteTypes.CLUBS, 8), Card(SuiteTypes.CLUBS, 12),
                         Card(SuiteTypes.CLUBS, 2), Card(SuiteTypes.CLUBS, 3)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the full house one')

    def test_when_there_is_a_straight_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 3), Card(SuiteTypes.HEARTS, 4),
                         Card(SuiteTypes.CLUBS, 6), Card(SuiteTypes.HEARTS, 5)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the straight one')

    def test_when_there_are_two_straight_as_a_higher_hand_then_the_one_with_higher_values_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 3), Card(SuiteTypes.HEARTS, 4),
                         Card(SuiteTypes.CLUBS, 6), Card(SuiteTypes.HEARTS, 5)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 4), Card(SuiteTypes.HEARTS, 5), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the higher straight one')

    def test_when_there_is_a_set_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 3), Card(SuiteTypes.DIAMONDS, 3), Card(SuiteTypes.HEARTS, 3),
                         Card(SuiteTypes.CLUBS, 6), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the set one')

    def test_when_there_are_two_sets_as_a_higher_hand_then_the_higher_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 3), Card(SuiteTypes.DIAMONDS, 3), Card(SuiteTypes.CLUBS, 3),
                         Card(SuiteTypes.CLUBS, 6), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 5), Card(SuiteTypes.HEARTS, 5), Card(SuiteTypes.DIAMONDS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the set one')

    def test_when_there_is_a_two_pair_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 3), Card(SuiteTypes.DIAMONDS, 3), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.CLUBS, 5), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the two pair one')

    def test_when_there_are_two_pair_as_a_higher_hand_then_the_one_with_higher_value_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 3), Card(SuiteTypes.DIAMONDS, 3), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.CLUBS, 5), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 3), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 6), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the higher two pair one')

    def test_when_there_is_a_pair_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 3), Card(SuiteTypes.DIAMONDS, 3), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.CLUBS, 6), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 2),
                         Card(SuiteTypes.HEARTS, 6), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the two pair one')

    def test_when_there_are_two_pairs_as_higher_hands_then_the_one_with_higher_value_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 3), Card(SuiteTypes.DIAMONDS, 3), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.CLUBS, 6), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 8), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 2),
                         Card(SuiteTypes.HEARTS, 6), Card(SuiteTypes.DIAMONDS, 7)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the two pair one')

    def test_when_there_is_nothing_as_higher_hand_then_the_one_with_higher_value_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, 3), Card(SuiteTypes.DIAMONDS, 2), Card(SuiteTypes.HEARTS, 5),
                         Card(SuiteTypes.CLUBS, 6), Card(SuiteTypes.HEARTS, 8)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, 3), Card(SuiteTypes.HEARTS, 2), Card(SuiteTypes.DIAMONDS, 6),
                         Card(SuiteTypes.HEARTS, 7), Card(SuiteTypes.CLUBS, 8)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, 5), Card(SuiteTypes.DIAMONDS, 4), Card(SuiteTypes.HEARTS, 2),
                         Card(SuiteTypes.HEARTS, 6), Card(SuiteTypes.DIAMONDS, 9)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_3, 'Should\'ve returned the higher value hand')
