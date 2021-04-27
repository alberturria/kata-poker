import unittest

from src.dealer import Dealer
from src.enums import SuiteTypes
from src.player import Player


class DealerTestCase(unittest.TestCase):
    SAMPLE_PLAYER_1 = Player(1)
    SAMPLE_PLAYER_2 = Player(2)
    SAMPLE_PLAYERS = [SAMPLE_PLAYER_1, SAMPLE_PLAYER_2]

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
        initial_cards = dealer.cards

        shuffled_cards = dealer.shuffle()

        self._assert_the_order_is_altered_and_not_its_content(initial_cards, shuffled_cards)

    def test_when_dealer_gives_cards_to_the_users_then_five_cards_are_given(self):
        dealer = Dealer()

        round_cards = dealer.get_cards()

        self._assert_the_correct_number_of_cards_are_retrieved(round_cards)

    def test_when_the_dealer_gives_cards_more_than_10_times_during_a_round_then_an_exception_is_raised(self):
        dealer = Dealer()
        with self.assertRaises(Exception):
            for i in range(11):
                dealer.get_cards()

    def test_when_the_dealer_set_new_round_then_the_cards_are_restored_and_reshuffled(self):
        dealer = Dealer()
        initial_cards = dealer.cards

        dealer.set_new_round()

        new_round_cards = dealer.cards

        self._assert_the_order_is_altered_and_not_its_content(initial_cards, new_round_cards)

    def _assert_all_the_cards_are_given(self, cards):
        for suit in SuiteTypes:
            cards_of_a_same_suite = [card for card in cards if card.suit is suit]
            sorted_cards = sorted(cards_of_a_same_suite, key=lambda card: card.value)
            for index in range(len(sorted_cards)):
                self.assertEquals(sorted_cards[index].value, index + 1, 'Should\'ve had the correct card')

    def _assert_the_order_is_altered_and_not_its_content(self, initial_cards, shuffled_cards):
        self.assertCountEqual(initial_cards, shuffled_cards, 'Should contain the same cards')
        self.assertNotEqual(initial_cards, shuffled_cards, 'Should not be the same cards')

    def _assert_the_correct_number_of_cards_are_retrieved(self, round_cards):
        expected_number_of_cards = 5
        for card in round_cards:
            self.assertIsInstance(card, card.__class__, 'Should\'ve been a card')
        self.assertEquals(len(round_cards), expected_number_of_cards, 'Should\'ve give 5 cards')
