## Maximizer attempts to get the highest capture score
import GameRules
import random

def name():
    return 'Max'

# Returns a random legal move 
def getMove(state):
    # State has Turn(curr player), darkCapture, lightCapture, Board
    ## Returns move
    currPlayer = state['Turn']
    if currPlayer == 'Light':
        #Maximizer
        bestValue = float('-inf')

    else:
        #Minimizer
