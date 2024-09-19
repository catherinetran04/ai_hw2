# 'Eight Puzzle with A* Heuristics'

""" The problem of sliding tiles numbered from 1 to 8 on a 3x3 board, where one of the
    squares is a blank. A state is represented as a tuple of length 9, where  element at
    index i represents the tile number  at index i (0 if it's an empty square) """

 #EightPuzzle example with A*
        # Default goal is (1, 2, 3, 4, 5, 6, 7, 8, 0)
        #   which represents:   1 2 3
        #                       4 5 6
        #                       7 8 _
        #

        # In this example, we'll construct a puzzle with initial state
        #               1 2 3
        #               4 5 6
        #               _ 7 8
        #



Problem 1. (40 points)
For problem 1, make alterations to the given python module. Use the example problem
function as a guide for how to create an instance of the 8-puzzle and what should be returned.

b. In the function problem 1b, create an instance of the 8-puzzle with initial state (1, 4,
2, 6, 7, 3, 0, 8, 5) and goal state (1, 2, 3, 8, 0, 4, 7, 6, 5) and run A* search on it with
the default heuristic. Return the solution that A* search finds.


d. In the function problem 1d, repeat problem c (including with the different goal state),
but write a new heuristic function that calculates the Manhattan Distance. Manhattan
Distance is the sum of the orthogonal (non-diagonal) distance that each tile is away
from its correct location, ignoring the fact that other tiles are in the way. Return the
solution that A* search finds.
e. For this one, put your answer in your pdf. Find four initial states that have optimal
solutions of lengths 18, 20, 22 and 24. For each of these, run A* search using the
default heuristic and your heuristic. Use a python function or unix utility to time
the length of each of the runs. In your writeup, create a table with the eight timing
results. (Note: When trying to come up with initial states that meet this criteria, it
is acceptable to work with other students in the class. This is the only part of this
homework in which you may collaborate.)

Problem 2. (30 points)
For problem 2, make alterations to the given python module. These questions use the
simplified map of Romania from the textbook. An undirected graph representation of that
map can be found in the search.py module. Use example problem 2 function as a guide for
how to create a version of the pathfinding problem and track statistics about it.
a. Create a version of the problem that will find a route from Zerind to Bucharest. Using
the InstrumentedProblem class, create three separate instances of the problem and
run Breadth-First Graph search, Depth-First Graph search and Iterative Deepening
search on them. Return your result in the form of a tuple of the three Problem objects.
1
CSCI4511W-02 - Homework 2 October 4, 2022
b. Create a version of the problem that will find a route from Oradea to Hirsova. Using
the InstrumentedProblem class, create three separate instances of the problem and
run Iterative Deepening, Uniform Cost and A* search on them. Return your result in
the form of a tuple of the three Problem objects.
