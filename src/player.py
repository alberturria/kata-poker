from copy import copy


class Player:
    def __init__(self, id, dealer):
        self._id = id
        self._dealer = dealer
        self._cards = None

    @property
    def cards(self):
        return copy(self._cards)

    def ask_for_cards(self):
        self._cards = self._dealer.get_cards()
