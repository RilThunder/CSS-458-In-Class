import matplotlib.pyplot as plt
import numpy as np

import Global
from Dealer import Dealer
from Player import Player

# Global variable
win = 0.
lose = 0.
tie = 0.
# The ratio of win per each game
ratio = []
wins = []

# Initialize the Plot Figure to plot the data
fig = plt.figure(figsize=(22,11))
pie_size = [[0.545, 0.50, 0.2, 0.3], [0.545, 0.05, 0.2, 0.3],
            [0.790, 0.50, 0.2, 0.3], [0.790, 0.05, 0.2, 0.3]]

fig = plt.gcf()
fig.canvas.set_window_title('Blackjack Analysis')

def main():
    global wins
    global win
    global lose
    global tie
    global numberOfRound
    numberOfGame = 0
    Simulation_Variation = [1, 2, 3, 2]
    
    """
    # Initialize the Plot Figure to plot the data
    fig1, ((pie1, pie2), (pie3, pie4)) = plt.subplots(2, 2, sharex='col', sharey='row')
    pie_list = [pie1, pie2, pie3, pie4]
    fig2 = plt.figure()
    """
    
    # While loops until Number of Simulation is met
    for num_sim in range(4):
        numberOfGame = 0
        del wins[:]
        del ratio[:]
        Global.WAY_TO_PLAY = Simulation_Variation[num_sim]
        
        # Declaring the Axes to be used in Figure
        ax1 = fig.add_axes((0.035, 0.50, 0.2, 0.3))
        ax1.axis([1, Global.NUMBER_OF_SIMULATION, 0.0, 1.0])
        ax1.set_title('Win Ratio vs Number of Games')
        ax1.set_xlabel('Number of Games')
        ax1.set_ylabel('Win Ratio')
        ax2 = fig.add_axes((0.280, 0.50, 0.2, 0.3))
        ax2.axis([1, Global.NUMBER_OF_SIMULATION, 0, Global.NUMBER_OF_SIMULATION])
        ax2.set_title('Number of Wins vs Number of Games')
        ax2.set_xlabel('Number of Games')
        ax2.set_ylabel('Number of Wins')


        while (numberOfGame < Global.NUMBER_OF_SIMULATION):
            # Reset the statistics for every new game
            win = 0
            lose = 0
            tie = 0
            
            # Initialize the Dealer for this Simulation
            theDealer = Dealer(None, Global.NUMBER_OF_DECKS)
            
            # Initialize the Player(s) for this simulation
            listOfPlayer = []
            for i in range(Global.NUMBER_OF_PLAYER): # Player number is decided on NUMBER_OF_PLAYER
                player = Player(theDealer, Global.WAY_TO_PLAY)
                listOfPlayer.append(player)  # Each player now have this dealer
                
            # Asigning the list of player back to the dealer
            theDealer.listOfPlayer = listOfPlayer
    
            # Shuffle the deck before entering the game
            theDealer.theDeck.shuffle()
            
            # Play each round until NUMBER_OF ROUNDS or Player runs out of Chips
            for i in range(Global.NUMBER_OF_ROUNDS): 
    
                # Initialize the Game, by dealing 2 cards for every player(s)
                # and the dealer.
                theDealer.deal(False, None)
    
                # Player(s) play until they Stand or Bust
                for j in range(Global.NUMBER_OF_PLAYER):
                    listOfPlayer[j].play()
                    
                # Dealer play until dealer Stand or Bust
                theDealer.play()
    
                theDealer.collectChip()
                check(listOfPlayer, theDealer, numberOfGame, i)
                # Remove cards from player and dealer and start empty again
                theDealer.refresh()
    
            # After all rounds are played, win ratio is appended to Ratio List.
            wins.append(win)
            ratio.append(float(win) / (Global.NUMBER_OF_ROUNDS))
            # Finished one whole simulation
    
            plotNumberOfGame(ax1, ax2, numberOfGame, wins)
            numberOfGame += 1
            
        print("--------------------------------------")
        print(num_sim)
        if(num_sim < 3):
            ax1.cla()
            ax2.cla()
        plotPieChart(fig, pie_size, num_sim, ratio)

    plt.show()

