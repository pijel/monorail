class GameGrid:
    #Tiles are stored as a 1x4 boolean list, coordinates are 1x2 integer lists [North,East]
    #Tile is stored [North,East,West,South] (NEWS order), true if there is an opening in that direction, false if there is not
    #Every Tile has two openings and two non openings. Actually every combo is represented of 2 from 4, so 6 tiles total
    def __init__(self,grid={(0,0):[False,True,True,False],(0,1):[False,True,True,False]}):
        self.grid = grid
    #Initialize the grid to the starting position, but also allows for varied starting positions
    #In Monorail, we start with two horizontal east west tiles 
    def move(self,coord,tile1):
        if coord in self.grid:
            return False
        else:
            self.grid[coord] = tile1
    #this function needs to be extended to count multiple moves
    #as of now, it can place a single tile, but in the game its possible to place up to 3 in a row
    def show(self):
        print(self.grid)
    def closedcomplete(self):       
        seen_coords = [(0,1)]            
        current_coord = (0,1)
        current_direction = 1
        expected_direction = 2
        # follow track around 
        while current_coord != (0,0):
            #print(current_direction)
            if current_direction == 0:
                expected_direction = 3
            elif current_direction == 1:
                expected_direction = 2
            elif current_direction == 2:
                expected_direction = 1
            elif current_direction == 3:
                expected_direction = 0
            # NORTH
            if current_direction == 0:
                temp = list(current_coord)
                temp[0] += 1
                current_coord = tuple(temp)
                seen_coords.append(current_coord)
                if current_coord not in self.grid:
                    return False
                if not self.grid[current_coord][expected_direction]:
                    return False
                else:
                    for k in range(4):
                        if self.grid[current_coord][k] and k != expected_direction:
                            current_direction = k
            
            #EAST
            elif current_direction == 1:
                temp = list(current_coord)
                temp[1] += 1
                current_coord = tuple(temp)
                #print(current_coord)
                if current_coord not in self.grid:
                    return False
                if not self.grid[current_coord][expected_direction]:
                    return False
                else:
                    for k in range(4):
                        if self.grid[current_coord][k] and k != expected_direction:
                            current_direction = k
                
                seen_coords.append(current_coord)
            
            #WEST 
            elif current_direction == 2:
                temp = list(current_coord)
                temp[1] -= 1
                current_coord = tuple(temp)
                if current_coord not in self.grid:
                    return False
                if not self.grid[current_coord][expected_direction]:
                    return False
                else:
                    for k in range(4):
                        if self.grid[current_coord][k] and k != expected_direction:
                            current_direction = k
                seen_coords.append(current_coord)
                
            #SOUTH
            elif current_direction == 3:
                temp = list(current_coord)
                temp[0] -= 1
                current_coord = tuple(temp)
                #print(current_coord)
                seen_coords.append(current_coord)
                if current_coord not in self.grid:
                    return False
                if not self.grid[current_coord][expected_direction]:
                    return False
                else:
                    for k in range(4):
                        if self.grid[current_coord][k] and k != expected_direction:
                            current_direction = k
            
            
            #check if every tile was used in the track 
        unused_tiles = [k for k in self.grid if k not in seen_coords]
        #print(unused_tiles)
        if len(unused_tiles) > 0:
            return False
        
            
        return True 
