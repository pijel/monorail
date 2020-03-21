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
        #self.grid[Coordinates(0,0)] = Tile(LEFT, RIGHT)
        #self.grid[Coordinates(1,0)] = Tile(LEFT, RIGHT)
        self.grid[Coordinates(0,0)] = Tile(DOWN, UP)
        self.grid[Coordinates(0,1)] = Tile(DOWN, UP)
        
    def __str__(self):
        return str(self.grid)
        
    def __repr__(self):
        return str(self.grid)
    
    def boundary(self):
        boundary_tiles = set([])
        for i in self.grid:
            for k in DIRECTIONS:
                boundary_tiles.add(i+k)
        placed_tiles = set([j for j in self.grid])
        return boundary_tiles - placed_tiles
        
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



class DoubleListNode:
    def __init__(self,x):
        self.val = x
        self.prev = None
        self.next = None
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    def add(self,value):
        new_node = DoubleListNode(value)
        if self.first == None and self.last == None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.last
            self.last.prev = new_node
            self.last = new_node
    def remove(self):
        if not self.first:
            return False
        return_value = self.first.val
        self.first = self.first.prev
        return return_value
    def peek(self):
        return self.first.val
    def show(self):
        a = self.first
        while a:
            print (a.val)
            a = a.prev
    def nonempty(self):
        return (self.first != None and self.last != None)

class Tile:
    def __init__(self, opening_one, opening_two):
        self.openings = opening_one, opening_two
        assert self.openings[0] in DIRECTIONS
        assert self.openings[1] in DIRECTIONS
    
    def __str__(self):
        return directionstring(self.openings[0]) + " " +  directionstring(self.openings[1])
    
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

def directionstring(coord):
    if coord == UP:
        return "UP"
    if coord == RIGHT:
        return "RIGHT"
    if coord == DOWN:
        return "DOWN"
    else:
        return "LEFT"



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


possible_tiles = []
for k in range(len(DIRECTIONS)):
    for j in range(k+1,len(DIRECTIONS)):
        new_tile = Tile(DIRECTIONS[j],DIRECTIONS[k])
        possible_tiles.append(new_tile)
#print(possible_tiles)

# !!IMPORTANT!!
# I ran this in Jupyter, meaning that I didn't need to declare global variables and that each of these functions was run seperately. The possible_tiles list is referenced underneath, and you will need to change it if you want to run this as one large script
# !!IMPORTANT!!

def possible_left_to_right():
    answer = []
    q = Queue()
    
    for j in possible_tiles:
        q.add([j])
    
    while q.nonempty():
        current_config = q.remove()
        if valid_left_to_right(current_config):
            answer.append(current_config)
            if len(current_config) < 3:
                for j in possible_tiles:
                    q.add(current_config + [j])
    return answer
  
#you can call possible_left_to_right to see a list of the possible left to right moves given in coordinate form. 
#after the valid_left_to_right function there are more functions that make it easier to read  (which is why I changed __str__ in the tile class)
def valid_left_to_right(tile_list):
    for i in range(len(tile_list)-1):
        if RIGHT in tile_list[i].openings and LEFT not in tile_list[i+1].openings:
            return False
        
    for i in range(1,len(tile_list)):
        if LEFT in tile_list[i].openings and RIGHT not in tile_list[i-1].openings:
            return False
    return True
        

#this function will need to change based on what the direction of the tiles is (i.e horizontal or vertical)


def print_tile_list(tile_list):
    answer = []
    for j in tile_list:
        answer.append(str(j))
    return answer

# coordinates are a little hard to read, so here is a helper function to make it nicer looking


leftright = []
for k in possible_left_to_right():
       leftright.append(print_tile_list(k))
easy_to_read_left_to_right = leftright
#print(easy_to_read_left_to_right)


def valid_down_to_up(tile_list):
    for i in range(len(tile_list)-1):
        if UP in tile_list[i].openings and DOWN not in tile_list[i+1].openings:
            return False
        
    for i in range(1,len(tile_list)):
        if DOWN in tile_list[i].openings and UP not in tile_list[i-1].openings:
            return False
    return True

def possible_down_to_up():
    answer = []
    q = Queue()
    
    for j in possible_tiles:
        q.add([j])
    
    while q.nonempty():
        current_config = q.remove()
        if valid_down_to_up(current_config):
            answer.append(current_config)
            if len(current_config) < 3:
                for j in possible_tiles:
                    q.add(current_config + [j])
    return answer

downup = []
for k in possible_down_to_up():
       downup.append(print_tile_list(k))
easy_to_read_down_to_up = downup





