import numpy as np


class Player:
    """""
    This is the constructor for the Player class
    """""

    def __init__(self, Dealer):
        self.bust = False
        self.stand = False
        # self.currentBet = GLOBAL.MIN_BET
        self.numberOfCard = []
        self.numOfChips = 0
        self.dealer = Dealer
        self.confidenceLevel = .5
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
        self.hit()
        self.stand = True
        pass

    """""
    This is the split method of the Player
    When the player call this, it will act like an actual split in the casino 
    """""

    def split(self):
        if len(self.numberOfCard) == 2 and self.numberOfCard[0] == self.numberOfCard[1]:
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

        # inside the loop, initially set to false and bust is not true initially.
        while (self.stand == False and self.bust != True):

            # The player will double when the card reach 11
            if np.sum(np.asarray(self.numberOfCard) == 11):
                self.double()
                if (np.sum(np.asarray(self.numberOfCard)) > 21):
                    self.bust = True
                break
                # checking to see if the sum of the current cards is less than 17
            # if it is then we hit.
            while (np.sum(np.asarray(self.numberOfCard)) < 17):
                # Maybe put a condition of when to double
                self.hit()
                # if the sum of the currecnt cards is more than 21
                # then we set bus = True. Or they stand.
            if (np.sum(np.asarray(self.numberOfCard)) > 21):
                self.bust = True
            else:
                self.stand = True
                # self.dealer.deal(True, self)
                
        
     
