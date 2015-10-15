'''
Created on Sep 23, 2015

@author: daleinen
'''
from Deck import Deck
import time

class Game(object):

    def __init__(self, deck_num, table_min, start_amount, stop_amount, my_sessions):
        #instance variables
        self.game_deck_num = deck_num
        self.game_table_min = table_min
        self.game_start_amt = start_amount
        self.game_stop_amt = stop_amount
        self.game_sess_num = my_sessions
        
        self.runSessions()
        
    #function to run session amounts and simulate nights of gambling    
    def runSessions(self):
        start_time = time.time()
        session = self.game_sess_num
        my_sess= self.game_sess_num
        one_per = round(session * 0.04)
        count = 1

        #simulating a new 'night or session' of gambling
        while (session > 0):
            
            self.playBJ()
            
            if ((count % one_per) == 0):
                output = int(count/float(my_sess) * 100)
                print "*",
               
            count += 1
            session -=1
            
        total_time = time.time() - start_time
        self.printTime(total_time)
    
    #------------------------------------------------------------------------------------------#
        
    #function to simulate the start of actual game of blackack, simulating one night of gambling        
    def playBJ(self):
        
        deck = Deck(self.game_deck_num)
        deck.shuffleDeck()
        in_hand = True
        #print deck.printDeck(self.game_deck_num * 52)
        
        player_card1 = deck.dealCard(in_hand)
        dealer_card1 = deck.dealCard(in_hand)
        player_card2 = deck.dealCard(in_hand)
        dealer_card2 = deck.dealCard(in_hand)
        
         
        
    #------------------------------------------------------------------------------------------#    
       
    def printTime(self, total_time):
        my_time = "seconds"
        if (total_time > 60):
            total_time = total_time / 60
            my_time = "minutes"
        print "\n\n---Complete---"
        print "\nTotal time taken for program: %s %s" % (round(total_time, 2), my_time)
        
        