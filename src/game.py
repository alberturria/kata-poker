from src.console_presenter import ConsolePresenter
from src.dealer import Dealer
from src.enums import GameMode
from src.hand_resolver import HandResolver
from src.player import Player


class Game:
    def __init__(self, number_of_players=2, mode=GameMode.STANDARD):
        self._number_of_players = number_of_players
        self._game_mode = mode
        self._players = []
        self._dealer = None

    @property
    def number_of_players(self):
        return self._number_of_players

    @property
    def game_mode(self):
        return self._game_mode

    def start_game(self):
        ConsolePresenter.present_start_game(self.number_of_players)
        self._dealer = Dealer()
        self._players = [Player(index, self._dealer) for index in range(self._number_of_players)]
        self._dealer.shuffle()
        for index in range(5):
            self.play_round(index)

    def play_round(self, round_number):
        ConsolePresenter.present_round(round_number)
        self._dealer.set_new_round()
        for player in self._players:
            player.ask_for_cards()
        self._solve_round()
        ConsolePresenter.present_splitter()

    def _solve_round(self):
        cards = []
        for player in self._players:
            cards.append(player.cards)

        ConsolePresenter.present_round_cards(cards)
        HandResolver.get_highest_hand(cards)