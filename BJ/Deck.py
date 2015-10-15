'''
Created on Sep 29, 2015

@author: daleinen
'''
from random import shuffle

class Deck(object):
    
    def __init__(self, deck_num):
        
        #instance variables
        self.game_deck = []
        self.num_cards = 0
        self.cards_used = 0
        self.shuffle_later = True
        self.createGameDeck(deck_num)
    
    #function to create game deck            
    def createGameDeck(self, deck_num):
        #adding 10 valued cards
        for _ in range(0, deck_num * 16):
            self.game_deck.append(10)
            
        #adding non ten valued cards
        for _ in range(0, deck_num * 4):
            #adding values 1-9, aces being 1
            for i in range(1, 10):
                self.game_deck.append(i)

    #function for shuffling the deck       
    def shuffleDeck(self):
        #shuffling deck 3 times
        for _ in range(3):
            shuffle(self.game_deck)
        #simulates cut card
        self.cards_used = 1
     
    #function for dealing a card   
    def dealCard(self, in_hand):
        #simulates the cut card at 75% penetration
        if (self.cards_used == self.num_cards * .75 and in_hand == True):
            self.shuffle_later = True
        elif (self.cards_used == self.num_cards * .75 and in_hand == False):
            self.shuffleDeck()
            
        self.cards_used += 1
        return self.game_deck[self.cards_used - 1]
    
    #function for checking for shuffle        
    def shuffleCheck(self):
        #shuffle the deck only if flaged to do so
        if self.shuffle_later == True:
            self.shuffleDeck()
            self.shuffle_later = False
    
    #function to print the deck, mostly for error checking        
    def printDeck(self, print_num):
        #printing all cards in deck
        for i in range(0, print_num):
            print str(self.game_deck[i]),"\t@index", str(i)
        return "---" 
        