class Tile:
    def __init__(self,coordinate,openings):
        #A tile is stored as it position on the grid and by it's openings, which denote where the road openings on the piece are. 
        #Openings is a length 4 boolean list in the NEWS fashion. That is, the first element in openings corresponds as to whether
        #There is a road section on the north face of the tile. The second corresponds to east, so on and so forth
        self.coordinate  = coordinate
        self.openings = openings
    def get_type(self):
        if self.openings == [True,False,False,True] or self.openings == [False,True,True,False]:
            return 1
        #If we have openings on North and South or East and West, this is a straight piece, which we denote as 1.
        return 2
        #Otherwise, it's a bend piece, and we'll denote it as 2.