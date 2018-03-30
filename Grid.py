class GameGrid:
    def __init__(self,grid={(0,0):[False,True,True,False],(0,1):[False,True,True,False]}):
        self.grid = grid
    def move(self,coord,tile1):
        if coord in self.grid:
            return False
        else:
            self.grid[coord] = tile1
    def show(self):
        print(self.grid)
    def closed(self):
        pass
        #Write a function that determines if a grid has a closed track by starting at the start and following the path 
    