from blackjack_classes import *
from blackjack_functions import *

print('-----------------------------------')
print("WELCOME TO BLACKJACK")
print('-----------------------------------')

# Create deck
deck = Deck()

total_chips = get_total_chips()

while True:
    hand_pos = 0
    # Shuffle deck
    deck.shuffle()

    # Deal cards
    player1 = Person(total_chips)
    player1.create_hand()
    player1.Hands[hand_pos].create_starting_hand(deck)

    dealer = Person()
    dealer.create_hand()
    dealer.Hands[hand_pos].create_starting_hand(deck)

    # Get player bet
    take_bet(player1)
    # Show all player cards but only 1 dealer card
    show_some(player1.Hands[0], dealer.Hands[0])

    # If player surrenders, return half the bet
    if surrender(player1):
        print("Player surrendered, half the bet is returned")
    else:
        # If a split is available and player says yes to split hand
        # Player plays both hands
        if split(player1, hand_pos):
            player1.split_hand(deck)
            for i in range(2):
                show_some(player1.Hands[i], dealer.Hands[0])
                hit_or_stand(deck, player1.Hands[i], dealer.Hands[0])

            while dealer.Hands[0].value < 17:
                hit(deck, dealer.Hands[0])

            for i in range(2):
                if player1.Hands[i].value <= 21:
                    show_all(player1.Hands[i], dealer.Hands[0])

                    if dealer.Hands[0].value > 21:
                        dealer_busts(player1)
                    elif dealer.Hands[0].value > player1.Hands[i].value:
                        dealer_wins(player1)
                    elif dealer.Hands[0].value < player1.Hands[i].value:
                        player_wins(player1)
                    else:
                        push(player1)
                else:
                    player_busts(player1)
                print()
        # If split is not available or player says no split, play single hand
        else:
            hit_or_stand(deck, player1.Hands[0], dealer.Hands[0])

            if player1.Hands[hand_pos].value <= 21:
                while dealer.Hands[0].value < 17:
                    hit(deck, dealer.Hands[0])

                show_all(player1.Hands[0], dealer.Hands[0])

                if dealer.Hands[0].value > 21:
                    dealer_busts(player1)
                elif dealer.Hands[0].value > player1.Hands[hand_pos].value:
                    dealer_wins(player1)
                elif dealer.Hands[0].value < player1.Hands[hand_pos].value:
                    player_wins(player1)
                else:
                    push(player1)
            else:
                player_busts(player1)

    print("\nPlayer total chips are at: {}".format(player1.total))

    if total_chips <= 0:
        print("Player ran out of chips! Better luck next time!")
        break

    new_game = input("Would you like to play again? y/n: ")

    if new_game[0].lower() == 'y':
        total_chips = player1.total
        continue
    else:
        print("Thank you for playing!")
        break








#
