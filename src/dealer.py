from random import shuffle

from src.card import Card
from src.enums import SuiteTypes


class Dealer:
    def __init__(self):
        self._cards = self._get_cards()

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        shuffle(self._cards)
        return self._cards

    def _get_cards(self):
        cards = []
        for index in range(1, 14):
            for suit in SuiteTypes:
                cards.append(Card(suit=suit, value=index))

        return cards
