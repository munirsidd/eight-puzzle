#
# driver/test code for state-space search on Eight Puzzles   
#

from searcher import *
from timer import Timer

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def print_solution_steps(solution):
    """ Prints the sequence of moves that lead from the initial state to the 
        solution state 
    """
    print('Found a solution requiring', solution.num_moves, 'moves.')
    show_steps = input('Show the moves (y/n)? ')
    if show_steps == 'y':
        solution.print_moves_to()

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher is None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()

    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln is None:
        print('Failed to find a solution.')
    else:
        print_solution_steps(soln) 

def process_file(filename, algorithm, param):
    """ uses a loop to process the file one line at a time """
    file = open(filename, 'r')
    
    num_moves = 0
    num_tested = 0
    num_solved = 0
    num_puzzles = 0
    for line in file:
        if line[-1] == '\n':
            digit_str = line[:-1]
        else:
            digit_str = line
        init_board = Board(digit_str)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        num_puzzles += 1
        if searcher == None:
            return
        
        print(digit_str + ': ', end = '')
        soln = None
        try:
            soln = searcher.find_solution(init_state)
        except KeyboardInterrupt:
            print('search terminated, ', end='')
            
        num_tested += searcher.num_tested 
        if soln == None:
            print('no solution')
        else:
            print(soln.num_moves, 'moves,', searcher.num_tested, 'states tested')
            num_solved += 1
            num_moves += soln.num_moves
            
    print()
    print('solved', num_solved, 'puzzles')
    if num_solved != 0:
        print('averages:', num_moves/num_solved, 'moves,', num_tested/num_puzzles, 'states tested')
        
    file.close()