class ConsolePresenter:

    @staticmethod
    def present_start_game(number_of_players):
        print('The poker game has started with {} players'.format(number_of_players))

    @staticmethod
    def present_hand(sample_hand):
        parsed_cards = []
        for card in sample_hand:
            parsed_cards.append('{value} - {suite}'.format(suite=card.suit.value, value=card.value.name))
        result = ', '.join(parsed_cards)

        print(result)

    @staticmethod
    def present_splitter():
        print('\n\n\n --- \n\n')

    @staticmethod
    def present_round(round_number):
        print('--- PLAYING ROUND {} ---'.format(round_number))

    @staticmethod
    def present_round_cards(cards):
        for hand in cards:
            ConsolePresenter.present_hand(hand)

    @staticmethod
    def present_winning_hand(hand):
        print('WINNING HAND')
        ConsolePresenter.present_hand(hand)
