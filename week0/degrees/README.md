# Notes to accompany my implementation of degrees.py

## General
People.csv -> id, name, birthyear
movies -> id, title, year
stars -> person_id, movie_id

Person is the state, movie is the action.
Want to move from source state to target state
Transition is via the movies that link them.

shortest_past needs to return a list of tuples (movie_id, person_id)
for example, [(1,2),(3,4)] would mean that:
- $source$ stared in movie 1 with person 2;
- person 2 stared in movie 3 with person 4

neighbors_for_person(id) returns a tuple (movie_id, person_id) for all people that stared in the movie with movie_id

## StackFrontier

Did this one first. It was a pretty simple implementation where the code largely followed the example code from the lecture. 
Note that util.py contains the boiler plate for Node, Stack and Queue Frontier along with their methods
This iteration checked the the state/target when the node was popped from the stack.

## QueueFrontier
Switched to QueueFrontier for the second iteration and implemented a check on the state/target when the node
is added to the stack. 
Ran into a problem with the len(path) == 0, which comes up when source == target (this wasn't a problem
with the first iteration because the source would have been popped from the stack before checking.

General observation is that this was similar to the implementation of a node in C for the hashing exercises.

