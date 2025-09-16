## MiniMax with alpha-beta pruning (removes branches of searching if unnecessary)
import GameRules
import random

def name():
    return 'Max'

# Returns a random legal move 
def getMove(state):
    # State has Turn(curr player), darkCapture, lightCapture, Board
    ## Returns move
    currPlayer = state['Turn']
    legalMoves = GameRules.getAllLegalMoves(state)
    alpha = float('-inf')
    beta = float('inf')
    
    if currPlayer == 'Light':
        #Maximizer
        bestValue = float('-inf') ## this is so that any score will be higher and get replaced automatically
        for move in legalMoves:
            tempState = GameRules.playMove(GameRules.copyState(state),move) #makes a temp board and tries a legal move w/o affecting real board
            tempVal = getMove(tempState) 
    else:
        #Minimizer
        bestValue = float('inf') ## this is so that any score will be lower, 
        alpha = float()