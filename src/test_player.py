import unittest
from unittest.mock import patch, Mock

from src.card import Card
from src.dealer import Dealer
from src.enums import SuiteTypes
from src.player import Player


class PlayerTestCase(unittest.TestCase):
    SAMPLE_ID = 1
    SAMPLE_DEALER = Dealer()
    SAMPLE_CARDS = [Card(SuiteTypes.CLUBS, 1), Card(SuiteTypes.HEARTS, 2)]

    def test_when_player_initializes_then_no_cards_are_provided(self):
        player = Player(self.SAMPLE_ID, self.SAMPLE_DEALER)

        self.assertIsNone(player.cards, 'Should not have any cards')

    def test_when_the_user_ask_for_cards_cards_from_the_dealer_then_the_cards_are_set(self):
        mocked_dealer = self._mock_dealer()

        player = Player(self.SAMPLE_ID, mocked_dealer)

        player.ask_for_cards()

        self.assertEquals(player.cards, self.SAMPLE_CARDS, 'Should\'ve set the cards given by the dealer')

    def _mock_dealer(self):
        mocked_dealer = Mock()
        mocked_dealer.get_cards.return_value = self.SAMPLE_CARDS
        return mocked_dealer

