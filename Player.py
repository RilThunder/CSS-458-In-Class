import Dealer.py as Deal
import Global.py as GL

class Player:


    """""
    This is the constructor for the Player class
    """""

    def __init__(self, theDealer):
        self.currentBet = GL.MIN_BET
        self.currentCards = []
        self.numOfChips = 0
        self.dealer = theDealer
        self.confidenceLevel = .5
        pass

    """""
    This is the hit method of the Player
    When the player call this, it will act like a hit in the casino
    """""
    def hit(self):
        currentCards = Deal.
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
    def stand(self):
        pass
