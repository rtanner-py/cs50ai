# implementing solution to question 4
from itertools import product

domains = {
    'A': {'mon','tue','wed'},
    'B': {'tue'},
    'C': {'mon','tue','wed'},
    'D': {'mon','tue','wed'},
    'E': {'mon','tue','wed'},
    'F': {'wed'},
    'G': {'mon','tue','wed'},
}

constraints = {
    ('A','B'),
    ('B','C'),
    ('B','D'),
    ('C','E'),
    ('C','F'),
    ('D','E'),
    ('F','G'),
}

def satisfy_constraints(assignment):
    for (x, y) in constraints:
        if x in assignment and y in assignment and assignment[x] == assignment[y]:
            return False
    return True

def backtraining(assignment, variables):
    if len(assignment) == len(variables):
        return assignment

    unassigned = [v for v in variables if v not in assignment]
    first = unassigned[0]

    for value in domains[first]:
        local_assignment = assignment.copy()
        local_assignment[first] = value

        if satisfy_constraints(local_assignment):
            result = backtraining(local_assignment, variables)
            if result is not None:
                return result
    
    return None

variables = ['A','B','C','D','E','F','G']
solution = backtraining({}, variables)

if solution:
    for variable, value in solution.items():
        print(f"{variable}: {value}")

else:
    print("No solution")