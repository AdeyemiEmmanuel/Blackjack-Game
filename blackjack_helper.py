from random import randint


def print_card_name(card_rank):
    if card_rank == 1:
        card_name = 'Ace'
    elif card_rank == 11:
        card_name = 'Jack'
    elif card_rank == 12:
        card_name = 'Queen'
    elif card_rank == 13:
        card_name = 'King'
    else:
        card_name = card_rank

    if card_rank == 8 or card_rank == 1:
        print('Drew an ' + str(card_name))
    elif card_rank < 1 or card_rank > 13:
        print('BAD CARD')
    else:
        print('Drew a ' + str(card_name))


def draw_card():
    card_rank = randint(1, 13)
    print_card_name(card_rank)

    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        card_value = 10
    elif card_rank == 1:
        card_value = 11
    else:
        card_value = card_rank

    return card_value


def print_header(message):
    print('-----------')
    print(message)
    print('-----------')


def draw_starting_hand(name):
    print_header(name.upper() + '\'S TURN')
    return draw_card() + draw_card()


def print_end_turn_status(hand_value):
    print('Final hand: ' + str(hand_value) + '.')

    if hand_value == 21:
        print('BLACKJACK!')
    elif hand_value > 21:
        print('BUST.')


def print_end_game_status(user_hand, dealer_hand, players, index, hand_totals, user_score):
    if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
        user_score[index] += 1
        print('{} wins! Score: {}'.format(players[index], user_score[index]))
    elif user_hand > 21 or (21 >= dealer_hand > user_hand):
        user_score[index] -= 1
        print('{} loses! Score: {}'.format(players[index], user_score[index]))
    else:
        print('{} pushes. Score: {}'.format(players[index], user_score[index]))
