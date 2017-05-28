import numpy as np
class Card:

    """""
    The constructor for the Card class
    parameter: numberOfDeck How many deck should this card class have
    A Deck is 52 cards so total cards will be 52 * numberOfDeck  
    """""
    def __init__(self, numberOfDeck):
        # creatr an array list of cards
        self.listOfCard = []
        for i in range(numberOfDeck):
            for numberOfSuit in range(4):
                # Add the card from 2 - 10
                for cardInSuit in range(2,11):
                    self.listOfCard.append(cardInSuit)
                # Add King, Queen Jack:
                for specialCard in range(3):
                    self.listOfCard.append(10)
                # Add Ace, the special value will be 11. The player see this will decide
                self.listOfCard.append(11)
        self.listOfCard = np.asarray(self.listOfCard)

    """""
    This method is used to shuffle the array of card
    """""
    def shuffle(self):
        # Use Numpy Random Shuffle to shuffle the list of cards
        np.random.shuffle(self.listOfCard)




    """""
    This method is used to draw the next card from the array of card
    It will remove that card and return the value of the card
    """""
    def draw(self):
        # Get the next card
        value = self.listOfCard[0]
        
        # Delete that card and create a new array of the old one with the missing of the card
        self.listOfCard = np.delete(self.listOfCard,0)
        return value
