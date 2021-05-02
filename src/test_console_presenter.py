import io
import unittest
from unittest.mock import patch

from src.card import Card
from src.console_presenter import ConsolePresenter
from src.enums import SuiteTypes, CardValue


class ConsolePresenterTestCase(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_presenting_the_start_game_then_the_correct_output_is_displayed(self, mock_stdout):
        sample_number_of_players = 4
        expected_string = 'The poker game has started with 4 players\n'

        ConsolePresenter.present_start_game(sample_number_of_players)

        self.assertEquals(mock_stdout.getvalue(), expected_string, 'Should\'ve returned the correct string')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_presenting_the_winning_hand_then_the_correct_output_is_displayed(self, mock_stdout):
        expected_string = 'ACE - HEARTS, TWO - HEARTS, THREE - CLUBS, FOUR - DIAMONDS, SEVEN - SPADES\n'
        sample_hand = [Card(SuiteTypes.HEARTS, CardValue.ACE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                       Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                       Card(SuiteTypes.SPADES, CardValue.SEVEN)]

        ConsolePresenter.present_hand(sample_hand)

        self.assertEquals(mock_stdout.getvalue(), expected_string, 'Should\'ve returned the correct string')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_presenting_the_round_hands_then_the_correct_output_is_displayed(self, mock_stdout):
        expected_string = 'ACE - HEARTS, TWO - HEARTS, THREE - CLUBS, FOUR - DIAMONDS, SEVEN - SPADES\nACE - HEARTS, TWO - HEARTS, THREE - CLUBS, FOUR - DIAMONDS, SEVEN - SPADES\n'

        sample_hand = [[Card(SuiteTypes.HEARTS, CardValue.ACE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                       Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                       Card(SuiteTypes.SPADES, CardValue.SEVEN)],
                       [Card(SuiteTypes.HEARTS, CardValue.ACE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                       Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                       Card(SuiteTypes.SPADES, CardValue.SEVEN)]]

        ConsolePresenter.present_round_cards(sample_hand)

        self.assertEquals(mock_stdout.getvalue(), expected_string, 'Should\'ve returned the correct string')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_presenting_a_splitter_then_the_correct_string_is_displayed(self, mock_stdout):
        expected_string = '\n\n\n --- \n\n\n'

        ConsolePresenter.present_splitter()

        self.assertEquals(mock_stdout.getvalue(), expected_string, 'Should\'ve returned the correct string')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_presenting_a_round_then_the_correct_string_is_displayed(self, mock_stdout):
        expected_string = '--- PLAYING ROUND 2 ---\n'

        ConsolePresenter.present_round(2)

        self.assertEquals(mock_stdout.getvalue(), expected_string, 'Should\'ve returned the correct string')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_presenting_the_winning_hand_then_the_correct_string_is_displayed(self, mock_stdout):
        expected_string = 'WINNING HAND\nACE - HEARTS, TWO - HEARTS, THREE - CLUBS, FOUR - DIAMONDS, SEVEN - SPADES\n'
        sample_hand = [Card(SuiteTypes.HEARTS, CardValue.ACE), Card(SuiteTypes.HEARTS, CardValue.TWO),
                       Card(SuiteTypes.CLUBS, CardValue.THREE), Card(SuiteTypes.DIAMONDS, CardValue.FOUR),
                       Card(SuiteTypes.SPADES, CardValue.SEVEN)]

        ConsolePresenter.present_winning_hand(sample_hand)

        self.assertEquals(mock_stdout.getvalue(), expected_string, 'Should\'ve returned the correct string')
