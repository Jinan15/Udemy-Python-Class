import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
            'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}

playing = True

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.deck = []
        # 8 decks in a standard deck in blackjack
        for i in range(8):
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def create_starting_hand(self, deck):
        self.add_cards(deck.deal())
        self.add_cards(deck.deal())

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Person():
    def __init__(self, total = 0):
        self.Hands = []
        if total != 0:
            self.total = total
            self.bet = 0

    def create_hand(self):
        self.Hands.append(Hand())

    def split_hand(self, deck):
        self.create_hand()
        self.create_hand()
        temp = self.Hands.pop(0)
        self.Hands[0].add_cards(temp.cards[0])
        self.Hands[0].add_cards(deck.deal())
        self.Hands[1].add_cards(temp.cards[1])
        self.Hands[1].add_cards(deck.deal())

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
