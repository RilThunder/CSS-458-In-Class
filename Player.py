import numpy as np
import Global
import random
class Player:
    
    """""
    This is the constructor for the Player class.
    All variables to be used for the player is initialized here.
    """""
    def __init__(self, Dealer):
        self.bust = False
        self.stand = False
        self.currentBet = Global.BUY_IN
        self.firstHandCard = []
        self.numOfChips = Global.STARTING_CHIPS
        self.dealer = Dealer
        self.confidenceLevel = .5
        self.secondHandCard = []          # secondhand used for the split()
        self.choice = 3
        self.split = False
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
        # In our simulation we are going to double between 9 to 11 inclusive.
        self.currentBet = Global.BUY_IN * 2
        self.didDouble = True
        self.stand = True
        pass


    """""
    Implement play method for the split.
    """""
    def play_split(self):
        pass

    """""
    This is the split method of the Player
    When the player call this, it will act like an actual split in the casino 
    """""
    def split(self):
        # Checks to see if the length of the card is 2 and if the index value 
        # of the card at 0 is equalt to the index value of card at 1. 
        if len(self.firstHandCard) == 2 and self.firstHandCard[0] == self.firstHandCard[1]:
            self.secondHandCard.append(self.firstHandCard[1])
            self.firstHandCard.remove(self.firstHandCard[1])
            return True
        else:
            False
        pass
  
              
    
    """""
    This is the stand method of the Player
    When the player call this, then the player will not receive more card and will be judged
    by the dealer. 
    """""
    def playNormal(self):
        if(self.confidenceLevel > .5 and self.currentBet < Global.MAX_BET):
            self.currentBet += round(self.currentBet * (self.confidenceLevel - .5))
            
        elif(self.confidenceLevel < .5 and self.currentBet > Global.BUY_IN):
            self.currentBet -= round(self.currentBet * (.5 - self.confidenceLevel))
        if(self.currentBet < Global.BUY_IN):
            self.currentBet = Global.BUY_IN
        if(self.currentBet > Global.MAX_BET):
            self.currentBet = Global.MAX_BET
        # inside the loop, initially set to false and bust is not true initially.
        while (self.stand == False and self.bust != True):

            # The player will double when the card reach 11
            if np.sum(np.asarray(self.firstHandCard) == 11):
                self.double()
                self.hit()
                if (np.sum(np.asarray(self.firstHandCard)) > 21):
                    self.bust = True
                break
                # checking to see if the sum of the current cards is less than 17
            # if it is then we hit.
            while (np.sum(np.asarray(self.firstHandCard)) < 17 and self.stand == False):
                # Maybe put a condition of when to double
                self.hit()
                # if the sum of the currecnt cards is more than 21
                # then we set bus = True. Or they stand.
            if (np.sum(np.asarray(self.firstHandCard)) > 21):
                self.bust = True
            else:
                self.stand = True
                # self.dealer.deal(True, self)

   
    
    
  # This play functions allow the player to choose if they want to play by the
 # odds, random or Normal.  
    def play(self):
        if self.choice == 1:
            self.playWithOdds()
        else:
            if self.choice ==2:
                self.playWithRandom()
            else:
                self.playNormal()

    """
    Play with random makes player to act randomly without any constraints.
    """
    def playWithRandom(self):
        pass


    """
    Play with odds by determining what cards are left and picking a choice based on the
    probablity
    """
    def playWithOdds(self):
        self.currentBet = Global.BUY_IN
        # inside the loop, initially set to false and bust is not true initially.
        while (self.stand == False and self.bust != True):
        # Need to check if busted as well. If busted then 21 - totalValue will be negative


            # Calculating the remaning cards to determine the probabiltity

            totalValue = np.sum(np.asarray(self.firstHandCard))
            remainingWeNeed = 21 - totalValue
            lengthOfTotal = np.size(self.dealer.firstHandCard)
            count = 0.0
            for i in self.dealer.firstHandCard:
                if i <= remainingWeNeed:
                    count+=1
            probWeShouldContinue = count/lengthOfTotal
            choice = random.random()
            # if the probability is greater than or eqault to the choice then
            # the player continues to hit or if not then they will stand. 
            if probWeShouldContinue >= choice:

                self.hit()
            else:
                self.stand = False
                continue

     
