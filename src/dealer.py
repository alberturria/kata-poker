from copy import copy
from random import shuffle

from src.card import Card
from src.enums import SuiteTypes, CardValue


class Dealer:
    def __init__(self):
        self._cards = self._init_deck()

    @property
    def cards(self):
        return copy(self._cards)

    def shuffle(self):
        shuffle(self._cards)
        return self._cards

    def get_cards(self):
        if len(self._cards) >= 5:
            cards_to_be_returned = self._cards[-5:]
            self._cards = self._cards[:len(self._cards) - 5]
            return cards_to_be_returned
        else:
            raise Exception('The dealer does not have more cards')

    def set_new_round(self):
        self._init_deck()
        self.shuffle()

    def _init_deck(self):
        self._cards = []
        for value in CardValue:
            for suit in SuiteTypes:
                self._cards.append(Card(suit=suit, value=value))

        return self._cards
