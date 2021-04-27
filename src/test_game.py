import unittest
from unittest.mock import patch

from src.game import Game


class GameTest(unittest.TestCase):
    def test_when_creating_the_game_then_the_number_of_players_is_set(self):
        expected_number_of_players = 5
        game = Game(5)

        self.assertEquals(game.number_of_players, expected_number_of_players,
                          'Should have set the correct number of players')

    def test_when_creating_a_game_then_the_standard_poker_mode_is_set(self):
        expected_mode = 'STANDARD'
        game = Game()

        self.assertEquals(game.game_mode.value, expected_mode, 'Should have set the standard mode')

    @patch('src.game.Dealer')
    def test_when_game_start_then_the_dealer_shuffles_the_cards(self, mocked_dealer_constructor):
        mock_dealer = mocked_dealer_constructor.return_value
        game = Game()

        game.start_game()

        self.assertTrue(mock_dealer.shuffle.called, 'Should have called the dealer')
