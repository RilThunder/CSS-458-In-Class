import numpy as np
import Card import Card
import Player
class Dealer:

    """""
    This is the constructor for the Dealer class
    It will have an array of cards the dealer have
    An array of card that dealer use to distribute the card
    A number of deck to know how many deck to use
    """""
    def __init__(self, player, numberOfDeck):
        # Assume that maximum number of card is 22
        self.numberOfCard = []
        self.listOfPlayer = player
        self.theDeck = Card(numberOfDeck)
        self.bust = False
        self.stand = False

    # collects chips when player loses/busts   
    def collectChip(self):
        pass
    
    # When the player win, the player will receive betAmount*2
    def payOutChip(self):
        pass
    
    # the player asks the dealer to deal the card to the player.
    # hit is first initialized to false, for game initialization.
    def deal(self, hit, player):
        if(hit == True):   # player can request a card
            player.numberOfCard.append(self.theDeck.draw())
        else:          # used for initializing the game
            for i in self.listOfPlayer:
                # add two cards for every player
                i.numberOfCard.append(self.theDeck.draw())
                i.numberOfCard.append(self.theDeck.draw())
            # add two cards for the dealer
            self.numberOfCard.append(self.theDeck.draw())
            self.numberOfCard.append(self.theDeck.draw())
    
    # play method dealer uses play the game
    def play(self):
        while(self.stand == False and self.bust != True):
            while(np.sum(np.asarray(self.numberOfCard)) < 17):
                self.hit()
            if(np.sum(np.asarray(self.numberOfCard)) > 21):
                self.bust = True
            else:
                self.stand = True
                 
    def hit(self):
        self.deal(True, self)
