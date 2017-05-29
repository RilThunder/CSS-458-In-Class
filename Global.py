"""""
Global Variable to be used in Blackjack Simulation.
Variables are first declared in here, and is used in various classes.
These are the initial value, but can be changed during the simulation.
"""""

NUMBER_OF_PLAYER = 4   # Number of Players participating the simulation
STARTING_CHIPS = 500   # Starting chips beginning of every simulation per Player
NUMBER_OF_DECKS = 2    # Number of decks used for the simulation
BUY_IN = 10            # Minimum Bet to play the blackjack
MAX_BET =  100         # The maximum bet per 1 round of game
NUMBER_OF_SIMULATION = 40  # Number of Simulation to be done
NUMBER_OF_ROUNDS = 50  # Number of rounds per simulation
DEALER_SOFT_SEVENTEEN = True  # Assign soft17 rule for the Dealer
WAY_TO_PLAY = 1  # 3 ways to play. 1 = Play with odds. 2 = play randomly. 3 = play in a normal way
CHANCE_TO_DOUBLE = 0.25  # Used to determine when the play should double in play random
CHANCE_TO_HIT = 0.5  # Used to determine when the play should hit in play random
BASE_CONFIDENT = 0.5  # affect how the player will bet

