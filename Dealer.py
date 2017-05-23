import numpy as np
import Global
from Card import Card


class Dealer:

    """""
    This is the constructor for the Dealer class
    It will have an array of cards the dealer have
    An array of card that dealer use to distribute the card
    A number of deck to know how many deck to use
    """""
    def __init__(self, player, numberOfDeck):
        # Assume that maximum number of card is 22
        self.numberDeckUsed = numberOfDeck
        self.firstHandCard = []
        self.listOfPlayer = player
        self.theDeck = Card(numberOfDeck)
        self.bust = False
        self.stand = False

    # collects chips when player loses/busts   
    def collectChip(self):
        for i in self.listOfPlayer:
            if (i.bust == False and (np.sum(np.asarray(i.firstHandCard)) > np.sum(np.asarray(self.firstHandCard))))\
                    or (self.bust == True and i.bust == False):
                i.numOfChips += i.currentBet * 2
                if (i.confidenceLevel < 1.0):
                    i.confidenceLevel += i.confidenceLevel**4
                    if (i.confidenceLevel > 1.0):
                        i.confidenceLevel = 1.0
            else:
                if (np.sum(np.asarray(i.firstHandCard)) != np.sum(np.asarray(self.firstHandCard))):
                    i.numOfChips-= i.currentBet
                    if (i.confidenceLevel > 0.0):
                        i.confidenceLevel -= i.confidenceLevel**4
                        if (i.confidenceLevel < 0.0):
                            i.confidenceLevel = 0.0
    

    
    # the player asks the dealer to deal the card to the player.
    # hit is first initialized to false, for game initialization.
    def deal(self, hit, player):
        if(hit == True):   # player can request a card
            if (len(self.theDeck.listOfCard) < 2):
                self.theDeck = Card(self.numberDeckUsed)
                self.theDeck.shuffle()

            player.firstHandCard.append(self.theDeck.draw())
        else:          # used for initializing the game
            # For the number of players
            for i in self.listOfPlayer:
                
                # add two cards for every player
                if (len(self.theDeck.listOfCard) < 2):
                    self.theDeck = Card(self.numberDeckUsed)
                    self.theDeck.shuffle()
                i.firstHandCard.append(self.theDeck.draw())
                i.firstHandCard.append(self.theDeck.draw())
                
            # add two cards for the dealer
            if (len(self.theDeck.listOfCard) < 2):
                self.theDeck = Card(self.numberDeckUsed)
                self.theDeck.shuffle()
            self.firstHandCard.append(self.theDeck.draw())
            self.firstHandCard.append(self.theDeck.draw())
    
    # play method dealer uses play the game
    def play(self):
        
        # If playing with hard 17 rule
        if(Global.DEALER_SOFT_SEVENTEEN == False):
            
            # If the dealer does not stand, and is not bust
            while(self.stand == False and self.bust != True):
                
                # Dealer hits until the dealer has 17 or higher cards
                while(np.sum(np.asarray(self.firstHandCard)) < 17):
                    self.hit()
                    
                # If the dealer has over 21 cards, dealer busts otherwise stands.
                if(np.sum(np.asarray(self.firstHandCard)) > 21):
                    self.bust = True
                else:
                    self.stand = True
                    
        # If playing with soft 17 rule
        elif(Global.DEALER_SOFT_SEVENTEEN == True):
            
            # If the dealer does not stand, and is not bust
            while(self.stand == False and self.bust != True):
                
                # If dealer's hand is below 17
                if(np.sum(np.asarray(self.firstHandCard)) < 17):
                    
                    # Dealer hits until the dealer has 17 or higher cards
                    while(np.sum(np.asarray(self.firstHandCard)) < 17):
                        self.hit()
                        
                    # If dealer has an Ace in his hand, then he has to use the Ace
                    # with 1 value under Soft17 rule
                    for i in range(self.firstHandCard.__sizeof__()):
                        if (self.firstHandCard[i]==11):
                            self.firstHandCard[i] = 1
                            break;
                            
                # If the dealer has over 21 cards, dealer busts otherwise stands.
                if(np.sum(np.asarray(self.firstHandCard)) > 21):
                    self.bust = True
                else:
                    self.stand = True
                    
                    
    def hit(self):
        self.deal(True, self)


    """""
    Refresh means get rid of all cards the dealer and player having at the moment
    Also reset the boolean attributes indicating stand or bust of the dealer and players
    """""
    def refresh(self):
        self.firstHandCard = []
        self.bust = False
        self.stand = False
        for i in self.listOfPlayer:
            i.firstHandCard = []
            i.currentBet = 0
            i.stand = False
            i.bust = False
