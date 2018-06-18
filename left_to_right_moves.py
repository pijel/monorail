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


final_answer = []
for k in possible_left_to_right():
       final_answer.append(print_tile_list(k))
easy_to_read_left_to_right = final_answer
#print(easy_to_read_left_to_right)


#Finally, here is just the list for perusal. Bad news for complexity - its 78 elements strong (out of 258 possible lists with no restriction, so it's actually kinda good). With a reasonable sounding ~10 openings to possibly play in, that's ~1000 moves. 

for_perusal = [['RIGHT UP'],
 ['DOWN UP'],
 ['LEFT UP'],
 ['DOWN RIGHT'],
 ['LEFT RIGHT'],
 ['LEFT DOWN'],
 ['RIGHT UP', 'LEFT UP'],
 ['RIGHT UP', 'LEFT RIGHT'],
 ['RIGHT UP', 'LEFT DOWN'],
 ['DOWN UP', 'RIGHT UP'],
 ['DOWN UP', 'DOWN UP'],
 ['DOWN UP', 'DOWN RIGHT'],
 ['LEFT UP', 'RIGHT UP'],
 ['LEFT UP', 'DOWN UP'],
 ['LEFT UP', 'DOWN RIGHT'],
 ['DOWN RIGHT', 'LEFT UP'],
 ['DOWN RIGHT', 'LEFT RIGHT'],
 ['DOWN RIGHT', 'LEFT DOWN'],
 ['LEFT RIGHT', 'LEFT UP'],
 ['LEFT RIGHT', 'LEFT RIGHT'],
 ['LEFT RIGHT', 'LEFT DOWN'],
 ['LEFT DOWN', 'RIGHT UP'],
 ['LEFT DOWN', 'DOWN UP'],
 ['LEFT DOWN', 'DOWN RIGHT'],
 ['RIGHT UP', 'LEFT UP', 'RIGHT UP'],
 ['RIGHT UP', 'LEFT UP', 'DOWN UP'],
 ['RIGHT UP', 'LEFT UP', 'DOWN RIGHT'],
 ['RIGHT UP', 'LEFT RIGHT', 'LEFT UP'],
 ['RIGHT UP', 'LEFT RIGHT', 'LEFT RIGHT'],
 ['RIGHT UP', 'LEFT RIGHT', 'LEFT DOWN'],
 ['RIGHT UP', 'LEFT DOWN', 'RIGHT UP'],
 ['RIGHT UP', 'LEFT DOWN', 'DOWN UP'],
 ['RIGHT UP', 'LEFT DOWN', 'DOWN RIGHT'],
 ['DOWN UP', 'RIGHT UP', 'LEFT UP'],
 ['DOWN UP', 'RIGHT UP', 'LEFT RIGHT'],
 ['DOWN UP', 'RIGHT UP', 'LEFT DOWN'],
 ['DOWN UP', 'DOWN UP', 'RIGHT UP'],
 ['DOWN UP', 'DOWN UP', 'DOWN UP'],
 ['DOWN UP', 'DOWN UP', 'DOWN RIGHT'],
 ['DOWN UP', 'DOWN RIGHT', 'LEFT UP'],
 ['DOWN UP', 'DOWN RIGHT', 'LEFT RIGHT'],
 ['DOWN UP', 'DOWN RIGHT', 'LEFT DOWN'],
 ['LEFT UP', 'RIGHT UP', 'LEFT UP'],
 ['LEFT UP', 'RIGHT UP', 'LEFT RIGHT'],
 ['LEFT UP', 'RIGHT UP', 'LEFT DOWN'],
 ['LEFT UP', 'DOWN UP', 'RIGHT UP'],
 ['LEFT UP', 'DOWN UP', 'DOWN UP'],
 ['LEFT UP', 'DOWN UP', 'DOWN RIGHT'],
 ['LEFT UP', 'DOWN RIGHT', 'LEFT UP'],
 ['LEFT UP', 'DOWN RIGHT', 'LEFT RIGHT'],
 ['LEFT UP', 'DOWN RIGHT', 'LEFT DOWN'],
 ['DOWN RIGHT', 'LEFT UP', 'RIGHT UP'],
 ['DOWN RIGHT', 'LEFT UP', 'DOWN UP'],
 ['DOWN RIGHT', 'LEFT UP', 'DOWN RIGHT'],
 ['DOWN RIGHT', 'LEFT RIGHT', 'LEFT UP'],
 ['DOWN RIGHT', 'LEFT RIGHT', 'LEFT RIGHT'],
 ['DOWN RIGHT', 'LEFT RIGHT', 'LEFT DOWN'],
 ['DOWN RIGHT', 'LEFT DOWN', 'RIGHT UP'],
 ['DOWN RIGHT', 'LEFT DOWN', 'DOWN UP'],
 ['DOWN RIGHT', 'LEFT DOWN', 'DOWN RIGHT'],
 ['LEFT RIGHT', 'LEFT UP', 'RIGHT UP'],
 ['LEFT RIGHT', 'LEFT UP', 'DOWN UP'],
 ['LEFT RIGHT', 'LEFT UP', 'DOWN RIGHT'],
 ['LEFT RIGHT', 'LEFT RIGHT', 'LEFT UP'],
 ['LEFT RIGHT', 'LEFT RIGHT', 'LEFT RIGHT'],
 ['LEFT RIGHT', 'LEFT RIGHT', 'LEFT DOWN'],
 ['LEFT RIGHT', 'LEFT DOWN', 'RIGHT UP'],
 ['LEFT RIGHT', 'LEFT DOWN', 'DOWN UP'],
 ['LEFT RIGHT', 'LEFT DOWN', 'DOWN RIGHT'],
 ['LEFT DOWN', 'RIGHT UP', 'LEFT UP'],
 ['LEFT DOWN', 'RIGHT UP', 'LEFT RIGHT'],
 ['LEFT DOWN', 'RIGHT UP', 'LEFT DOWN'],
 ['LEFT DOWN', 'DOWN UP', 'RIGHT UP'],
 ['LEFT DOWN', 'DOWN UP', 'DOWN UP'],
 ['LEFT DOWN', 'DOWN UP', 'DOWN RIGHT'],
 ['LEFT DOWN', 'DOWN RIGHT', 'LEFT UP'],
 ['LEFT DOWN', 'DOWN RIGHT', 'LEFT RIGHT'],
 ['LEFT DOWN', 'DOWN RIGHT', 'LEFT DOWN']]