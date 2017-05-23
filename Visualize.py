import matplotlib.pyplot as plt
import numpy as np

import Global
from Dealer import Dealer
from Player import Player

# Global variable
win = 0
lose = 0
tie = 0
# The ratio of win per each game
ratio = []


def main():
    global hl
    global win
    global lose
    global tie
    global numberOfRound
    numberOfGame = 0

    while (numberOfGame < Global.NUMBER_OF_SIMULATION):
        # Reset the statistics for every new game
        win = 0
        lose = 0
        tie = 0
        theDealer = Dealer(None, Global.NUMBER_OF_DECKS)
        listOfPlayer = []
        for i in range(Global.NUMBER_OF_PLAYER):
            player = Player(theDealer)
            listOfPlayer.append(player)  # Each player now have this dealer
        # Asigning the list of player back to the dealer
        theDealer.listOfPlayer = listOfPlayer

        # Shuffle the deck before entering the game
        theDealer.theDeck.shuffle()
        plt.figure()
        for i in range(Global.NUMBER_OF_ROUNDS):  # Play each round until player lose or something

            theDealer.deal(False, None)

            for j in range(Global.NUMBER_OF_PLAYER):
                listOfPlayer[j].play()
            theDealer.play()


            theDealer.collectChip()
            check(listOfPlayer, theDealer, numberOfGame, i)
            # Remove cards from player and dealer and start empty again
            theDealer.refresh()

        ratio.append(win / (Global.NUMBER_OF_ROUNDS))
        # Finished one whole simulation

        numberOfGame += 1


def check(listPlayer, theDealer, numberOfGame, numberOfRound):
    global win
    global tie
    global lose
    print("For the " + str(numberOfGame + 1) + "th game and " + str(
        numberOfRound + 1) + "th round, here are the results ")
    print("The first player have a total of " + str(np.sum(np.asarray(listPlayer[0].firstHandCard))))
    print("The dealer have a total of " + str(np.sum(np.asarray(theDealer.firstHandCard))))

    print()
    # Check to see if the first player win or lose this round
    # The player win when the player haven't bust and the dealer already busted
    # Or when both player and dealer haven't bust but the player card have to be
    # greater than the dealer
    if ((np.sum(np.asarray(listPlayer[0].firstHandCard)) > np.sum(np.asarray(theDealer.firstHandCard))) and
                listPlayer[0].bust == False) \
            or (theDealer.bust and listPlayer[0].bust == False):
        win += 1
    else:
        if (np.sum(np.asarray(listPlayer[0].firstHandCard)) == np.sum(np.asarray(theDealer.firstHandCard))):
            tie += 1
        else:
            if (theDealer.bust and listPlayer[0].bust):
                print("The player Busted first")
            lose += 1

    # Sample output
    print()
    print("Total number of win, lose and tie for player 1 is")
    print("Win: " + str(win))
    print("Lose " + str(lose))
    print("Tie: " + str(tie))
    print("Total chips at the moment " + str(listPlayer[0].numOfChips))
    print()


# def plotRatio(ratio):
#
#     plt.figure()
#     yAxis = np.asarray(ratio)
#
#     xAxis = np.arange(Global.NUMBER_OF_SIMULATION)
#
#
#
#     plt.plot(xAxis, yAxis)
#     plt.show()


main()
# plotRatio(ratio)
