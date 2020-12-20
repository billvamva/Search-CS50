"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

class Board:
    def __init__(self, state, x, o):
        self.state = state
        self.x = x
        self.o = o
    
    def return_state(self):
        return self.state
    
    def get_turn(self):
        if self.x == self.o:
            return X
        else:
            return O

def initial_state():
    """
    Returns starting state of the board.
    """
    s = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
    return s


def player(board):
    return board.get_turn()
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board.state[i][j] == None:
                actions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    legal = actions(board)
    if action not in legal:
        return 'Move is not possible' 
    if player(board) == X:
        board.state[i][j] = X
        board.x += 1
        return board.state
    else:
        board.state[i][j] = O
        board.o += 1 
        return board.state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        if board.x > board.o:
            return X
        else:
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
            if board.state[i][j] == X:
                set_x.add((i,j))
            elif board.state[i][j] == O:
                set_o.add((i,j))
    set_win = {frozenset([(0,0),(1,0),(2,0)]), frozenset([(0,0), (0,1), (0,2)]), 
    frozenset([(1,0), (1,1), (1,2)]), frozenset([(2,0), (2,1), (2,2)]), 
    frozenset([(0,0), (1,2), (2,2)]), frozenset([(0,0), (0,1), (0,2)]),
    frozenset([(0,2), (1,2), (2,2)]), frozenset([(0,0), (0,1), (0,2)]),
    frozenset([(0,0), (0,1), (0,2)]), frozenset([(0,0), (1,1), (2,2)]),
    frozenset([(0,2), (1,1), (2,0)])}

    for win in set_win:
        if win.issubset(set_x) or win.issubset(set_o):
            return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


if __name__ == "__main__":
    s = initial_state()
    board = Board(s, 0, 0)
    board.state[0][1] = X
    board.x += 1
    board.state[0][0] = X
    board.x += 1
    board.state[0][2] = X
    board.x += 1

    print(board.state)
    print(terminal(board))
    print(winner(board))