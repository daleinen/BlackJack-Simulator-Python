'''
Created on Sep 23, 2015

@author: daleinen
'''

from Input import Input
from Game import Game
    
#printing a welcome message
welcome_message = "\nWelcome to JackBlack's BlackSnake BlackJack Simulator 1.0!\n"
print(welcome_message)

#instance of input class
my_input = Input()

#while true loop to gather user inputs
while True:
    #getting and setting user variables
    deck_num = my_input.getNumDecks()
    table_min = my_input.getTableMin()
    start_amount = my_input.getStrAmnt()
    stop_amount = my_input.getStpAmnt(start_amount)
    my_sessions = my_input.getSess()
    
    print "\nAre these amounts correct?"
    print "Deck number: %s" % (deck_num)
    print "Table min: %s" % (table_min)
    print "Start amount: %s" % (start_amount)
    print "Stop amount: %s" % (stop_amount)
    print "Sessions: %s" % (my_sessions)
    
    #confirm with that user entered variables are correct
    user_confirm = str(raw_input("Okay to start program?(y/n): "))
    if (user_confirm.upper() == "Y"):
        print "\nThis may take several minutes\nProcessing\n"
        break
    else:
        print "\nEnter amounts again,"

#creating instance of game class and running out sessions
Game(deck_num, table_min, start_amount, stop_amount, my_sessions)