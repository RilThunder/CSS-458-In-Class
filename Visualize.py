import Dealer
import Global
import Player


def main():
    numberOfGame = 0
    while (numberOfGame < 100):
        theDealer = Dealer(None, Global.NUMBER_OF_DECKS)
        listOfPlayer = []
        for i in range(Global.NUMBER_OF_PLAYER):
            player = Player(theDealer)
            listOfPlayer.append(player)  # Each player now have this dealer
        # Asigning the list of player back to the dealer
        theDealer.listOfPlayer = listOfPlayer

        while (True):  # Play each round until player lose or something
            theDealer.deal(False, None)
            for i in range(Global.NUMBER_OF_PLAYER):
                listOfPlayer[i].play()
            theDealer.play()

        # Finished one whole simulation
        numberOfGame += 1
