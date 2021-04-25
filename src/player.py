class Player():
    def __init__(self, id):
        self._id = id
        self._cards = None

    @property
    def cards(self):
        return self._cards