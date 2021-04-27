class HandResolver:
    @staticmethod
    def get_highest_hand(array_of_hands):
        for hand in array_of_hands:
            number_of_suits = HandResolver._get_number_of_suits(hand)
            return hand if number_of_suits == 1 and HandResolver._is_straight(hand) else None
        return None

    @staticmethod
    def _get_number_of_suits(hand):
        suits = set(card.suit for card in hand)
        return len(suits)

    @staticmethod
    def _is_straight(hand):
        values = [card.value for card in hand]
        return (max(values) - min(values) == 4)



