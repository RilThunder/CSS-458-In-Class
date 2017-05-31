import matplotlib.pyplot as plt
import numpy as np

import Global
from Dealer import Dealer
from Player import Player

#=======================================================================
#                        General Documentation
""" 
Blackjack Simulation - Visualize
Visualize work as the Driver for the Blackjack Simulation.

Once the program runs, it will simulate the blackjack
as if it was played by an actual player and a dealer.

All of the win, loss, tie, chipcounts will be counted for,
and is used to plot the analysis on the graphical figure.

The simulation is executed 4 times in our simulation,
and per simulation, a different variable can change to compare the
result for our analysis.
"""

#-----------------------------------------------------------------------
#                       Additional Documentation
#
# - Written by : Trystan MacInnes, Himakar Kadiri,
#                Jin Kim, Thuan Tran
# - Last modified on : 05/29/2017
#
# Notes:
# - Written with Python 2.7.11
# - To test, execute "python Visualize.py".
#-----------------------------------------------------------------------

# Global variable
win = 0.
lose = 0.
tie = 0.
player_bust = 0
dealer_bust = 0

ratio = [] # The ratio of win per each game
wins = [] # The list of wins in a game
win_round = [] # The list of wins in every round
chips = [] # The list of chips earned in every round
win_ratio_list = [] # The list of winning ratio per simulation
loss_ratio_list = [] # The list of losing ratio per simulation
player_bust_list = [] # The list of player bust # per simulation
dealer_bust_list = [] # The list of dealer bust # per simulation

# Initialize the Plot Figure to plot the data
fig = plt.figure(figsize=(15,9)) # initialize the size of the figure
# Set the background of figure to 'white'
rect = fig.patch
rect.set_facecolor('white')
# Set the title of the figure in a window
fig = plt.gcf()
fig.canvas.set_window_title('BLACKJACK SIMULATION')
# Declaring the size of each pie to be used
pie_size = [[0.535, 0.46, 0.23, 0.37], [0.77, 0.46, 0.23, 0.37],
            [0.535, 0.03, 0.23, 0.37], [0.77, 0.03, 0.23, 0.37]]

filename = 'MainTextFile.txt'
file = open(filename, 'w')
playOneRound = 'playOneRoundDetail.txt'
detailFile = open(playOneRound, 'w')

#--------------------------------main-----------------------------------
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
    global player_bust
    global dealer_bust
    global player_bust_list
    global dealer_bust_list

    # Changing variables for each simulation
    Simulation_Variation = [1, 1, 2, 3]
    Player_Variation = [4, 4, 4, 4]
    Deck_Variation = [2, 2, 2, 2]
    Confidence_Variation = [0.2, 0.4, 0.6, 0.8]
    Round_Variation = [20, 20, 20, 20]
    Game_Variation = [20, 20, 20, 20]

