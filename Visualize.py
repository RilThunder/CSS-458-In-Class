import numpy as np

from Dealer import Dealer
import Global
from Player import Player

ratio = []
def main():
    numberOfGame = 0

    while (numberOfGame < Global.NUMBER_OF_SIMULATION):
        win = 0  # Win/Loss ratio
        lose = 0
        theDealer = Dealer(None, Global.NUMBER_OF_DECKS)
        listOfPlayer = []
        for i in range(Global.NUMBER_OF_PLAYER):
            player = Player(theDealer)
            listOfPlayer.append(player)  # Each player now have this dealer
        # Asigning the list of player back to the dealer
        theDealer.listOfPlayer = listOfPlayer
        numberRounds = 0

        while (numberRounds < Global.NUMBER_OF_ROUNDS):  # Play each round until player lose or something
            theDealer.deal(False, None)
            for i in range(Global.NUMBER_OF_PLAYER):
                listOfPlayer[i].play()
            theDealer.play()
            # for i in range(Global.NUMBER_OF_PLAYER):
            if (np.sum(np.asarray(listOfPlayer[0].numberOfCard)) > np.sum(np.asarray(theDealer.numberOfCard))
                and listOfPlayer[0].bust == False):
                win += 1
            else:
                lose += 1
            numberRounds += 1
            print(win)
            print(lose)
        ratio.append(win / lose)
        # Finished one whole simulation
        numberOfGame += 1

main()
