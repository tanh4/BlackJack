#!/usr/bin/python3

import random
from Card import CardValue
from Card import Card

class Deck:
    def __init__(self):
        self.deck = []
        for cardName in CardValue:
            self.deck.append(Card(cardName))
        
        self.deck = self.deck * 4

    def shuffle(self):
        random.shuffle(self.deck)

    def nextCard(self):
        return self.deck.pop()

    def __str__(self):
        return str(self.deck)


if __name__ == "__main__":
    deck = Deck()
    deckValue = str(deck)
    #print(deckValue)