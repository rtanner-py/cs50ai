"""
Example maze file:
#####B#
##### #
####  #
#### ##
     ##
A######
"""

import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier(): 
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node) #last in- first out

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1] #last
            self.frontier = self.frontier[:-1] #can combine these two lines with .pop
            return node
        
class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:] #first in, first out
            return node
        
class Maze():
    def __init__(self, filename):
        # A represents start, B is the end

        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("Maze must only have 1 start point")
        if contents.count("B") != 1:
            raise Exception("Maze must only have 1 end point")
        
        # determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # keep track of walls
        self.walls = []
        for i  in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i,j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        self.solution = None
    
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("#", end="")
                elif (i,j) == self.start:
                    print("A", end="")
                elif (i,j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i,j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()
    
    def neighbours(self, state):
        row, col = state
        candidates = [
            ("up", (row-1, col)),
            ("down", (row+1, col)),
            ("left", (row, col-1)),
            ("right", (row, col+1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r,c)))
        return result

    def solve(self):
        self.num_explored = 0
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier() #DFS
        frontier.add(start)

        self.explored = set()

        while True:
            if frontier.empty():
                raise Exception("No Solution")
        
            node = frontier.remove()
            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
        
            self.explored.add(node.state)

            for action, state in self.neighbours(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        img = Image.new("RGBA", (self.width * cell_size, self.height * cell_size), "black")
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    fill = (40,40,40)
                elif (i,j) == self.start:
                    fill = (255,0,0)
                elif (i,j) == self.goal:
                    fill = (0,171,28)
                elif solution is not None and show_solution and (i,j) in solution:
                    fill = (220,235,113)

                elif solution is not None and show_explored and (i,j) in self.explored:
                    fill = (212,97,85)

                else: 
                    fill = (237,240,252)

                draw.rectangle(
                    ([
                        (j* cell_size + cell_border, i * cell_size + cell_border),
                        ((j+1) * cell_size - cell_border, (i+1) * cell_size - cell_border)
                        ]),
                        fill=fill
                ) 
        img.save(filename)

if len(sys.argv) != 2:
    sys.exit(f"usage: python {__name__} maze.txt")

m = Maze(sys.argv[1])
print("Maze: ")
m.print()
print("Solving")
m.solve()
print(f"States explored: {m.num_explored}")
print("Solution: ")
m.print()
m.output_image("maze.png", show_explored=True)
                
                