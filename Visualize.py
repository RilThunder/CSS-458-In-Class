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
win_round = []
chips = []
win_ratio_list = []
loss_ratio_list = []

# Initialize the Plot Figure to plot the data
fig = plt.figure(figsize=(15,9))
rect = fig.patch
rect.set_facecolor('white')
pie_size = [[0.535, 0.46, 0.23, 0.37], [0.535, 0.03, 0.23, 0.37],
            [0.77, 0.46, 0.23, 0.37], [0.77, 0.03, 0.23, 0.37]]

fig = plt.gcf()
fig.canvas.set_window_title('BLACKJACK SIMULATION')
filename = 'MainTextFile.txt'
file = open(filename, 'w')
playOneRound = 'playOneRoundDetail.txt'
detailFile = open(playOneRound, 'w')
def main():
    global wins
    global win
    global win_round
    global lose
    global tie
    global numberOfRound
    global chip
    global chips
    global file
    global win_ratio_list
    global loss_ratio_list
    Simulation_Variation = [1, 2, 3, 1]

    # While loops until Number of Simulation is met
    for numberOfSim in range(4):
        if numberOfSim == 1:
            file.write('We are using the playing with odds method')
            file.write('\n')
            file.write('This is like calculating the remaining cards and determine if it is best to hit')

        else:
            if numberOfSim == 2:
                file.write('We are using the playing random method')
                file.write('\n')
                file.write('This is like flipping a coin where we generate a random number'
                           ' and determine if we should continue or not')
            else:
                file.write('We are using the playing normal method')
                file.write('\n')
                file.write('This is a set of predefined way that the player can play Black Jack')
        file.write('\n')

        numberOfGame = 0
        del wins[:]
        del ratio[:]
        del chips[:]
        del win_ratio_list[:]
        del loss_ratio_list[:]
        Global.WAY_TO_PLAY = Simulation_Variation[numberOfSim]
        
        # Declaring the Axes to be used in Figure      
        fig.text(0.33, 0.95, 'BLACKJACK SIMULATION', fontsize=30, color = 'k')
        simu_title = fig.text(0.21, 0.85, 'Simulation: ' + str(numberOfSim+1), fontsize=20)
        
        ax1 = fig.add_axes((0.045, 0.50, 0.2, 0.3))
        ax1.axis([1, Global.NUMBER_OF_SIMULATION, 0.0, 1.0])
        ax1.set_title('Win Ratio vs Number of Games')
        ax1.set_xlabel('Number of Games')
        ax1.set_ylabel('Win Ratio')
        
        ax2 = fig.add_axes((0.310, 0.50, 0.2, 0.3))
        ax2.axis([1, Global.NUMBER_OF_SIMULATION, 0, 1000])
        ax2.set_title('Chip Count vs Number of Games')
        ax2.set_xlabel('Number of Games')
        ax2.set_ylabel('Number of Chips')
        
        ax3 = fig.add_axes((0.045, 0.07, 0.465, 0.3))
        
        current_pie = plt.axes(pie_size[numberOfSim])

        while (numberOfGame < Global.NUMBER_OF_SIMULATION):
            # Reset the statistics for every new game
            win = 0
            lose = 0
            tie = 0
            chip = 0

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
            chips.append(float(chip) / (Global.NUMBER_OF_ROUNDS))
            
            # Finished one whole simulation
            plotNumberOfGame(ax1, ax2, ax3, numberOfGame, win_round, wins, chips)
            plotPieChart(current_pie, ratio, numberOfSim, numberOfGame, Global.WAY_TO_PLAY)
            if(numberOfSim == 3) and (numberOfGame == Global.NUMBER_OF_SIMULATION - 1):
                ax3.plot(range(1, Global.NUMBER_OF_ROUNDS+1), win_round, marker='.', color= 'b')
            del win_round[:]
            numberOfGame += 1
            
        if(numberOfSim < 3):
            ax1.cla()
            ax2.cla()
        label_PieChart(current_pie, numberOfSim, Global.WAY_TO_PLAY)
        simu_title.remove()

    simu_title = fig.text(0.21, 0.85, 'Simulation: ' + str(numberOfSim+1), fontsize=20)
    plt.show()

def label_PieChart(current_pie, numberOfSim, WAY_TO_PLAY):
    global win_ratio_list
    global loss_ratio_list
    
    if(WAY_TO_PLAY == 1):
        playing = 'with odd'
    elif(WAY_TO_PLAY == 2):
        playing = 'randomly'
    else:
        playing = 'normally'

    current_pie.set_title('Simulation ' + str(numberOfSim + 1) + \
                            '\n' + 'Player playing ' + playing)

    win_ratio = np.average(win_ratio_list)
    loss_ratio = 1 - np.average(loss_ratio_list)
    win_loss_ratio = np.array([win_ratio, loss_ratio])
    current_pie.pie(win_loss_ratio, labels = ['Win', 'Loss'], \
                    colors = ['yellowgreen', 'gold'], autopct='%1.1f%%')
    labels = ['Win', 'Loss']
    current_pie.legend(labels, loc = 2)

