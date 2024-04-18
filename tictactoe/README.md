#Notes for week 0 tictactoe

Task is to complete the outstanding functions in tictactoe.py
- Player, actions, result, winner, terminal, utility and minimax

## player
takes $board$ as input, returns either X or O depending on whose turn it is.
Logic
- X goes first
- if count(x) > count(o) then o's turn
- if count(o) > count(x) then something has gone wrong
- if count(x) == count(o) then x's turn

so, if count(x)>count(o) then o, but otherwise x.

Note that board.count() doesn't work as intended. Need to loop through each row in the board (it is a 3x3 list)

## actions
returns a set of all possible actions that can be taken on a given board
each action should be represented as a tuple (i,j) where i is the row, j is the cell in that row
possible moves are any cells on the board that do not have an x or o in them
any return value is acceptable if a temrinal board is provided as input

```python
return {(i,j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell is None}
```

## result
takes board and action as input. Return new board state without modifying original board
raise exception if action not valid
returned board is the board that would result from:

- take original input board
- let play whose turn it is make their move
- at the cell indicated by the input action
- make deep copy of the baord first >> import from copy import deepcopy

```python
    new = deepcopy(board)
    if action in actions(board):
        new[action[0]][action[1]] = player(board)
    else:
        raise ValueError("Invalid move")
    return new
```

## winner
- need to check all rows
-- in any row, just need to return the first cell if they are all the same and they do not equal none.
- need to check all columns
-- in any column, just need to return the first cell if they are all the same and they do not equal none.
- need to check diagonals
-- both top left -> bottom right; and, bottom left -> top right.

## terminal
takes board as input
returns true if game is over (won, no available moves) otherwise false

## utility
return -1, 0 or 1 depending on terminal state of game and whether X/O wins or it is a draw.

## minimax
Pseudo Code:
- Given a state $s$:
-- (max player turn) MAX picks action $a$ in ACTIONS($s$) that produces the highest value of MIN-VALUE(RESULT($s, a$)). The reference to MIN-VALUE(RESULT($s, a$)) is the reference to what is the min player going to choose in their next turn, given by choice of $s$ to minimise the outcome.
-- (min player turn) MIN picks an action $a$ in ACTIONS($s$) that produces the smallest value of MAX-VALUE(RESULT($s, a$))
-- We then turn to considering the MIN-VALUE / MAX-VALUE functions. How do you calculate the value of a state if you are trying to minimise/maximise the value.

So, for min-value:
if TERMINAL($state$): 
        return UTILITY($state$) 
    $v = ∞$ (want value to be as low as possible) 
    for $action$ in ACTIONS($state$): (minimise score given what opponent can do next) 
        $v$ = min($v$, MAX-VALUE(RESULT($state,action$))) 
    return $v$ 

for max-value:
if TERMINAL($state$):
    return UTILITY($state$)
    $v = -∞$ (want value to be as high as possible)
    for $action$ in ACTIONS($state$):
        $v$ = max($v$, MIN-VALUE(RESULT($state,action$)))
    return $v$

for the minimax() function:
- check the current player. If it is X then:
    $v$ = -∞$$
    loop through all actions for the given board
        set k to min_value for the resulting board given (board, action)
        if k > v
            v = k
            best move = action
            if v == 1:  
                break
- if O, then v = + infinity; k = max_value; if k < v; if v== -1

## alpha-beta pruning
- need to keep track of alpha (highest) and beta (lowest) values that X (maximizing) and O (minimizing) can guarantee
- update alpha when exploring X; update beta when exploring O;
- if, at any point, alpha >= beta, then stop because opponent would not allow game to reach that state.

so:
```current_player = player(baord)
best_move = None
alpha = -inf
beta = inf

for X:
k = min_value(result(board, action), alpha, beta)
if k > v:
    v = k
    best_move = action
alpha = max(alpha, v)
if alpha >= beta:
    break

for O (as above, but add):
k = max_value(result(board, action), alpha, beta)
...
beta = min(beta, v)
if alpha >= beta:
    break
```