#
# classes for objects that perform state-space search on Eight Puzzles  
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    def __init__(self, depth_limit):
        """ initializes attributes """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def add_state(self, new_state):
        """ adds the State object new_state to the
            Searcher's list of untested states
        """
        self.states += [new_state]
    
    def should_add(self, state):
        """ returns True if the called Searcher self should
            add state to its list of untested states
        """
        if (self.depth_limit != -1 and state.num_moves > self.depth_limit) or \
           (state.creates_cycle() == True):
               return False
        else:
            return True
        
    def add_states(self, new_states):
        """ takes a list of State objects new_states and processes
            the elements of new_states one at a time
        """
        for new_state in new_states:
            if self.should_add(new_state) == True:
                self.add_state(new_state)

    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """ performs a full state-space search that begins at init_state 
            and ends when the goal state is found or there are no more untested states
        """
        self.add_state(init_state)
        while self.states != []:
            self.num_tested += 1
            s = self.next_state()
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())
        return None

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

class BFSearcher(Searcher):
    """ a class for objects that perform an uninformed breadth-first state-space
        search on an Eight Puzzle
    """
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    """ a class for objects that perform an uninformed depth-first state-space
        search on an Eight Puzzle
    """
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = self.states[-1]
        self.states.remove(s)
        return s
        
def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    """ a heuristic function that takes a state object and returns an estimate 
        of how many additional moves are needed to get from state to the goal state    
    """
    return state.board.num_misplaced()

def h2(state):
    """ a heuristic function that takes a state object and returns an estimate
        of how many additional moves are needed to get from state to the goal state
    """
    return state.board.distance_misplaced()

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    def __init__(self, heuristic):
        """ initializes attributes """
        super().__init__(-1)
        self.heuristic = heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """ adds a sublist containing the priority and state 
            to the list of untested states
        """
        self.states += [[self.priority(state), state]]

    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        best_pair = max(self.states)
        s = best_pair[1]
        self.states.remove(best_pair)
        return s
    
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

class AStarSearcher(GreedySearcher):
    """ A class for objects that perform an informed A* state-space
        search on an Eight Puzzle
    """
    def priority(self, state):
        """ computes and returns the priority of the specified state, based on the heuristic 
            function used by the searcher and the cost already expeded to reach that state
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
    