import numpy as np
import Card
class Dealer:

    """""
    This is the constructor for the Dealer class
    It will have an array of cards the dealer have
    An array of card that dealer use to distribute the card
    A number of deck to know how many deck to use
    """""
    def __init__(self, player, numberOfDeck):
        # Assume that maximum number of card is 22
        self.numberOfCard= np.zeros(22)
        self.listOfPlayer = player
        self.theDeck = Card(numberOfDeck)

    # collects chips when player loses/busts   
    def collectChip(self):
        pass

    def payOutChip(self):
        pass



