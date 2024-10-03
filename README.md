# 'Eight Puzzle with A* Heuristics'

This project implements solutions for the classic 8-puzzle problem using the A search algorithm* with multiple heuristics. Additionally, it includes pathfinding on a simplified map of Romania using various search strategies, such as Breadth-First Search, Depth-First Search, Iterative Deepening Search, and Uniform Cost Search.

# Problem Overview
8-Puzzle Problem
The 8-puzzle consists of a 3x3 grid with 8 numbered tiles and one blank space. The goal is to move the tiles by sliding them into the blank space to achieve a specific configuration.

The initial state is represented as a tuple of length 9, where each element corresponds to a tile number, and 0 represents the blank space.

For example:

- Initial state: (1, 2, 3, 4, 5, 6, 0, 7, 8)
- Goal state: (1, 2, 3, 4, 5, 6, 7, 8, 0)

 # EightPuzzle example with A*
        # In this example, we'll construct a puzzle with initial state
        #               1 2 3
        #               4 5 6
        #               _ 7 8
        
        # Default goal is (1, 2, 3, 4, 5, 6, 7, 8, 0)
        #   which represents:   1 2 3
        #                       4 5 6
        #                       7 8 _
        #
    
# Romania Map Problem
A simplified version of the Romania map is represented as an undirected graph. The task is to find the shortest route between cities using various search strategies. Example problems involve finding routes from Zerind to Bucharest and from Oradea to Hirsova.

# Features
A Search on the 8-Puzzle Problem:*

Solve the 8-puzzle using A* search with:
- The default heuristic (number of misplaced tiles).
- Custom heuristic: Manhattan Distance.

Pathfinding on Romania Map (searches for finding routes):
- Breadth-First
- Depth-First
- Iterative Deepening

Uniform Cost and A* searches with statistical analysis using InstrumentedProblem.

# Project Structure
- eight_puzzle_init: Solves an 8-puzzle with the default heuristic.
- eight_puzzle_init_goal: Solves an 8-puzzle with a custom initial and goal state.
- eight_puzzle_with_manhattan_distance_heuristic: Implements a new heuristic function using Manhattan Distance and runs A* search.
- comparing_heuristics: Compares the default heuristic and Manhattan Distance heuristic, providing timing results for optimal solutions of different lengths.
- romania_map_bfs: Tracks the stats of a Breadth-First search for a route from Zerind to Bucharest.
- romania_map_bfs_dfs_ids: Compares Breadth-First, Depth-First, and Iterative Deepening searches.
- romania_map_ids_uc_astar: Compares Iterative Deepening, Uniform Cost, and A* search for a route from Oradea to Hirsova.
