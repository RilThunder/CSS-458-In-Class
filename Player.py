import random

import numpy as np

import Global


class Player:
    """""
    This is the constructor for the Player class.
    All variables to be used for the player is initialized here.
    """""

    def __init__(self, Dealer, wayToPlay):
        self.bust = False
        self.stand = False
        self.currentBet = Global.BUY_IN
        self.firstHandCard = []
        self.numOfChips = Global.STARTING_CHIPS
        self.dealer = Dealer
        self.confidenceLevel = Global.BASE_CONFIDENT
        self.choice = wayToPlay
        self.didDouble = False

        pass

    """""
    This is the hit method of the Player.
    When the player call this, dealer will deal the card to the player.
    """""

    def hit(self):
        self.dealer.deal(True, self)
        pass

    """""
    This is the double method of the Player
    When the player call this, it will act like a double in the casino.
    Have to decide probability. 
    """""

    def double(self):
        # player's probability of choosing to double down
        # In our simulation we are going to double between 9 to 11 inclusive.

        sum = np.sum(np.asarray(self.firstHandCard))
        if sum >= 9 and sum <= 11:
            self.didDouble = True
            self.currentBet = self.currentBet * 2
        self.stand = True




    """""
    This is the stand method of the Player
    When the player call this, then the player will not receive more card and will be judged
    by the dealer. 
    """""

    def playNormal(self):
        self.makeTheBet()  # inside the loop, initially set to false and bust is not true initially.
        while (self.stand == False and self.bust != True):
            # The player will double when the sum of card is in the range 9 - 11
            self.dealer.checkLengthCard()
            if np.sum(np.asarray(self.firstHandCard)) <= 11 and np.sum(np.asarray(self.firstHandCard)) >= 9:
                self.double()
                self.hit()
                if (np.sum(np.asarray(self.firstHandCard)) > 21):
                    self.bust = True
                break
                # checking to see if the sum of the current cards is less than 17
            # if it is then we hit.
            while (np.sum(np.asarray(self.firstHandCard)) < 17 and self.stand == False):
                # Maybe put a condition of when to double
                self.dealer.checkLengthCard()
                self.hit()
                # if the sum of the currecnt cards is more than 21
                # then we set bus = True. Or they stand.
                if np.sum(np.asarray(self.firstHandCard) > 21):
                    for i in range(np.size(np.asarray(self.firstHandCard))):
                        if self.firstHandCard[i] == 11:
                            self.firstHandCard[i] = 1
                            break

                if (np.sum(np.asarray(self.firstHandCard)) > 21):
                    self.bust = True
                else:
                    # Should not stand when after drawing one card and the total card
                    # is still less than 17
                    if (np.sum(np.asarray(self.firstHandCard) < 17)):
                        continue
                    else:
                        self.stand = True
                        # self.dealer.deal(True, self)

    """
    This method is used to determine how much the player will bet for each round
    Depending on the confidence level, the player will bet more or less
    """
    def makeTheBet(self):
        if (self.confidenceLevel > .5 and self.currentBet < Global.MAX_BET):
            self.currentBet += round(self.currentBet * (self.confidenceLevel - .5))

        elif (self.confidenceLevel < .5 and self.currentBet > Global.BUY_IN):
            self.currentBet -= round(self.currentBet * (.5 - self.confidenceLevel))
        if (self.currentBet < Global.BUY_IN):
            self.currentBet = Global.BUY_IN
        if (self.currentBet > Global.MAX_BET):
            self.currentBet = Global.MAX_BET

    """ 
    This method will pick the way the player will play
    Either by playing with odss, play with random or play in a normal way 
    and will continue it until the player stand or bust 
    """

    def play(self):
        if np.sum(np.asarray(self.firstHandCard) > 21):
            for i in range(np.size(np.asarray(self.firstHandCard))):
                if self.firstHandCard[i] == 11:
                    self.firstHandCard[i] = 1
                    break


        if self.choice == 1:
            self.playWithOdds()
        else:
            if self.choice == 2:
                self.playWithRandom()
            else:
                self.playNormal()

    """
    Play with random makes player to act randomly without any constraints.
    This is determined by a probability
    It is like flipping a coin. <= 0.5 then the player will hit, else the player will stand
    """

    def playWithRandom(self):
        self.makeTheBet()
        while (self.stand == False and self.bust != True):
            self.dealer.checkLengthCard()
            choice = random.random()
            if choice <= Global.CHANCE_TO_HIT:
                self.hit()
                # Should we double ? There is a 0.25 chance that we will double
                newChoice = random.random()
                if newChoice <= Global.CHANCE_TO_DOUBLE:
                    self.double()
                    self.hit()
            else:
                self.stand = True
            if np.sum(np.asarray(self.firstHandCard) > 21):
                for i in range(np.size(np.asarray(self.firstHandCard))):
                    if self.firstHandCard[i] == 11:
                        self.firstHandCard[i] = 1
                        break
            if (np.sum(np.asarray(self.firstHandCard)) > 21):
                self.bust = True

    """
    Play with odds by determining what cards are left and picking a choice based on the
    probablity
    """

    def playWithOdds(self):
        self.makeTheBet()

        # inside the loop, initially set to false and bust is not true initially.
        while (self.stand == False and self.bust != True):
            # Need to check if busted as well. If busted then 21 - totalValue will be negative
            # Calculating the remaning cards to determine the probabiltity
            self.dealer.checkLengthCard()
            totalValue = np.sum(np.asarray(self.firstHandCard))
            remainingWeNeed = 21 - totalValue
            lengthOfTotal = np.size(self.dealer.theDeck.listOfCard)
            if (lengthOfTotal == 0):
                print('Check')
            count = 0.0
            for i in self.dealer.theDeck.listOfCard:
                if i <= remainingWeNeed:
                    count += 1
            probWeShouldContinue = count / lengthOfTotal
            choice = random.random()
            sum = np.sum(np.asarray(self.firstHandCard))
            # if the probability is greater than or eqault to the choice then
            # the player continues to hit or if not then they will stand. 
            if probWeShouldContinue >= choice:
                if sum >= 9 and sum <= 11:
                    self.double()
                self.hit()
            else:
                self.stand = True
            if np.sum(np.asarray(self.firstHandCard) > 21):
                for i in range(np.size(np.asarray(self.firstHandCard))):
                    if self.firstHandCard[i] == 11:
                        self.firstHandCard[i] = 1
                        break
            if (np.sum(np.asarray(self.firstHandCard)) > 21):
                self.bust = True
