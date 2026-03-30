import random

suits = ("Hearts","Diamonds","Clubs","Spades")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Jack","Queen","King","Ace")
vaules = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank 
        self.values = vaules[rank]
        
    def __str__(self):
        return self.rank + "of" + self.suit

    def __gt__(self, other):
        return self.value > other.value # Player 1 card > Player 2 card
    
    def __lt__(self, other):
        return self.value < other.value # Player 2 card > Player 1 card
    
    def __eq__(self, other):
        return self.value == other.value
    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal_one(self):
        return self.deck.pop()
            

class Player:
   def __init__(self,name):
        self.name = name
        self.deck = []
        self.value = 0
        
    def remove_card(self):
        return self.deck.pop(0)
    
    def add_card(self,card):
        self.deck.append(card)
        self.value += vaules[card.rank]
    
    def __str__(self):
        return f"The Player {self.name} has {len(self.deck)} cards."
