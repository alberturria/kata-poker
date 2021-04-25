from src.dealer import Dealer
from src.enums import GameMode


class Game:
    def __init__(self, number_of_players=2, mode=GameMode.STANDARD):
        self._number_of_players = number_of_players
        self._game_mode = mode

    @property
    def number_of_players(self):
        return self._number_of_players

    @property
    def game_mode(self):
        return self._game_mode

    def start_game(self):
        dealer = Dealer()
        dealer.shuffle()
