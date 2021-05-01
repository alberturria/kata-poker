from enum import Enum


class GameMode(Enum):
    STANDARD = 'STANDARD'


class SuiteTypes(Enum):
    SPADES = 'SPADES'
    CLUBS = 'CLUBS'
    DIAMONDS = 'DIAMONDS'
    HEARTS = 'HEARTS'


class CardValue(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    JACK = 10
    QUEEN = 11
    KING = 12
    ACE = 14


class HandType(Enum):
    ROYAL_FLUSH = 8
    POKER = 7
    FULL_HOUSE = 6
    COLOR = 5
    STRAIGHT = 4
    SET = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGHER_CARD = 0
