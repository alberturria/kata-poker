from src.card import Card


class Dealer:
    def __init__(self):
        self._cards = self._get_cards()

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        pass

    def _get_cards(self):
        return [Card() for card in range(40)]
