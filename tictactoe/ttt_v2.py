"""
Tic Tac Toe Player
With AB-Pruning
"""
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = count_o = 0
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    return O if count_x > count_o else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i,j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell is EMPTY}



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new = deepcopy(board)
    if action in actions(board):
        new[action[0]][action[1]] = player(board)
    else:
        raise ValueError("Invalid move")
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    blank = 0
    for row in board:
        if EMPTY in row:
            blank += row.count(EMPTY)
    if blank == 0 or winner(board) is not None:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        if winner(board) == O:
            return -1
        else:
            return 0


def minimax(board, depth=math.inf):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    best_move = None
    alpha = -math.inf
    beta = math.inf

    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action), alpha, beta, depth-1)
            #print(f"Current action {action} | current k {k} | current v {v}")
            #print(f"Current alpha {alpha} | current beta {beta}")
            if k > v:
                v = k
                best_move = action
            alpha = max(alpha, v)
            if alpha >= beta or depth <= 0:
                break
    else:
        v = math.inf
        for action in actions(board):
             #print(f"Current action {action} | current k {k} | current v {v}")
            #print(f"Current alpha {alpha} | current beta {beta}")
            k = max_value(result(board, action), alpha, beta, depth -1)
            if k < v:
                v = k
                best_move = action
            beta = min(beta, v)
            if alpha >= beta or depth <= 0:
                break
    return best_move

def max_value(board, alpha, beta, depth):
    if terminal(board) or depth <= 0:
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta, depth - 1))
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v

def min_value(board, alpha, beta, depth):
    if terminal(board) or depth <= 0:
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta, depth -1))
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v