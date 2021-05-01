from src.enums import HandType
from collections import Counter


class HandResolver:
    @staticmethod
    def get_highest_hand(array_of_hands):
        highest_hand = None
        hand_type = HandType.HIGHER_CARD
        for hand in array_of_hands:
            highest_hand = hand if highest_hand is None else highest_hand
            if HandResolver._is_royal_flush(hand):
                actual_hand_type = HandType.ROYAL_FLUSH
            elif HandResolver._is_poker(hand):
                actual_hand_type = HandType.POKER
            elif HandResolver._is_full_house(hand):
                actual_hand_type = HandType.FULL_HOUSE
            elif HandResolver._is_color(hand):
                actual_hand_type = HandType.COLOR
            elif HandResolver._is_straight(hand):
                actual_hand_type = HandType.STRAIGHT
            elif HandResolver._is_set(hand):
                actual_hand_type = HandType.SET
            elif HandResolver._is_two_pair(hand):
                actual_hand_type = HandType.TWO_PAIR
            elif HandResolver._is_pair(hand):
                actual_hand_type = HandType.PAIR
            else:
                actual_hand_type = HandType.HIGHER_CARD

            if actual_hand_type.value > hand_type.value:
                highest_hand = hand
                hand_type = actual_hand_type
            elif actual_hand_type.value == hand_type.value:
                if hand_type in [HandType.ROYAL_FLUSH, HandType.STRAIGHT, HandType.HIGHER_CARD, HandType.COLOR, HandType.TWO_PAIR]\
                        and HandResolver._maximum_value_in_the_hand(hand) > HandResolver._maximum_value_in_the_hand(highest_hand):
                    highest_hand = hand
                elif hand_type in [HandType.POKER, HandType.SET, HandType.PAIR] \
                        and HandResolver._get_value_of_the_most_repeated(hand) > HandResolver._get_value_of_the_most_repeated(highest_hand):
                    highest_hand = hand
                elif hand_type == HandType.FULL_HOUSE and HandResolver._get_full_house_value(hand) > HandResolver._get_full_house_value(highest_hand):
                    highest_hand = hand
        return highest_hand

    @staticmethod
    def _get_number_of_suits(hand):
        suits = set(card.suit for card in hand)
        return len(suits)

    @staticmethod
    def _is_straight(hand):
        values = [card.value.value for card in hand]
        return (max(values) - min(values) == 4)

    @staticmethod
    def _maximum_value_in_the_hand(hand):
        return max(card.value.value for card in hand)

    @staticmethod
    def _is_royal_flush(hand):
        number_of_suits = HandResolver._get_number_of_suits(hand)
        return number_of_suits == 1 and HandResolver._is_straight(hand)

    @staticmethod
    def _is_poker(hand):
        collection = Counter([card.value.value for card in hand])
        return collection.most_common(1)[0][1] == 4

    @staticmethod
    def _is_full_house(hand):
        collection = Counter([card.value.value for card in hand])
        return collection.most_common(1)[0][1] == 3 and collection.most_common(2)[1][1] == 2

    @staticmethod
    def _is_color(hand):
        return HandResolver._get_number_of_suits(hand) == 1

    @staticmethod
    def _is_set(hand):
        collection = Counter([card.value.value for card in hand])
        return collection.most_common(1)[0][1] == 3

    @staticmethod
    def _get_value_of_the_most_repeated(hand):
        collection = Counter([card.value.value for card in hand])
        return collection.most_common(1)[0][0]

    @staticmethod
    def _get_full_house_value(hand):
        collection = Counter([card.value.value for card in hand])
        return collection.most_common(1)[0][0]

    @staticmethod
    def _is_two_pair(hand):
        different_values = set(card.value.value for card in hand)
        return len(different_values) == 3

    @staticmethod
    def _is_pair(hand):
        different_values = set(card.value.value for card in hand)
        return len(different_values) == 4