def valid_move( move, grid):
    #move denoted by -  'H' or 'V' for horizontal/vertical, starting coordinate, array of tiles
    
    move_length = len(move[2])
    move_coords = [ move[1] ]
    
    if move[0] == 'H':
        for i in range(move_length-1):
            move_coords.append(move[1] + Coordinates(i+1,0))
    if move[0] == 'V':
        for i in range(move_length-1):
            move_coords.append(move[1] + Coordinates(0,i+1))
            
    #collision
    
    for i in move_coords:
        if i in grid.grid:
            return False
        
    
    # move that makes track impossible
    
    
    #check if below, there is an opening for up and not the corresponding down tile in the move
    if move[0] == 'H':
        below_coords = [ i + DOWN for i in move_coords]
        for i in range(len(below_coords)):
            if below_coords[i] in grid.grid:
                if UP in grid.grid[below_coords[i]].openings and DOWN not in (move[2][i]).openings:
                    return False
                if UP not in grid.grid[below_coords[i]].openings and DOWN in (move[2][i]).openings:
                    return False
                
                
        above_coords = [ i + UP for i in move_coords]
        for i in range(len(above_coords)):
            if above_coords[i] in grid.grid:
                if DOWN in grid.grid[above_coords[i]].openings and UP not in (move[2][i]).openings:
                    return False
                if DOWN not in grid.grid[above_coords[i]].openings and UP in (move[2][i]).openings:
                    return False
                
        left_coord = [ move[1] + LEFT ]
        for i in range(len(left_coord)):
            if left_coord[i] in grid.grid:
                if RIGHT in grid.grid[left_coord[i]].openings and LEFT not in (move[2][0]).openings:
                    return False
                if RIGHT not in grid.grid[left_coord[i]].openings and LEFT in (move[2][0]).openings:
                    return False
                
        right_coord = [ move_coords[-1] + RIGHT ]
        for i in range(len(right_coord)):
            if right_coord[i] in grid.grid:
                if LEFT in grid.grid[right_coord[i]].openings and RIGHT not in (move[2][-1]).openings:
                    return False
                if LEFT not in grid.grid[right_coord[i]].openings and RIGHT in (move[2][-1]).openings:
                    return False
                
    if move[0] == 'V':
        above_coord = [ move_coords[-1] + UP ]
        for i in range(len(above_coord)):
            if above_coord[i] in grid.grid:
                if DOWN in grid.grid[above_coord[i]].openings and UP not in (move[2][-1]).openings:
                    return False
                if DOWN not in grid.grid[above_coord[i]].openings and UP in (move[2][-1]).openings:
                    return False
                
        below_coord = [ move[1] + DOWN]
        for i in range(len(below_coord)):
            if below_coord[i] in grid.grid:
                if UP in grid.grid[below_coord[i]].openings and DOWN not in (move[2][0]).openings:
                    return False
                if UP not in grid.grid[below_coord[i]].openings and DOWN in (move[2][0]).openings:
                    return False
    
                
        left_coords = [ i + LEFT for i in move_coords]
        for i in range(len(left_coords)):
            if left_coords[i] in grid.grid:
                if RIGHT in grid.grid[left_coords[i]].openings and LEFT not in (move[2][i]).openings:
                    return False
                if RIGHT not in grid.grid[left_coords[i]].openings and LEFT in (move[2][i]).openings:
                    return False   
                
        right_coords = [ i + RIGHT for i in move_coords]
        for i in range(len(right_coords)):
            if right_coords[i] in grid.grid:
                if LEFT in grid.grid[right_coords[i]].openings and RIGHT not in (move[2][i]).openings:
                    return False
                if LEFT not in grid.grid[right_coords[i]].openings and RIGHT in (move[2][i]).openings:
                    return False               
        
        
        
    return True
                       

def all_possible_moves(grid):
    moves = []
    for i in grid.boundary():
        for j in possible_left_to_right():
            if len(j) > 0:
                if valid_move( ['H', i, j ], grid ):
                    moves.append (['H', i, j ])                    
            if len(j) > 1:
                if valid_move( ['H', i + LEFT, j ], grid ):
                    moves.append (['H', i + LEFT, j ])
            if len(j) > 2:
                if valid_move( ['H', i + LEFT + LEFT , j ], grid ):
                    moves.append (['H', i + LEFT + LEFT, j ])
                                
                    
        for k in possible_down_to_up():
            if len(k) > 0:
                if valid_move( ['V', i, k ], grid ):
                    moves.append (['V', i, k ])   
            if len(k) > 1:
                if valid_move( ['V', i + DOWN, k ], grid ):
                    moves.append (['V', i + DOWN, k ])
            if len(k) > 2:
                if valid_move( ['V', i + DOWN + DOWN , k ], grid ):
                    moves.append (['V', i + DOWN + DOWN, k ])
                    
    return moves
#double counts 1 - length moves :( , once as 'H' and once as 'V'
    
    
    
    
    
    
    