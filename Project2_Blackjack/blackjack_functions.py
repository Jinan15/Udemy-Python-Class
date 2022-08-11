from blackjack_classes import *

def get_total_chips():
    ret = 0
    while True:
        try:
            ret = int(input("How many chips do you have? "))
        except:
            print("Sorry please provide an integer")
        else:
            if ret <= 0:
                print("Please enter a number higher than 0")
            else:
                return ret

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed {}".format(chips.total))
            else:
                break

def hit(deck, player_hand):
    single_card = deck.deal()
    player_hand.add_cards(single_card)
    player_hand.adjust_for_ace()

def hit_or_stand(deck, player_hand, dealer_hand):
    playing = True
    turn = True
    while playing:
        while turn:
            x = input('Hit or Stand? Enter h or s: ')

            if x[0].lower() == 'h':
                hit(deck, player_hand)
                turn = False
            elif x[0].lower() == 's':
                print("\nPlayer Stands Dealer's Turn")
                return
            else:
                print("Sorry, please try again")
                continue
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            return
        turn = True
    return

def surrender(player):
    while True:
        player_input = input("Would you like to surrender (Yes or No)? ")
        if player_input.lower() == 'yes':
            player.total -= int(player.bet/2)
            return True
        elif player_input.lower() == 'no':
            return False
        else:
            print("Invalid input! Please input yes or no")

def split(player, hand_pos):
    if player.Hands[hand_pos].cards[0].value == player.Hands[hand_pos].cards[1].value:
        while True:
            player_input = input("Would you like to split (Yes or No)? ")
            if player_input.lower() == 'yes':
                if player.total > player.bet * 2:
                    return True
                else:
                    print("Insufficient chips, only allowed to play single hand")
                    return False
            elif player_input.lower() == 'no':
                return False
            else:
                print("Invalid input! Please input yes or no")
    else:
        return False

def show_some(player_hand, dealer_hand):
    print()
    print("Dealer's Hand")
    print('-----------------------------------')
    print("First card hidden, {}".format(dealer_hand.cards[1]))
    print('-----------------------------------\n')
    print("Player's Hand")
    print('-----------------------------------')
    print(*player_hand.cards, sep=', ')
    print('-----------------------------------\n')

def show_all(player_hand, dealer_hand):
    print("Dealer's Hand: ")
    for card in dealer_hand.cards:
        print(card)

    print("Value of Dealer's hand is: {}".format(dealer_hand.value))

    print("\nPlayer's Hand: ")
    for card in player_hand.cards:
        print(card)

    print("Value of Player's hand is: {}".format(player_hand.value))


def player_busts(player):
    print("BUST PLAYER!")
    player.lose_bet()

def player_wins(player):
    print("PLAYER WINS!")
    player.win_bet()

def dealer_busts(player):
    print("PLAYER WINS! DEALER BUSTED")
    player.win_bet()

def dealer_wins(player):
    print("DEALER WINS!")
    player.lose_bet()

def push(player):
    print('Dealer and player tie! PUSH')