#---------------------Number of simulation (max 4)----------------------
    # While loops until Number of Simulation is met
    for numberOfSim in range(4):
        wayToPlay = Simulation_Variation[numberOfSim]
        numberOfPlayer = Player_Variation[numberOfSim]
        numberOfDeck = Deck_Variation[numberOfSim]
        writeTo = 'We are using the playing with '
        differentAttributes = "with " + str(numberOfPlayer) + " players and " + str(numberOfDeck) + " decks "
        if wayToPlay == 1:

            writeTo += "odds "
        else:
            if wayToPlay == 2:
                writeTo += "random "

            else:
                writeTo += "normal "
        writeTo += differentAttributes + "\n"
        if wayToPlay == 1:

            writeTo += 'This is like calculating the remaining cards and determine if it is best to hit' + "\n"
        else:
            if wayToPlay == 2:
                writeTo += 'This is like flipping a coin where we generate a random number and determine if we should continue or not' + "\n"

            else:
                writeTo += 'This is a set of predefined way that the player can play Black Jack' + "\n"
        print(writeTo)
        file.write(writeTo)

        
        # Reinitializing the value and list for new simulation
        numberOfGame = 0 
        del wins[:]
        del ratio[:]
        del chips[:]
        del win_ratio_list[:]
        del loss_ratio_list[:]
        del player_bust_list[:]
        del dealer_bust_list[:]

        # Changing the variables for each simulation.
        Global.WAY_TO_PLAY = Simulation_Variation[numberOfSim]
        Global.NUMBER_OF_DECKS = Deck_Variation[numberOfSim]
        Global.NUMBER_OF_PLAYER = Player_Variation[numberOfSim]
        Global.BASE_CONFIDENT = Confidence_Variation[numberOfSim]
        Global.NUMBER_OF_SIMULATION = Game_Variation[numberOfSim]
        Global.NUMBER_OF_ROUNDS = Round_Variation[numberOfSim]
            
        # Declaring the Axes to be used in Figure      
        # Displays title on simulation
        fig.text(0.33, 0.95, 'BLACKJACK SIMULATION', fontsize=30, color = 'k')
        # Display 'Simulation #' to indicate which simulation the graph is showing
        simu_title = fig.text(0.21, 0.88, 'Simulation: ' + str(numberOfSim+1), fontsize=20)
        
        # Declaring first axes for 'Win Ratio vs Number of Games'
        ax1 = fig.add_axes((0.045, 0.50, 0.2, 0.3))
        ax1.axis([1, Global.NUMBER_OF_SIMULATION, 0.0, 1.0])
        ax1.set_title('Win Ratio vs Number of Games')
        ax1.set_xlabel('Number of Games')
        ax1.set_ylabel('Win Ratio')
        
        # Declaring second axes for 'Chip Count vs Number of Games'
        ax2 = fig.add_axes((0.310, 0.50, 0.2, 0.3))
        ax2.axis([1, Global.NUMBER_OF_SIMULATION, 0, 2000])
        ax2.set_title('Chip Count vs Number of Games' + '\n' + 
        '(Starting confidence level: ' + str(Global.BASE_CONFIDENT) + ')')
        ax2.set_xlabel('Number of Games')
        ax2.set_ylabel('Number of Chips')
        
        # Declaring second axes for 'Number of Win vs Number of Rounds'
        # Title, and other variables are declared later for refreshing plot figure
        ax3 = fig.add_axes((0.045, 0.07, 0.465, 0.3))
        
        # Declaring axes for pie chart at pie_size[] location
        current_pie = plt.axes(pie_size[numberOfSim])

#-------------------------- Number of Games ----------------------------
        while (numberOfGame < Global.NUMBER_OF_SIMULATION):
            # Reset the statistics for every new game
            win = 0
            lose = 0
            tie = 0
            chip = 0
            player_bust = 0
            dealer_bust = 0

            # Initialize the Dealer for this Simulation
            theDealer = Dealer(None, Global.NUMBER_OF_DECKS)
            
            # Initialize the Player(s) for this simulation
            listOfPlayer = []
            for i in range(Global.NUMBER_OF_PLAYER): # Player number is decided on NUMBER_OF_PLAYER
                player = Player(theDealer, Global.WAY_TO_PLAY, Global.BASE_CONFIDENT)
                listOfPlayer.append(player)  # Each player now have this dealer
                
            # Asigning the list of player back to the dealer
            theDealer.listOfPlayer = listOfPlayer
    
            # Shuffle the deck before entering the game
            theDealer.theDeck.shuffle()
            

#------------------------- Number of Rounds ----------------------------
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
            # Calls for each method to plot the new lines in a figure
            plotNumberOfGame(ax1, ax2, ax3, numberOfGame, win_round, wins, chips)
            plotPieChart(current_pie, ratio, numberOfSim, numberOfGame, Global.WAY_TO_PLAY)
            # Used for last plot lines at the end of simulation, 
            # to keep the simulation show, without erasing
            if(numberOfSim == 3) and (numberOfGame == Global.NUMBER_OF_SIMULATION - 1):
                ax3.plot(range(1, Global.NUMBER_OF_ROUNDS+1), win_round, marker='.', color= 'b')

            # Clear win_round to be used on next game
            del win_round[:]
            numberOfGame += 1
            
        # Clear axes 1 and 2 to be used for next simulation
        if(numberOfSim < 3):
            ax1.cla()
            ax2.cla()

        # Makes a pie chart figure for current simulation
        label_PieChart(current_pie, numberOfSim, Global.WAY_TO_PLAY)

        # Clears title to show the next simulation text
        simu_title.remove()

    simu_title = fig.text(0.21, 0.88, 'Simulation: ' + str(numberOfSim+1), fontsize=20)

    # Plot the figure
    plt.show()

