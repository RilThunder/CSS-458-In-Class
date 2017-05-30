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
        # bust and stand are initially set to false.
        self.bust = False
        self.stand = False

    """""
    This method is used to collect chips from the player at the end of each round if he/she loses
    This method is also used to pay out chips to each player if he/she wins as well
    """""

    def collectChip(self):
        # If the player wins, give them the chip
        # In addition, increase their confidence Level (which will affect their betting)
        for i in self.listOfPlayer:
            # checking to see if the bust is false and first hand card of array is greater
            # than the sum of first hand card array.
            if (i.bust == False and (np.sum(np.asarray(i.firstHandCard)) > np.sum(np.asarray(self.firstHandCard)))) \
                    or (self.bust == True and i.bust == False):
                i.numOfChips += i.currentBet * 2
                if i.confidenceLevel < 1.0:
                    i.confidenceLevel += i.confidenceLevel ** 4
                    if i.confidenceLevel > 1.0:
                        i.confidenceLevel = 1.0
            else:
                # Player lose, time to take away their money
                # Checking the players confidence interval
                if np.sum(np.asarray(i.firstHandCard)) != np.sum(np.asarray(self.firstHandCard)):
                    i.numOfChips -= i.currentBet
                    if i.confidenceLevel > 0.0:
                        i.confidenceLevel -= i.confidenceLevel ** 4
                        if i.confidenceLevel < 0.0:
                            i.confidenceLevel = 0.0

    """""
       This method is used to deal the card to the Player and Dealer as well
       Depending on the parameter, this method will either hand out the card whenever the player hit
       Or distribute 2 cards to each player for each round
    """""

    # the player asks the dealer to deal the card to the player.
    # hit is first initialized to false, for game initialization.
    def deal(self, hit, player):
        # checking the length of the card.
        self.checkLengthCard()
        if hit == True:  # player can request a card

            if not player.bust:
                player.firstHandCard.append(self.theDeck.draw())
        else:  # used for initializing the game
            # For the number of players
            for i in self.listOfPlayer:
                # add two cards for every player
                # appending values to the first hand card.
                self.checkLengthCard()
                i.firstHandCard.append(self.theDeck.draw())
                i.firstHandCard.append(self.theDeck.draw())

            # add two cards for the dealer
            # appending values to the frist hadn card
            self.checkLengthCard()
            self.firstHandCard.append(self.theDeck.draw())
            self.firstHandCard.append(self.theDeck.draw())
        self.checkLengthCard()

    """"
    This method is used to check if the dealer has sufficient card
    IF the dealer does not have sufficient card, then a new card deck is generated
    """""

    def checkLengthCard(self):
        # checks the length of the card, to see if it is greater than 2
        # since there are two cards. 
        # Call the shuffle method to shuffle the deck
        if len(self.theDeck.listOfCard) < 2:
            self.theDeck = Card(self.numberDeckUsed)
            self.theDeck.shuffle()  

    """"
    This is the way the dealer will play.
    The dealer will hit until he or she reach greater than or equal 17 
    The dealer's way to play depends 
    """""

    # play method dealer uses play the game
    def play(self):

        # If playing with hard 17 rule
        if Global.DEALER_SOFT_SEVENTEEN == False:

            # If the dealer does not stand, and is not bust
            while self.stand == False and self.bust != True:

                # Dealer hits until the dealer has 17 or higher cards
                while np.sum(np.asarray(self.firstHandCard)) < 17:
                    self.hit()

                # If the dealer has over 21 cards, dealer busts otherwise stands.
                if np.sum(np.asarray(self.firstHandCard)) > 21:
                    self.bust = True
                else:
                    self.stand = True

        # If playing with soft 17 rule
        elif Global.DEALER_SOFT_SEVENTEEN == True:

            # If the dealer does not stand, and is not bust
            while self.stand == False and self.bust != True:

                # If dealer's hand is below 17


                # Dealer hits until the dealer has 17 or higher cards
                while np.sum(np.asarray(self.firstHandCard)) < 17:
                    self.hit()

                    # If dealer has an Ace in his hand, then he has to use the Ace
                    # with 1 value under Soft17 rule
                for i in range(np.size(np.asarray(self.firstHandCard))):
                    if self.firstHandCard[i] == 11:
                        self.firstHandCard[i] = 1

                # If the dealer has over 21 cards, dealer busts otherwise stands.
                if np.sum(np.asarray(self.firstHandCard)) > 21:
                    self.bust = True
                else:
                    self.stand = True

    """""
    This is similar to the hit method of the Player in which the dealer will deal himself/herself card
    """""
    
    # Dealer will hit card based on the scenario
    def hit(self):
        self.deal(True, self)

    """""
    Refresh can also be called as clear which means, get rid of all cards the 
    dealer and player having at the moment Also reset the boolean attributes 
    indicating stand or bust of the dealer and players
    """""

    def refresh(self):
        self.firstHandCard = []
        self.bust = False
        self.stand = False
        for i in self.listOfPlayer:
            i.firstHandCard = []
            i.stand = False
            i.bust = False
