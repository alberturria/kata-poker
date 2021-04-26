import unittest
from copy import copy

from src.dealer import Dealer
from src.enums import SuiteTypes


class DealerTestCase(unittest.TestCase):
    def test_when_dealer_is_created_then_he_has_the_cards(self):
        dealer = Dealer()

        for card in dealer.cards:
            self.assertIsInstance(card, card.__class__, 'Should\'ve a card')

    def test_when_dealer_gets_the_cards_then_it_gets_the_correct_number_of_them(self):
        expected_number_of_cards = 52
        dealer = Dealer()

        self.assertEquals(len(dealer.cards), expected_number_of_cards, 'Should have the correct number of cards')

    def test_when_the_dealer_gets_the_cards_then_all_the_cards_into_the_deck_are_given(self):
        dealer = Dealer()

        self._assert_all_the_cards_are_given(dealer.cards)

    def test_when_the_dealer_shuffles_the_cards_then_the_order_is_altered(self):
        dealer = Dealer()
        initial_cards = copy(dealer.cards)

        shuffled_cards = dealer.shuffle()

        self._assert_the_order_is_altered_and_not_its_content(initial_cards, shuffled_cards)

    def _assert_all_the_cards_are_given(self, cards):
        for suit in SuiteTypes:
            cards_of_a_same_suite = [card for card in cards if card.suit is suit]
            sorted_cards = sorted(cards_of_a_same_suite, key=lambda card: card.value)
            for index in range(len(sorted_cards)):
                self.assertEquals(sorted_cards[index].value, index + 1, 'Should\'ve had the correct card')

    def _assert_the_order_is_altered_and_not_its_content(self, initial_cards, shuffled_cards):
        self.assertCountEqual(initial_cards, shuffled_cards, 'Should contain the same cards')
        self.assertNotEqual(initial_cards, shuffled_cards, 'Should not be the same cards')
