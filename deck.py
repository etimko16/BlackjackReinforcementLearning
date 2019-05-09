# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:37:53 2019

@author: Emily
"""     

import random

class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def getValue(card):
        rank = card.rank
        if rank == "J" or rank == "Q" or rank == "K":
            return 10
        elif rank == "A":
            return 11
        else:
            return int(rank, 10)
        
class Deck:
    
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        cards = [None] * 52
        i = 0
        for x in range(13):
            for y in range(4):
                cards[i] = Card(ranks[x], suits[y])
                i += 1
        self.cards = cards
    
    def drawCard(deck):
        card = deck.cards[random.randint(0,(len(deck.cards)-1))]
        Deck.removeCard(card, deck)
        return card

    def removeCard(card, deck):
        for x in range(len(deck.cards) -1):
            if deck.cards[x] == card:
                deck.cards.remove(deck.cards[x])
                return deck