def plotPieChart(fig, pie_size, i, ratio):
    win_ratio = np.average(ratio)
    loss_ratio = 1 - np.average(ratio)
    win_loss_ratio = np.array([win_ratio, loss_ratio])
    current_pie = plt.axes(pie_size[i])
    current_pie.pie(win_loss_ratio, labels = ['Win', 'Loss'], \
                    colors = ['gold', 'yellowgreen'], autopct='%1.1f%%')
    labels = ['Win', 'Loss']
    current_pie.legend(labels)
    return 0

def plotNumberOfGame(ax1, ax2, numberOfGame, wins):
    
    # Plot the first axes in Fig
    ax1.plot(numberOfGame, ratio[numberOfGame], '-.', color='b')
    ax1.plot(range(numberOfGame + 1), ratio, marker='.', color='r')
    
    # Plot the second axes in Fig
    ax2.bar(range(numberOfGame + 1), wins)
    
    plt.pause(0.005)  # Pause 0.001 to create interval between every plot
    fig.show()  # Display Fig1

def check(listPlayer, theDealer, numberOfGame, numberOfRound):
    global win
    global tie
    global lose
    global wins
    print("For game " + str(numberOfGame + 1) + " and round " + str(
        numberOfRound + 1) + ", here are the results ")
    print("The first player had a total of " + str(np.sum(np.asarray(listPlayer[0].firstHandCard))))
    print("The dealer had a total of " + str(np.sum(np.asarray(theDealer.firstHandCard))))

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

def playRound():
    
    # Initialize the Dealer for this Simulation
    theDealer = Dealer(None, Global.NUMBER_OF_DECKS)
    
    # Initialize the Player(s) for this simulation
    listOfPlayer = []
    for i in range(Global.NUMBER_OF_PLAYER): # Player number is decided on NUMBER_OF_PLAYER
        player = Player(theDealer, Global.WAY_TO_PLAY)
        listOfPlayer.append(player)  # Each player now have this dealer
        
    # Asigning the list of player back to the dealer
    theDealer.listOfPlayer = listOfPlayer
    # Shuffle the deck before entering the game
    theDealer.theDeck.shuffle()
    # Initialize the Game, by dealing 2 cards for every player(s)
    # and the dealer.
    theDealer.deal(False, None)
    # Player(s) play until they Stand or Bust
    for j in range(Global.NUMBER_OF_PLAYER):
        print('Player ' +str(j + 1) + ' starts with ' + str(listOfPlayer[j].firstHandCard))
        listOfPlayer[j].play()
        print('Player ' +str(j + 1) + 'ends with' + str(listOfPlayer[j].firstHandCard))
        if listOfPlayer[j].bust == True:
            print('Player ' +str(j + 1) + ' Bust!')
    # Dealer play until dealer Stand or Bust
    print('Dealer starts with ' + str(theDealer.firstHandCard))
    theDealer.play()
    print('Dealer ends with '+ str(theDealer.firstHandCard))
    if theDealer.bust == True:
        print('Dealer Bust!')
    for j in range(Global.NUMBER_OF_PLAYER):
        if ((np.sum(np.asarray(listOfPlayer[j].firstHandCard)) > np.sum(np.asarray(theDealer.firstHandCard))) and listOfPlayer[j].bust == False) \
                or (theDealer.bust and listOfPlayer[j].bust == False):
            print('Player ' + str(j+1) + ' won!')
        else:
            if (np.sum(np.asarray(listOfPlayer[0].firstHandCard)) == np.sum(np.asarray(theDealer.firstHandCard))):
                print('Player ' + str(j+1) + ' tied the dealer!')
            else:
                print('Player ' + str(j+1) + ' lost!')
    theDealer.collectChip()
    # Remove cards from player and dealer and start empty again
    theDealer.refresh()

main()
