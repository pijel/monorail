class InvalidMoveException(Exception):
    pass

class Coordinates:
    def __init__(self, x, y):
        self.x, self.y = x,y
    
    def __add__(self, other):
        return Coordinates(self.x+other.x, self.y+other.y)
        
    def __sub__(self, other):
        return Coordinates(self.x-other.x, self.y-other.y)
        
    def __neg__(self):
        return Coordinates(-self.x, -self.y)
        
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def __repr__(self):
        return "({},{})".format(self.x, self.y)
        
    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y
        
    def __hash__(self):
        return hash((self.x, self.y))
        
    def copy(self):
        return Coordinates(self.x, self.y)
        
class Tile:
    def __init__(self, opening_one, opening_two):
        self.openings = opening_one, opening_two
        assert self.openings[0] in DIRECTIONS
        assert self.openings[1] in DIRECTIONS
    
    def __str__(self):
        return str(self.openings[0]) + str(self.openings[1])
    
    def __repr__(self):
        return str(self.openings[0]) + str(self.openings[1])
    
    def __eq__(self, other):
        return self.openings == other.openings or self.openings[::-1] == other.openings
        
    def __hash__(self):
        return hash(self.openings)
        
UP = Coordinates(0,1)
RIGHT = Coordinates(1,0)
DOWN = Coordinates(0,-1)
LEFT = Coordinates(-1,0)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

class Grid:
    def __init__(self):
        # may want to generalise in future to allow arbitrary starting boards
        self.grid = {}
        self.grid[Coordinates(0,0)] = Tile(LEFT, RIGHT)
        self.grid[Coordinates(1,0)] = Tile(LEFT, RIGHT)
        
    def __str__(self):
        return str(self.grid)
        
    def __repr__(self):
        return str(self.grid)
        
    def is_valid_move(self, tile, pos):
        """ return true iff placing the given tile at position pos is valid """
        # check that there's no tile at that position yet
        if self.has_tile_at(pos): return False
        # return true if the tile connects to another tile properly
        for o in tile.openings:
            if self.has_tile_at(pos+o) and -o in self.grid[pos+o].openings: return True
        return False
        
    def make_move(self, tile, pos):
        if not self.is_valid_move(tile, pos): raise InvalidMoveException
        else: self.grid[pos] = tile
        
    def is_closed(self):
        """ returns true iff all tiles together form a single closed track by walking from tile to tile along valid connexions """
        if len(self.grid) < 8: return False
        stack = list(self.grid)
        # we need to store the initial position in order to check whether the last position links to it
        init = stack[0]
        current_pos = init
        next_found = True
        # walk to the next connected tile while we can
        while next_found:
            # once we've visited a tile we need to remove it from the stack so that we don't accidentally revisit it from the next tile
            stack.remove(current_pos)
            next_found = False
            for o in self.grid[current_pos].openings:
                next_pos = current_pos+o
                if next_pos in stack:
                    next_found = True
                    current_pos = next_pos
                    break
        # return true iff we have visited all tiles and we can walk from current_pos to init, as that implies the track is closed
        return not stack and init-current_pos in self.grid[current_pos].openings
    
    def has_tile_at(self, coord):
        return coord in self.grid
 
 
 ### TESTS #### 

# construct smallest possible closed track
# G = Grid()
# G.make_move(Tile(UP,LEFT), Coordinates(2,0))
# G.make_move(Tile(DOWN,LEFT), Coordinates(2,1))
# G.make_move(Tile(RIGHT,LEFT), Coordinates(1,1))
# G.make_move(Tile(RIGHT,LEFT), Coordinates(0,1))
# G.make_move(Tile(RIGHT,DOWN), Coordinates(-1,1))
# G.make_move(Tile(RIGHT,UP), Coordinates(-1,0))
# print G.is_closed()