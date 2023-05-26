# Use randint to generate random cards.
from blackjack_helper import *

# NUMBER OF PLAYERS
num_players = int(input("Welcome to Blackjack! How many players? "))

# PLAYERS INFORMATION
players = []
user_score = []
for i in range(1, num_players + 1):
    players_name = input("What is player {}'s name? ".format(i))
    players.append(players_name)
    user_score.append(3)

# FULL GAME
another_game = 'y'
while another_game == 'y':
    # USERS GAME
    hand_totals = []
    for player in players:
        user_hand = draw_starting_hand(player)
        should_hit = 'y'
        while user_hand < 21:
            should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
            if should_hit == 'n':
                break
            elif should_hit != 'y':
                print("Sorry I didn't get that.")
            else:
                user_hand = user_hand + draw_card()
        hand_totals.append(user_hand)
        print_end_turn_status(user_hand)

    # DEALER's GAME
    dealer_hand = draw_starting_hand("DEALER")
    while dealer_hand < 17:
        print("Dealer has {}.".format(dealer_hand))
        dealer_hand = dealer_hand + draw_card()
    print_end_turn_status(dealer_hand)

    # GAME RESULT
    index = 0
    another_players = players.copy()
    print_header('GAME RESULT')
    for user_hand in hand_totals:
        print_end_game_status(user_hand, dealer_hand, players, index, hand_totals, user_score)
        if user_score[index] == 0:
            print("{} eliminated!".format(players[index]))
            another_players.remove(players[index])
        index += 1
    players = another_players
    score_copy = user_score.copy()
    for score in score_copy:
        if score == 0:
            user_score.remove(score)
    if len(user_score) < 1:
        print("All players eliminated!")
        break
    another_game = input("Do you want to play another hand (y/n)? ")
