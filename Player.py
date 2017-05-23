import numpy as np
import Global

class Player:
    """""
    This is the constructor for the Player class
    """""

    def __init__(self, Dealer):
        self.bust = False
        self.stand = False
        self.currentBet = Global.BUY_IN
        self.firstHandCard = []
        self.numOfChips = Global.STARTING_CHIPS
        self.dealer = Dealer
        self.confidenceLevel = .5
        self.secondHandCard = []
        pass

    """""
    This is the hit method of the Player
    When the player call this, it will act like a hit in the casino
    """""

    def hit(self):
        self.dealer.deal(True, self)
        pass

    """""
    This is the double method of the Player
    When the player call this, it will act like a double in the casino
    """""

    def double(self):
        self.currentBet = Global.BUY_IN * 2
        self.hit()
        self.stand = True
        pass

    """""
    This is the split method of the Player
    When the player call this, it will act like an actual split in the casino 
    """""

    def split(self):
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

    def play(self):
        self.currentBet = Global.BUY_IN
        # inside the loop, initially set to false and bust is not true initially.
        while (self.stand == False and self.bust != True):


            # Need to stop after double. In this loop, still draw after double

            # The player will double when the card reach 11
            if np.sum(np.asarray(self.firstHandCard) == 11):
                self.double()
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
                
        
     
