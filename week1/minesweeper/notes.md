# Minesweeper

## Intro

CS50ai, week 1 - project 2

Task - Write an AI agent that can gather knowledge about the Minesweeper board and select cells that it knows to be save.

Distribution code: [https://cdn.cs50.net/ai/2020/x/projects/1/minesweeper.zip](https://cdn.cs50.net/ai/2020/x/projects/1/minesweeper.zip)

Runner.py contains all the code for the graphical interface.

Minesweeper.py contains all the game logic and code for the AI to play the game. The task is to complete the missing functions in minesweeper.py.

## preamble

A sentence is represented as {A,B,C,D,E,F,G,H} = 1; 
Where each of a,b,c...h is a tuple of (i,j) co-ordinates
The number at the end, "count" represents the number of those cells that are mines.

The example above says that of all these cells, 1 is a mine.

Example 2:

A   B   C
D   E   F
0   G   H

The sentence we can contrust is {D,E,G} = 0.
We therefore know that all of these cells are safe, as none are mines.
Whereever we have a sentence where the count is 0, we can assume that all the cells in the sentence must be safe.

Example 3:
A   B   C
D   E   F
G   H   3

The sentence is {E,F,H} = 3
We therefore know that all the cells are mines.

In general, we want sentences to be able cells that are not yet known about. Once we know the contents of the cells, we can update our sentences to simplify them.

If we have {A,B,C} = 2, and we are then told C is safe, then:
- Remove C from the set and mark it as safe;
- {A,B} = 2, so we know both are mines and they can me updated in the knwon mines.

Alternatively, {A,B,C} = 2. We are told c is a mine:
- Remove C from the set, mark as a mine;
- Decrease the count
- New sentence: {A,B} = 1

Example 4:
1   1   1
A   B   C
D   2   E

We know:
- {A,B,C} = 1
- {A,B,C,D,E} = 2
- We can infer {D,E} = 1

Where we have two sentences (Set 1 = Count 1; Set 2 = Count 2) and set1 is a subset of set 2, then we can construct the new setnence set2-set1 = count2-count1

## To do

### In the Sentence class

- Complete known_mines
-- should return a set of all the cells in self.cells that are known to be mines;
-- Where we have a set of n items ({A,B,C}) and the count is n (ie, len(cells) == cells.count) then we know that the individual cells are mines. Otherwise, we cannot know whether any individual cell is a mine or not, and so we return an empty set.
-- So, check whether len(cells) == cells.count and, if so, return cells. 
-- Note that if len(cells) == 0 and cells.count == 0, then this will still match, but it is not a valid sentence. So need to check that len(cells) > 0 first.
- Complete known_safes
-- Similar to the known_mines, but when len(self.cells) != 0 and cells.count == 0, then we know all the cells in self.cells are safe and can return this as a set.
- Complete mark_mine
-- Need to remove that cell from current sentence (which should only be cells that we currently don't know the value for) and decrease the count by 1 (as there is one less mine for the remaining cells)
-- self.cells.remove(cell) will remove a cell from a sentence (cells is a set)
-- self.count -= 1
- Complete mark_safe
-- as above, but don't need to update the count, just remove the cell.

### In the Minesweeper class

complete add_knowledge
: This is a larger block of coding, so did this last
: Marking the cell as a move made is just adding the cell to self.moves_made
: Marking it as safe is just calling self.mark_safe(cell)
: Adding a new sentence to the AI's KB based on the value of cell and count
: Iterate through all the neighbours of the cell (i-1,j-1)->(i+1,j+1), but remembering to us cell[0]+2 and cell[1]+2 because of how range() works; Also remembering to ignore (i,j) where this is the original cell (the middle one);
: if i,j is a mine, then reduce the count by -1; if it is in safe.safes, self.moves_made, or self.mines then ignore it as we already have knowledge of that cell and a sentence should be constructed of cells that we have no knowledge of;
: Add any remaining cells to temporary set (unknown_neighbours)
: create a new sentence of unknown_neighbours and count;
: Mark any additional cells as safe/mines based on updated KB:
- iterate through existing knowledge. 
- if known_mines (function above) returns a non-empty list, then iterate through the cells in known_mines().copy() (avoid changing the list in place) and mark_mine(cell) for each cell;
- Do the same thing for known_safes()
: Add any new inferred sentences. This applies the subset rule wrong the notes
- Loop through all the sentences in the knowledge and then loop through it again; this gets sentences A and B to compare. If the same sentence is both A and B, then skip;
- If the two are equal, then you can remove one of them as it is a duplicate
- If A is a subset of B, then you can create a new sentence of B - A, B.count - A.count
: Draw any new infereces from the KB after making these changes. This stumped me for a while but, it is as simple as running through the sentence and applying the logic for  for known_mines and known_safes() again.
- because we now have this code twice, we can abstract it into its own function (make_inferences) and call self.make_inferences() to reduce duplication.

Complete make_save_move
: return a known safe cell that isn't a move already made;
: return none if no known safe cell
: we have self.safes which is a set of safe cells. We can iterate through this set and, if it is not in self.moves_made (a set of previously made moves), we can return this. If there are no unexplored safe cells, return None.

Complete make random_move
: compile a list of all unexplored cells that are not mines (checking self.mines, a set of all cells known to be mines) and return a random.choice from this list. Returns none if there are no random moves that can be made.


