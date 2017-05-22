import numpy as np

import Global
from Dealer import Dealer
from Player import Player

win = 0
lose = 0
tie = 0
ratio = []


def main():
    numberOfGame = 0

    while (numberOfGame < Global.NUMBER_OF_SIMULATION):

        theDealer = Dealer(None, Global.NUMBER_OF_DECKS)
        listOfPlayer = []
        for i in range(Global.NUMBER_OF_PLAYER):
            player = Player(theDealer)
            listOfPlayer.append(player)  # Each player now have this dealer
        # Asigning the list of player back to the dealer
        theDealer.listOfPlayer = listOfPlayer
        numberRounds = 0
        # Shuffle the deck before entering the game
        theDealer.theDeck.shuffle()

        while (numberRounds < Global.NUMBER_OF_ROUNDS):  # Play each round until player lose or something

            theDealer.deal(False, None)

            for i in range(Global.NUMBER_OF_PLAYER):
                listOfPlayer[i].play()
            theDealer.play()
            check(listOfPlayer, theDealer)
            numberRounds += 1
            # Sample output
            print()
            print("Total number of win, lose and tie for player 1 is")
            print(win)
            print(lose)
            print(tie)
            print()

            # Remove cards from player and dealer and start empty again
            theDealer.refresh()

        ratio.append(win / lose)
        # Finished one whole simulation
        numberOfGame += 1


def check(listPlayer, theDealer):
    global win
    global tie
    global lose
    print("The first player have a total of " + str(np.sum(np.asarray(listPlayer[0].numberOfCard))))
    print("The dealer have a total of " + str(np.sum(np.asarray(theDealer.numberOfCard))))

    print()
    # Check to see if the first player win or lose this round
    # The player win when the player haven't bust and the dealer already busted
    # Or when both player and dealer haven't bust but the player card have to be
    # greater than the dealer
    if ((np.sum(np.asarray(listPlayer[0].numberOfCard)) > np.sum(np.asarray(theDealer.numberOfCard))) and
                listPlayer[0].bust == False) \
            or (theDealer.bust and listPlayer[0].bust == False):
        win += 1
    else:
        if (np.sum(np.asarray(listPlayer[0].numberOfCard)) == np.sum(np.asarray(theDealer.numberOfCard))):
            tie += 1
        else:

            lose += 1


main()
