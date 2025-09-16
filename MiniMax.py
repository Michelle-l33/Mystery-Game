## MiniMax with alpha-beta pruning (removes branches of searching if unnecessary)
import GameRules
import random

def name():
    return 'MiniMax'

#https://www.geeksforgeeks.org/dsa/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/  and chatgpt helped with getMove and minimax
def getMove(state): # State has Turn(curr player), darkCapture, lightCapture, Board
    currPlayer = state['Turn']
    legalMoves = GameRules.getAllLegalMoves(state) #gets all legal moves of the board in its current state

    if not legalMoves:
        return None
    
    alpha = float('-inf') #initializes as -ing and +inf to make sure they can be replaced accordingly.
    beta = float('inf')
    
    if currPlayer == 'Light': #Maximizer
        bestMove = None
        bestValue = float('-inf') ## this is so that any score will be higher and get replaced automatically
        for move in legalMoves:
            tempState = GameRules.playMove(GameRules.copyState(state),move) #makes a temp board and tries a legal move w/o affecting real board
            tempVal = minimax(tempState,alpha,beta) #initializes the recursive searching 
            if tempVal > bestValue: #if the found best value is better than the current one, make that one the best choice
                bestValue = tempVal
                bestMove = move # make this move the optimal choice
            alpha = max(alpha, bestValue) #update the alpha to the current best value that the maximizer could get on its current path
        return bestMove #
    
    else: #Minimizer
        bestMove = None
        bestValue = float('inf') ## this is so that any score will be lower and replace it.
        ## need to copy maximizer but opposite down here


def minimax(state, alpha, beta): #recursively checks through the rest of the possible outcomes of each move
    legalMove2 = GameRules.getAllLegalMoves(state)

    if not legalMoves:
        return None
    
    if state['Turn'] == 'Light': #Max
        currValue = float('-inf')
        for mv in legalMove2:
            tempState2 = GameRules.playMove(GameRules.copyState(state),mv)
            value = max(value, minimax(tempState2, alpha, beta))
            alpha = max(value,alpha)