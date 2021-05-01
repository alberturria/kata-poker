import unittest

from src.card import Card
from src.enums import SuiteTypes, CardValue
from src.hand_resolver import HandResolver


class HandResolverTestCase(unittest.TestCase):
    def test_when_there_is_a_royal_flush_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.FIVE), Card(SuiteTypes.HEARTS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the royal flush one')

    def test_when_there_are_two_royal_flush_then_the_higher_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.FIVE), Card(SuiteTypes.HEARTS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.HEARTS, CardValue.NINE), Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the royal flush one')

    def test_when_there_is_a_poker_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.ACE), Card(SuiteTypes.DIAMONDS, CardValue.ACE),
                         Card(SuiteTypes.SPADES, CardValue.ACE),
                         Card(SuiteTypes.CLUBS, CardValue.ACE), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the poker one')

    def test_when_there_are_two_pokers_then_the_highest_poker_wins(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.TWO), Card(SuiteTypes.DIAMONDS, CardValue.TWO),
                         Card(SuiteTypes.SPADES, CardValue.TWO),
                         Card(SuiteTypes.CLUBS, CardValue.TWO), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.HEARTS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.THREE),
                         Card(SuiteTypes.SPADES, CardValue.THREE),
                         Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the poker one')

    def test_when_there_is_a_full_house_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.JACK), Card(SuiteTypes.DIAMONDS, CardValue.JACK),
                         Card(SuiteTypes.SPADES, CardValue.QUEEN),
                         Card(SuiteTypes.CLUBS, CardValue.QUEEN), Card(SuiteTypes.HEARTS, CardValue.QUEEN)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the full house one')

    def test_when_there_are_two_full_house_as_a_higher_hands_then_the_three_highest_repeated_cards_are_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.JACK), Card(SuiteTypes.DIAMONDS, CardValue.JACK),
                         Card(SuiteTypes.SPADES, CardValue.QUEEN),
                         Card(SuiteTypes.CLUBS, CardValue.QUEEN), Card(SuiteTypes.HEARTS, CardValue.QUEEN)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.KING), Card(SuiteTypes.HEARTS, CardValue.KING),
                         Card(SuiteTypes.DIAMONDS, CardValue.KING),
                         Card(SuiteTypes.HEARTS, CardValue.TWO), Card(SuiteTypes.CLUBS, CardValue.TWO)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the full house one')

    def test_when_there_is_a_color_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.JACK), Card(SuiteTypes.HEARTS, CardValue.ACE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN),
                         Card(SuiteTypes.HEARTS, CardValue.SIX), Card(SuiteTypes.HEARTS, CardValue.FOUR)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the full house one')

    def test_when_there_are_two_colors_as_a_higher_hands_then_the_higher_value_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.JACK), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN),
                         Card(SuiteTypes.HEARTS, CardValue.SIX), Card(SuiteTypes.HEARTS, CardValue.FOUR)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.ACE), Card(SuiteTypes.CLUBS, CardValue.EIGHT),
                         Card(SuiteTypes.CLUBS, CardValue.FIVE),
                         Card(SuiteTypes.CLUBS, CardValue.TWO), Card(SuiteTypes.CLUBS, CardValue.THREE)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the full house one')

    def test_when_there_is_a_straight_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.TWO), Card(SuiteTypes.DIAMONDS, CardValue.THREE),
                         Card(SuiteTypes.HEARTS, CardValue.FOUR),
                         Card(SuiteTypes.CLUBS, CardValue.SIX), Card(SuiteTypes.HEARTS, CardValue.FIVE)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the straight one')

    def test_when_there_are_two_straight_as_a_higher_hand_then_the_one_with_higher_values_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.TWO), Card(SuiteTypes.DIAMONDS, CardValue.THREE),
                         Card(SuiteTypes.HEARTS, CardValue.FOUR),
                         Card(SuiteTypes.CLUBS, CardValue.SIX), Card(SuiteTypes.HEARTS, CardValue.FIVE)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.FOUR), Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_1, sample_hand_2, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the higher straight one')

    def test_when_there_is_a_set_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.THREE),
                         Card(SuiteTypes.HEARTS, CardValue.THREE),
                         Card(SuiteTypes.CLUBS, CardValue.SIX), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the set one')

    def test_when_there_are_two_sets_as_a_higher_hand_then_the_higher_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.THREE),
                         Card(SuiteTypes.CLUBS, CardValue.THREE),
                         Card(SuiteTypes.CLUBS, CardValue.SIX), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.FIVE), Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.DIAMONDS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the set one')

    def test_when_there_is_a_two_pair_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.THREE),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.CLUBS, CardValue.FIVE), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the two pair one')

    def test_when_there_are_two_pair_as_a_higher_hand_then_the_one_with_higher_value_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.THREE),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.CLUBS, CardValue.FIVE), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.THREE),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SIX), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the higher two pair one')

    def test_when_there_is_a_pair_as_a_higher_hand_then_that_one_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.THREE),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.CLUBS, CardValue.SIX), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.HEARTS, CardValue.SIX), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_1, 'Should\'ve returned the two pair one')

    def test_when_there_are_two_pairs_as_higher_hands_then_the_one_with_higher_value_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.THREE),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.CLUBS, CardValue.SIX), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.EIGHT), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.HEARTS, CardValue.SIX), Card(SuiteTypes.DIAMONDS, CardValue.SEVEN)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_2, 'Should\'ve returned the two pair one')

    def test_when_there_is_nothing_as_higher_hand_then_the_one_with_higher_value_is_returned(self):
        sample_hand_1 = [Card(SuiteTypes.HEARTS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.TWO),
                         Card(SuiteTypes.HEARTS, CardValue.FIVE),
                         Card(SuiteTypes.CLUBS, CardValue.SIX), Card(SuiteTypes.HEARTS, CardValue.EIGHT)]
        sample_hand_2 = [Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.DIAMONDS, CardValue.SIX),
                         Card(SuiteTypes.HEARTS, CardValue.SEVEN), Card(SuiteTypes.CLUBS, CardValue.EIGHT)]
        sample_hand_3 = [Card(SuiteTypes.DIAMONDS, CardValue.FIVE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                         Card(SuiteTypes.HEARTS, CardValue.TWO),
                         Card(SuiteTypes.HEARTS, CardValue.SIX), Card(SuiteTypes.DIAMONDS, CardValue.NINE)]

        result = HandResolver.get_highest_hand([sample_hand_2, sample_hand_1, sample_hand_3])

        self.assertEquals(result, sample_hand_3, 'Should\'ve returned the higher value hand')