#--------------------------- plotPieChart ------------------------------
def plotPieChart(current_pie, ratio, numberOfSim, numberOfGame, WAY_TO_PLAY):
    global win_ratio_list
    global loss_ratio_list
    global player_bust
    global dealer_bust
    
    # To display the correct play method on pie
    if(WAY_TO_PLAY == 1):
        playing = 'Odd'
    elif(WAY_TO_PLAY == 2):
        playing = 'Random'
    else:
        playing = 'Normal'
        
    # Append the bust # to a list to get an average
    player_bust_list.append(player_bust)
    dealer_bust_list.append(dealer_bust)
    
    # Show the title of the pie
    current_pie.set_title('Simulation ' + str(numberOfSim + 1) + \
                            ' Round ' + str(numberOfGame + 1) + '\n' + 
                            '' + playing + ' : ' +
                            'Players=' + str(Global.NUMBER_OF_PLAYER) + \
                            ' : Decks=' + str(Global.NUMBER_OF_DECKS) + '\n' +
                            'Avg. P.Bust=' + str(player_bust) + ' D.Bust ='+
                            str(dealer_bust))

    # Get the win/loss ratio, while adding them on the list
    win_ratio = np.average(ratio)
    win_ratio_list.append(win_ratio)
    loss_ratio = 1 - np.average(ratio)
    loss_ratio_list.append(win_ratio)
    win_loss_ratio = np.array([win_ratio, loss_ratio])
    
    # Display the pie chart that refreshes every round
    current_pie.pie(win_loss_ratio, \
                    colors = ['yellowgreen', 'gold'])
    labels = ['Win', 'Loss']
    current_pie.legend(labels, loc = 2)

#------------------------- label_PieChart ------------------------------
def label_PieChart(current_pie, numberOfSim, WAY_TO_PLAY):
    global win_ratio_list
    global loss_ratio_list
    global player_bust
    global dealer_bust
    global player_bust_list
    global dealer_bust_list
    
    # To display the correct play method on pie
    if(WAY_TO_PLAY == 1):
        playing = 'Odd'
    elif(WAY_TO_PLAY == 2):
        playing = 'Random'
    else:
        playing = 'Normal'

    # Show the title of the pie
    current_pie.set_title('Simulation ' + str(numberOfSim + 1) + \
                            '\n' + '' + playing + ' : ' +
                            'Players=' + str(Global.NUMBER_OF_PLAYER) + \
                            ' : Decks=' + str(Global.NUMBER_OF_DECKS) + '\n' +
                            'Avg. P.Bust=' + str(round(np.average(player_bust_list), 1)) + ' D.Bust=' +
                            str(round(np.average(dealer_bust_list), 1)))
                            
    # Get the total win/loss ratio, for average win/loss ratio
    win_ratio = np.average(win_ratio_list)
    loss_ratio = 1 - np.average(loss_ratio_list)
    win_loss_ratio = np.array([win_ratio, loss_ratio])

    # Display the pie chart that refreshes every round
    current_pie.pie(win_loss_ratio, labels = ['Win', 'Loss'], \
                    colors = ['yellowgreen', 'gold'], autopct='%1.1f%%')
    labels = ['Win', 'Loss']
    current_pie.legend(labels, loc = 2)

#------------------------- plotNumberOfGame ----------------------------
def plotNumberOfGame(ax1, ax2, ax3, numberOfGame, win_round, wins, chips):
    
    # Plot the first axes in Fig
    #ax1.plot(numberOfGame, ratio[numberOfGame], '-.', color='g')
    color = np.array(['b', 'g', 'r', 'c', 'm', 'k'])
    np.random.shuffle(color)
    ax1.plot(range(1, numberOfGame + 2), ratio, marker='.', color= color[0])
    
    # Plot the second axes in Fig
    chips_array = np.array(chips)
    chips_array[chips_array < 0] = 100
    ax2.plot(range(1, numberOfGame + 2), chips_array, marker='.', color= color[0])

    # Plot the third axes in Fig
    ax3.plot(range(1, Global.NUMBER_OF_ROUNDS+1), win_round, marker='.', color= 'b')
    
    plt.pause(0.06)  # Pause 0.001 to create interval between every plot
    fig.show()  # Display Fig1

    # Clear the axes 3 to refresh for next round
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
    global player_bust
    global dealer_bust

    writeTo = "For game " + str(numberOfGame + 1) + " and round " + str(

        numberOfRound + 1) + ", here are the results " + "\n"
    print(writeTo)
    file.write(writeTo)
    writeTo = "The first player had a total of " + str(np.sum(np.asarray(listPlayer[0].firstHandCard))) + "\n"
    print(writeTo)
    file.write(writeTo)
    writeTo = "The dealer had a total of " + str(np.sum(np.asarray(theDealer.firstHandCard))) + "\n"
    print(writeTo)
    file.write(writeTo)
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
                writeTo = "The player Busted first" + "\n"
                print(writeTo)
                file.write(writeTo)

            lose += 1
            
    # Get the number of bust for player and dealer in a game
    if(listPlayer[0].bust == True):
        player_bust += 1
    if(theDealer.bust == True):
        dealer_bust += 1

    chip += listPlayer[0].numOfChips
    win_round.append(win)
    writeTo = "Total number of win, lose and tie for player 1 is" + "\n"
    # Sample output

    file.write(writeTo)
    print(writeTo)

    writeTo = "Win: " + str(win) + "\n"
    print(writeTo)
    file.write(writeTo)

    writeTo = "Lose " + str(lose) + "\n"
    print(writeTo)
    file.write(writeTo)

    writeTo = "Tie: " + str(tie) + "\n"
    print(writeTo)
    file.write(writeTo)

    writeTo = "Total chips at the moment " + str(listPlayer[0].numOfChips) + "\n"

    print(writeTo)
    file.write(writeTo)

