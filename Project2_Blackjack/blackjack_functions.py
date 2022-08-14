from blackjack_classes import *

suits = {'Hearts':'♥', 'Diamonds':'♦', 'Spades':'♣', 'Clubs':'♠'}
ranks = {'Two':'2', 'Three':'3', 'Four':'4', 'Five':'5', 'Six':'6', 'Seven':'7', 'Eight':'8',
            'Nine':'9', 'Ten':'10', 'Jack':'J', 'Queen':'Q', 'King':'K', 'Ace': 'A'}

def make_card(card):
    pcarddisplay = [] 
    pcarddisplay.append("┌─────────┐")
    pcarddisplay.append("│{}{}. . .│")
    pcarddisplay.append("│. . . . .│")
    pcarddisplay.append("│. . . . .│")
    pcarddisplay.append("│. . {}. .│")
    pcarddisplay.append("│. . . . .│")
    pcarddisplay.append("│. . . . .│")
    pcarddisplay.append("│. . .{}{}│")
    pcarddisplay.append("└─────────┘")

    if card.rank == 'Ten':
        top = ("│", ranks[card.rank], ". . . .│")
        pcarddisplay[1] = "".join(top)

        bottom = ("│. . . .", ranks[card.rank], "│")
        pcarddisplay[7] = "".join(bottom)
    else:
        top = ("│.", ranks[card.rank], ". . . .│")
        pcarddisplay[1] = "".join(top)

        bottom = ("│. . . .", ranks[card.rank], ".│")
        pcarddisplay[7] = "".join(bottom)

    if card.suit == "Diamonds":
        pcarddisplay[4] = "│. . ♦ . .│"
    if card.suit == "Clubs":
        pcarddisplay[4] = "│. . ♣ . .│"
    if card.suit == "Hearts":
        pcarddisplay[4] = "│. . ♥ . .│"
    if card.suit == "Spades":
        pcarddisplay[4] = "│. . ♠ . .│"

    return pcarddisplay

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
        player_input = input("Would you like to surrender (Y for yes or N for no)? ")
        if player_input[0].lower() == 'y':
            player.total -= int(player.bet/2)
            return True
        elif player_input[0].lower() == 'n':
            return False
        else:
            print("Invalid input! Please input Y for yes or N for no")

def split(player, hand_pos):
    if player.Hands[hand_pos].cards[0].value == player.Hands[hand_pos].cards[1].value:
        while True:
            player_input = input("Would you like to split (Y for yes or N for no)? ")
            if player_input[0].lower() == 'y':
                if player.total > player.bet * 2:
                    return True
                else:
                    print("Insufficient chips, only allowed to play single hand")
                    return False
            elif player_input[0].lower() == 'n':
                return False
            else:
                print("Invalid input! Please input Y for yes or N for no")
    else:
        return False

def show_some(player_hand, dealer_hand):
    print()
    print("Dealer's Hand")
    print('-----------------------------------')
    print("First card hidden")
    print('\n'.join(map('  '.join, zip((make_card(dealer_hand.cards[1]))))))
    print('-----------------------------------')
    print("Player's Hand")
    print('-----------------------------------')
    print('\n'.join(map('  '.join, zip(*(make_card(c) for c in player_hand.cards)))))
    # print(*player_hand.cards, sep=', ')
    print('-----------------------------------\n')

def show_all(player_hand, dealer_hand):
    print("-----------------------------------")
    print("Game finished")
    print("-----------------------------------")
    print("Dealer's Hand: ")
    print('\n'.join(map('  '.join, zip(*(make_card(c) for c in dealer_hand.cards)))))

    print("Value of Dealer's hand is: {}".format(dealer_hand.value))

    print("\nPlayer's Hand: ")
    print('\n'.join(map('  '.join, zip(*(make_card(c) for c in player_hand.cards)))))

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
