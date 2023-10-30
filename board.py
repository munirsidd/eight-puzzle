#
# A Board class for the Eight Puzzle
#

from math import sqrt

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = digitstr[3 * r + c]
                if self.tiles[r][c] == '0':
                   self.blank_r = r
                   self.blank_c = c

    def __repr__(self):
        """ returns a string representation of the Board object self """
        s = ''
        
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    s += '_' + ' '
                else:
                    s += self.tiles[r][c] + ' '
            s += '\n'
       
        return s
        
    def move_blank(self, direction):
        """ returns true and modifies the contents of the Board object self
            specified by direction if possible
        """
        if direction == 'up':
            new_blank_r = self.blank_r - 1
            new_blank_c = self.blank_c
        elif direction == 'down':
            new_blank_r = self.blank_r + 1
            new_blank_c = self.blank_c
        elif direction == 'left':
            new_blank_r = self.blank_r
            new_blank_c = self.blank_c - 1
        elif direction == 'right':
            new_blank_r = self.blank_r
            new_blank_c = self.blank_c + 1
        else:
            return False
        
        if new_blank_r < 0 or new_blank_r > 2 or \
           new_blank_c < 0 or new_blank_c > 2:
               return False
         
        if direction == 'up':
            self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r - 1][self.blank_c]
            self.tiles[new_blank_r][new_blank_c] = '0'
        elif direction == 'down':
            self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r + 1][self.blank_c]
            self.tiles[new_blank_r][new_blank_c] = '0'
        elif direction == 'left':
            self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c - 1]
            self.tiles[new_blank_r][new_blank_c] = '0'
        elif direction == 'right':
            self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c + 1]
            self.tiles[new_blank_r][new_blank_c] = '0'
            
        self.blank_r = new_blank_r
        self.blank_c = new_blank_c
        return True
    
    def digit_string(self):
        """ creates and returns a string of digits that corresponds to 
            the current contents of the called Board object's tiles attribute
        """
        s = ''
        
        for r in range(3):
            for c in range(3):
                s += self.tiles[r][c]
        
        return s
    
    def copy(self):
        """ returns a newly-constructed Board object that is
            a deep copy of the called object self
        """
        return Board(self.digit_string())
    
    def num_misplaced(self):
        """ returns the number of tiles that are misplaced excluding
            the blank cell in the Board object self
        """
        count = 0
        
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != GOAL_TILES[r][c]:
                    if self.tiles[r][c] != '0':
                        count += 1
        return count
    
    def distance_misplaced(self):
        """ returns the sum of the distances of each misplaced tile from the goal position
            excluding the blank tile in the Board object self
        """
        goal_row = 0
        goal_col = 0
        dist = 0
        
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != GOAL_TILES[r][c]:
                    if self.tiles[r][c] != '0':
                        for i in range(3):
                            for j in range(3):
                                if GOAL_TILES[i][j] == self.tiles[r][c]:
                                    goal_row = i
                                    goal_col = j
                        dist += sqrt((goal_row - r)**2 + (goal_col - c)**2)
        return dist
                        
    def __eq__(self, other):
        """ returns True if the called object self and the argument other
            have the same values for the titles attribute
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False