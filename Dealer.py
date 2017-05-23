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
            else:
                if (np.sum(np.asarray(i.firstHandCard)) != np.sum(np.asarray(self.firstHandCard))):
                    i.numOfChips-= i.currentBet
    

    
    # the player asks the dealer to deal the card to the player.
    # hit is first initialized to false, for game initialization.
    def deal(self, hit, player):
        if(hit == True):   # player can request a card
            if (len(self.theDeck.listOfCard) < 2):
                self.theDeck = Card(self.numberDeckUsed)
                self.theDeck.shuffle()
            player.firstHandCard.append(self.theDeck.draw())
        else:          # used for initializing the game
            for i in self.listOfPlayer:
                if (len(self.theDeck.listOfCard) < 2):
                    self.theDeck = Card(self.numberDeckUsed)
                    self.theDeck.shuffle()
                # add two cards for every player
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
        if(Global.DEALER_SOFT_SEVENTEEN == False):
            while(self.stand == False and self.bust != True):
                while(np.sum(np.asarray(self.firstHandCard)) < 17):
                    self.hit()
                if(np.sum(np.asarray(self.firstHandCard)) > 21):
                    self.bust = True
                else:
                    self.stand = True
        elif(Global.DEALER_SOFT_SEVENTEEN == True):
            while(self.stand == False and self.bust != True):
                if(np.sum(np.asarray(self.firstHandCard)) < 17):
                    while(np.sum(np.asarray(self.firstHandCard)) < 17):
                        self.hit()
                    for i in range(self.firstHandCard.__sizeof__()):
                        if (self.firstHandCard[i]==11):
                            self.firstHandCard[i] = 1
                            break;
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
