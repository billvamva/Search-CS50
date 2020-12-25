"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    initial = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
    return initial


def player(board):
    no_x = 0
    no_o = 0
    
    if terminal(board):
        return None
    

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                no_x += 1
            
            if board[i][j] == O:
                no_o += 1
    
    if no_x > no_o:
        return O
    else:
        return X

    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    res_board =  copy.deepcopy(board)   
 
    if player(board) == X:
        res_board[i][j] = X
        return res_board
    else:
        res_board[i][j] = O
        return res_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    set_x = set()
    set_o = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                set_x.add((i,j))
            elif board[i][j] == O:
                set_o.add((i,j))
    
    set_win = {frozenset([(0,0),(1,0),(2,0)]), frozenset([(0,0), (0,1), (0,2)]), 
    frozenset([(1,0), (1,1), (1,2)]), frozenset([(2,0), (2,1), (2,2)]), 
    frozenset([(0,2), (1,2), (2,2)]), frozenset([(0,0), (1,1), (2,2)]), 
    frozenset([(0,2), (1,1), (2,0)]), frozenset([(0,1), (1,1), (2,1)])}

    for win in set_win:
        if win.issubset(set_x):
            return X
        if win.issubset(set_o):
            return O
    return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    set_x = set()
    set_o = set()


    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                set_x.add((i,j))
            elif board[i][j] == O:
                set_o.add((i,j))
    
    set_win = {frozenset([(0,0),(1,0),(2,0)]), frozenset([(0,0), (0,1), (0,2)]), 
    frozenset([(1,0), (1,1), (1,2)]), frozenset([(2,0), (2,1), (2,2)]), 
    frozenset([(0,2), (1,2), (2,2)]), frozenset([(0,0), (1,1), (2,2)]), 
    frozenset([(0,2), (1,1), (2,0)]), frozenset([(0,1), (1,1), (2,1)])}

    for win in set_win:
        if win.issubset(set_x) or win.issubset(set_o):
            return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 10
    elif winner(board) == O:
        return -10
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(state, depth):
        if terminal(state):
            return utility(state) - depth
        bestVal = float('-inf')
        for action in actions(state):
            actionVal = min_value(result(state,action), depth + 1) 
            bestVal = max(bestVal, actionVal) 
        return bestVal

    def min_value(state, depth):
        if terminal(state):
            return utility(state) + depth
        bestVal = float('inf')
        for action in actions(state):
            actionVal =  max_value(result(state, action), depth + 1)
            bestVal = min(bestVal,actionVal)
        return bestVal   


    if player(board) == X:
        bestVal = float('-inf')
        bestAction = None
        for action in actions(board):
            actionVal = min_value(result(board,action), 0)
            if  actionVal > bestVal:
                bestVal = actionVal
                bestAction = action
        return bestAction
    
    elif player(board) == O:
        bestVal = float('inf')
        bestAction = None
        for action in actions(board):
            actionVal = max_value(result(board,action), 0)
            if actionVal < bestVal:
                bestVal = actionVal
                bestAction = action
        return bestAction



if __name__ == "__main__":
    pass

