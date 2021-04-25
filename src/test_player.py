import unittest

from src.player import Player


class PlayerTestCase(unittest.TestCase):
    SAMPLE_ID = 1

    def test_when_player_initializes_then_no_cards_are_provided(self):
        player = Player(self.SAMPLE_ID)

        self.assertIsNone(player.cards, 'Should not have any cards')
