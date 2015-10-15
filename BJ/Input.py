'''
Created on Sep 23, 2015

@author: daleinen
'''

class Input(object):
    
    #function getting user input for number of decks
    def getNumDecks(self):
        dn = 0
        #user input for deck number must be 1-2-4-6-8
        while dn not in [1,2,4,6,8]:
            try:
                dn = int(raw_input("Please enter a number of decks(1,2,4,6,8): ")) 
            except:
                print ("\nPlease enter and integer value of 1,2,4,6,8 only")
        return dn
    
    #function getting user input for table minimum
    def getTableMin(self):
        tm = 0
        #user input for table minimum must be 5-10-15-25-50
        while tm not in [5,10,15,25,50]:
            try:
                tm = int(raw_input("Please enter a table min(5,10,15,25,50): ")) 
            except:
                print ("\nPlease enter and integer value of 5,10,15,25,50 only")
        return tm   
    
    #function getting iser input for starting amount
    def getStrAmnt(self):
        sa = 0
        #user input for start amount must be an int greater than zero
        while (sa <= 0):
            try:
                sa = int(raw_input("Please enter a starting amount: "))
            except:
                print ("Please enter a positive integer only")
        return sa
    
    #function getting user input for stoping amount 
    def getStpAmnt(self, sa):
        st = 0
        #user input for stop amount must be great than start amount
        while True:
            try:
                st = int(raw_input("Please enter a stop amount: "))
                if (st > sa):
                    break
            except:
                print ("\nValue must be greater than your start value")
        return st
    
    #function getting user input for gambling sessions
    def getSess(self):
        se = 0
        #user input for sessions must be an int greater than zero
        while (se <= 0):
            try:
                se = int(raw_input("Please enter number of gambling sessions: "))
            except:
                print ("\nValue must be great than zero")
        return se
                
                
                
