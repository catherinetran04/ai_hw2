import sys
sys.path.append('aima-python')
from search import *
import math
import time

class EightP:

    def __init__(self):
        pass

    def eight_puzzle_init(self):
        '''
        1. create an instance of the 8-puzzle with initial state (1, 2, 3, 4, 5, 6, 0, 7, 8) 
        2. check solbaility and run A* search on it with the default heuristic
        2. return the solution from the A* search algorithm
        '''
        init = (1, 2, 3, 4, 5, 6, 0, 7, 8)
        puzzle = EightPuzzle(init)
        print("Is the puzzle solvable from this initial state?")
        print(puzzle.check_solvability(init))
        print("A* with default heuristic")
        return astar_search(puzzle).solution()

    
    
    def eight_puzzle_init_goal(self):
        '''
        1. create an instance of the 8-puzzle with initial state (0, 6, 2, 1, 5, 3, 4, 8, 7) 
        and goal state (1, 2, 3, 8, 0, 4, 7, 6, 5) and run A* search on it with the default heuristic
        2. return the solution from the A* search algorithm
        '''
        init =  (0, 6, 2, 1, 5, 3, 4, 8, 7) 
        goal =   (1, 2, 3, 8, 0, 4, 7, 6, 5)
        puzzle = EightPuzzle(init,goal)
        return astar_search(puzzle).solution() 

    def eight_puzzle_with_manhattan_distance_heuristic(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem 
        2. write code that will create a different heuristic
        3. return the solution from the A* search algorithm
        '''
        
        init = (0, 6, 2, 1, 5, 3, 4, 8, 7)
        goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)
        puzzle = EightPuzzle(init, goal)
        node = Node(init)
        def mhd(node):
            init = node.state
            '''Define your manhattan-distance heuristic for the 8-puzzle here
            '''
            sum = 0
            for num in range (1,9):
                for i in range (0,9):
                    if (num == init[i]):
                        for j in range (0,9):
                            if (num == goal[j]):
                                dist = abs((j%3)-(i%3)) + abs((j//3)-(i//3))
                sum = sum + dist
            return sum
        return astar_search(puzzle, mhd).solution()

    def comparing_heuristics(self):
        '''
        1. find initial states with optimal solutions of lengths 18, 20, 22 and 24
        2. for each of those, for each heuristic measure the time it takes to find a solution

        Find four initial states that have optimal solutions of lengths 18, 20, 22 and 24
        For each of these, run A* search using the  default heuristic and your heuristic
        Use a python function or unix utility to time the length of each of the runs.
        In your writeup, create a table with the eight timing results. 
        '''
        goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        init18 = (1, 3, 2, 4, 6, 5, 7, 8, 0)
        puzzle18 = EightPuzzle(init18)
        node = Node(init18)

        # same as above
        def mhd(node):
            init = node.state
            '''Define your manhattan-distance heuristic for the 8-puzzle here
            '''
            sum = 0
            for num in range (1,9):
                for i in range (0,9):
                    if (num == init[i]):
                        for j in range (0,9):
                            if (num == goal[j]):
                                dist = abs((j%3)-(i%3)) + abs((j//3)-(i//3))
                sum = sum + dist
            return sum


        print (len(astar_search(puzzle18).solution()))
        #default_time = time.time()
        #manhattan_time = time.time()
        print (astar_search(puzzle18).solution()) 
        print (astar_search(puzzle18, mhd).solution())
        #print (default_time, manhattan_time)
        print('==================')
        return 0



    def romania_map_bfs(self):
        '''Use the InstrumentedProblem class to track stats about a breadth-first
        search on the Romania Map problem.
        '''
        g = InstrumentedProblem(GraphProblem('Zerind', 'Bucharest', romania_map))
        result = breadth_first_graph_search(g)
        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")
        print(g)
        return g

    def romania_map_bfs_dfs_ids(self):
        '''Use the InstrumentedProblem class to track stats about 
        different searches on the Romania Map problem.
        '''
        g1 = InstrumentedProblem(GraphProblem('Zerind', 'Bucharest', romania_map))
        g2 = InstrumentedProblem(GraphProblem('Zerind', 'Bucharest', romania_map))
        g3 = InstrumentedProblem(GraphProblem('Zerind', 'Bucharest', romania_map))
        bf = breadth_first_graph_search(g1)
        df = depth_first_graph_search(g2)
        ids = iterative_deepening_search(g3)
        print("   Su   Go   St")
        print(g1)
        print(g2)
        print(g3)
        return (g1, g2, g3)

    def romania_map_ids_uc_astar(self):
        '''Use the InstrumentedProblem class to track stats about
        different searches on the Romania Map problem.
        '''
        g1 = InstrumentedProblem(GraphProblem('Oradea', 'Hirsova', romania_map))
        g2 = InstrumentedProblem(GraphProblem('Oradea', 'Hirsova', romania_map))
        g3 = InstrumentedProblem(GraphProblem('Oradea', 'Hirsova', romania_map))
        ids = iterative_deepening_search(g1)
        uc = uniform_cost_search(g2)
        ast = astar_search(g3)
        print("   Su   Go   St")
        print(g1)
        print(g2)
        print(g3)
        return (g1, g2, g3)


def main():
    
    # Create object, ep, of datatype EightP.
    ep = EightP()
 
    #=======================
    # A* with 8-Puzzle 
    # An example for you to follow to get you started on the EightPuzzle
    print('Eight puzzle with only initial state input:')
    print('=======================')
    print(ep.eight_puzzle_init())

    print('Eight puzzle given intitial state and goal:')
    print('==================')
    print(ep.eight_puzzle_init_goal())

    print('Problem 1d result:')
    print('==================')
    print(ep.eight_puzzle_with_manhattan_distance_heuristic())

    print('Problem 1e result:')
    print('==================')
    print(ep.comparing_heuristics())

    print('Problem 2 example')
    print('==================')
    print(ep.romania_map_bfs())

    print('Problem 2a result:')
    print('==================')
    print(ep.romania_map_bfs_dfs_ids())

    print('Problem 2b result:')
    print('==================')
    print(ep.romania_map_ids_uc_astar())

    
if __name__ == '__main__':
    main()
