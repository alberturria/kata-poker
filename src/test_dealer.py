import unittest

from src.dealer import Dealer


class DealerTestCase(unittest.TestCase):
    def test_when_dealer_is_created_then_he_has_the_cards(self):
        dealer = Dealer()

        for card in dealer.cards:
            self.assertIsInstance(card, card.__class__, 'Should\'ve a card')

    def test_when_dealer_gets_the_cards_then_it_gets_the_correct_number_of_them(self):
        expected_number_of_cards = 40
        dealer = Dealer()

        self.assertEquals(len(dealer.cards), expected_number_of_cards, 'Should have the correct number of cards')