def playRound():
    global detailFile

    if Global.WAY_TO_PLAY == 1:
        writeTo = 'We are using the playing with odds method' + "\n" + 'This is like calculating the remaining cards and determine if it is best to hit' + "\n"
        detailFile.write(writeTo)
        print(writeTo)

    else:
        if Global.WAY_TO_PLAY == 2:
            writeTo = 'We are using the playing random method' + "\n" + 'This is like flipping a coin where we generate a random number and determine if we should continue or not' + "\n"
            print(writeTo)
            detailFile.write(writeTo)
        else:
            writeTo = 'We are using the playing normal method' + "\n" + 'This is a set of predefined way that the player can play Black Jack' + "\n"
            print(writeTo)
            detailFile.write(writeTo)

    writeTo = 'For this detail round, we are using ' + str(
        Global.NUMBER_OF_DECKS) + " decks" "\n" + 'We also have ' + str(Global.NUMBER_OF_PLAYER) + ' players' + "\n"
    print(writeTo)
    detailFile.write(writeTo)

    # Initialize the Dealer for this Simulation
    theDealer = Dealer(None, Global.NUMBER_OF_DECKS)
    
    # Initialize the Player(s) for this simulation
    listOfPlayer = []
    for i in range(Global.NUMBER_OF_PLAYER): # Player number is decided on NUMBER_OF_PLAYER
        player = Player(theDealer, Global.WAY_TO_PLAY ,0.5)
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
        writeTo = 'Player ' + str(j + 1) + ' starts with ' + str(listOfPlayer[j].firstHandCard) + "\n"
        print(writeTo)
        detailFile.write(writeTo)

        listOfPlayer[j].play()
        writeTo = 'Player ' + str(j + 1) + ' ends with' + str(listOfPlayer[j].firstHandCard) + "\n"
        print(writeTo)
        detailFile.write(writeTo)
        if listOfPlayer[j].bust == True:
            writeTo = 'Player ' + str(j + 1) + ' Bust!' + "\n"
            detailFile.write(writeTo)
            print(writeTo)

    # Dealer play until dealer Stand or Bust
    writeTo = 'Dealer starts with ' + str(theDealer.firstHandCard) + "\n"
    detailFile.write(writeTo)
    print(writeTo)

    theDealer.play()
    writeTo = 'Dealer ends with ' + str(theDealer.firstHandCard) + "\n"
    detailFile.write(writeTo)
    print(writeTo)
    if theDealer.bust == True:
        writeTo = 'Dealer Bust!' + "\n"
        detailFile.write(writeTo)
        print(writeTo)
    for j in range(Global.NUMBER_OF_PLAYER):
        if ((np.sum(np.asarray(listOfPlayer[j].firstHandCard)) > np.sum(np.asarray(theDealer.firstHandCard))) and listOfPlayer[j].bust == False) \
                or (theDealer.bust and listOfPlayer[j].bust == False):
            writeTo = 'Player ' + str(j + 1) + ' won!' + "\n"
            detailFile.write(writeTo)
            print(writeTo)
        else:
            if (np.sum(np.asarray(listOfPlayer[j].firstHandCard)) == np.sum(np.asarray(theDealer.firstHandCard))):
                writeTo = 'Player ' + str(j + 1) + ' tied the dealer!' + "\n"
                print(writeTo)
                detailFile.write(writeTo)

            else:
                writeTo = 'Player ' + str(j + 1) + ' lost!' + "\n"
                print(writeTo)
                detailFile.write(writeTo)
    theDealer.collectChip()
    # Remove cards from player and dealer and start empty again
    theDealer.refresh()

main()
playRound()
file.close()
detailFile.close()