def plotPieChart(current_pie, ratio, numberOfSim, numberOfGame, WAY_TO_PLAY):
    global win_ratio_list
    global loss_ratio_list
    
    if(WAY_TO_PLAY == 1):
        playing = 'with odd'
    elif(WAY_TO_PLAY == 2):
        playing = 'randomly'
    else:
        playing = 'normally'

    current_pie.set_title('Simulation ' + str(numberOfSim + 1) + \
                            ' Round ' + str(numberOfGame + 1) + '\n' + 
                            'Player playing ' + playing)

    win_ratio = np.average(ratio)
    win_ratio_list.append(win_ratio)
    loss_ratio = 1 - np.average(ratio)
    loss_ratio_list.append(win_ratio)
    
    win_loss_ratio = np.array([win_ratio, loss_ratio])
    current_pie.pie(win_loss_ratio, \
                    colors = ['yellowgreen', 'gold'])
    labels = ['Win', 'Loss']
    current_pie.legend(labels, loc = 2)

def plotNumberOfGame(ax1, ax2, ax3, numberOfGame, win_round, wins, chips):
    
    # Plot the first axes in Fig
    #ax1.plot(numberOfGame, ratio[numberOfGame], '-.', color='g')
    color = np.array(['b', 'g', 'r', 'c', 'm', 'k'])
    np.random.shuffle(color)
    ax1.plot(range(1, numberOfGame + 2), ratio, marker='.', color= color[0])
    
    # Plot the second axes in Fig
    ax2.plot(range(1, numberOfGame + 2), chips, marker='.', color= color[0])

    ax3.plot(range(1, Global.NUMBER_OF_ROUNDS+1), win_round, marker='.', color= 'b')
    
    plt.pause(0.06)  # Pause 0.001 to create interval between every plot
    fig.show()  # Display Fig1

    ax3.cla()
    ax3.axis([1, Global.NUMBER_OF_ROUNDS, 0.0, Global.NUMBER_OF_ROUNDS])
    ax3.set_title('Number of Win vs Number of Rounds')
    ax3.set_xlabel('Number of Rounds')
    ax3.set_ylabel('Number of Win')

def check(listPlayer, theDealer, numberOfGame, numberOfRound):
    global win
    global tie
    global lose
    global wins
    global chip
    global chips
    global win_round
    global file
    file.write("For game " + str(numberOfGame + 1) + " and round " + str(

        numberOfRound + 1) + ", here are the results ")
    file.write('\n')
    file.write("The first player had a total of " + str(np.sum(np.asarray(listPlayer[0].firstHandCard))))
    file.write('\n')
    file.write("The dealer had a total of " + str(np.sum(np.asarray(theDealer.firstHandCard))))
    file.write('\n')
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
                file.write("The player Busted first")
                file.write('\n')
            lose += 1

    chip += listPlayer[0].numOfChips
    win_round.append(win)
    
    # Sample output
    file.write('\n')
    file.write("Total number of win, lose and tie for player 1 is")
    file.write('\n')
    file.write("Win: " + str(win))
    file.write('\n')
    file.write("Lose " + str(lose))
    file.write('\n')
    file.write("Tie: " + str(tie))
    file.write('\n')
    file.write("Total chips at the moment " + str(listPlayer[0].numOfChips))
    file.write('\n')

def playRound():
    global detailFile

    if Global.WAY_TO_PLAY == 1:
        detailFile.write('We are using the playing with odds method')
        detailFile.write('\n')
        detailFile.write('This is like calculating the remaining cards and determine if it is best to hit')

    else:
        if Global.WAY_TO_PLAY == 2:
            detailFile.write('We are using the playing random method')
            detailFile.write('\n')
            detailFile.write('This is like flipping a coin where we generate a random number'
                             ' and determine if we should continue or not')
        else:
            detailFile.write('We are using the playing normal method')
            detailFile.write('\n')
            detailFile.write('This is a set of predefined way that the player can play Black Jack')
    detailFile.write('\n')
    detailFile.write('For this detail round, we are using ' + str(Global.NUMBER_OF_DECKS))
    detailFile.write('\n')
    detailFile.write('We also have ' + str(Global.NUMBER_OF_PLAYER) + ' players')

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
        detailFile.write('Player ' + str(j + 1) + ' starts with ' + str(listOfPlayer[j].firstHandCard))
        detailFile.write('\n')
        listOfPlayer[j].play()
        detailFile.write('Player ' + str(j + 1) + ' ends with' + str(listOfPlayer[j].firstHandCard))
        detailFile.write('\n')
        if listOfPlayer[j].bust == True:
            detailFile.write('Player ' + str(j + 1) + ' Bust!')
            detailFile.write('\n')
    # Dealer play until dealer Stand or Bust
    detailFile.write('Dealer starts with ' + str(theDealer.firstHandCard))
    detailFile.write('\n')
    theDealer.play()
    detailFile.write('Dealer ends with ' + str(theDealer.firstHandCard))
    detailFile.write('\n')
    if theDealer.bust == True:
        detailFile.write('Dealer Bust!')
        detailFile.write('\n')
    for j in range(Global.NUMBER_OF_PLAYER):
        if ((np.sum(np.asarray(listOfPlayer[j].firstHandCard)) > np.sum(np.asarray(theDealer.firstHandCard))) and listOfPlayer[j].bust == False) \
                or (theDealer.bust and listOfPlayer[j].bust == False):
            detailFile.write('Player ' + str(j + 1) + ' won!')
            detailFile.write('\n')
        else:
            if (np.sum(np.asarray(listOfPlayer[j].firstHandCard)) == np.sum(np.asarray(theDealer.firstHandCard))):
                detailFile.write('Player ' + str(j + 1) + ' tied the dealer!')
                detailFile.write('\n')
            else:
                detailFile.write('Player ' + str(j + 1) + ' lost!')
                detailFile.write('\n')
    theDealer.collectChip()
    # Remove cards from player and dealer and start empty again
    theDealer.refresh()

main()
# playRound()
file.close()
detailFile.close()
