import random

suits = ("Hearts","Diamonds","Clubs","Spades")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Jack","Queen","King","Ace")
vaules = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank 
        self.values = vaules[rank]
        
    def __str__(self):
        return self.rank + "of" + self.suit
    
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
            

class Hand:
    def __init__(self,name):
        self.name = name
        self.deck = []
        
    def remove_card(self):
        return self.deck.pop(0)
    
    def add_card(self):
        self.deck.append(Card)
        self.value+= vaules[Card.rank]
    
    def __str__(self):
        return f"The Player {self.name} has {len(self.deck)} cards."