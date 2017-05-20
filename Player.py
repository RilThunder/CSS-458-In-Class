import numpy as np

class Player:


    """""
    This is the constructor for the Player class
    """""
    
    def __init__(self,Dealer):
        self.bust = False
        self.stand = False
        #self.currentBet = GLOBAL.MIN_BET
        self.currentCards = np.empty()
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
        pass


    """""
    This is the split method of the Player
    When the player call this, it will act like an actual split in the casino 
    """""
    def split(self):
        pass

    """""
    This is the stand method of the Player
    When the player call this, then the player will not receive more card and will be judged
    by the dealer
    """""
    def play(self):
        while(self.stand == False):
            while(np.sum(self.currentCards) < 17):
                self.hit()
            if(np.sum(self.currentCards) > 21):
                self.bust = True
            else:
                self.stand == True
    
        self.dealer.deal(True, self)
   
    def stand(self):
        pass
