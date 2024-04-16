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

## terminal

## utility

## minimax