
free = 0
LOCKED = -1

from random import choice,seed

class GridClass:
    
    def __init__(self,row, col):

        seed()
        self.rows = row
        self.cols = col

        self.grid = None
        
        self.generate_maze()

        self.grid[0][0] = self.grid[row-1][col-1] = free
    

    # Creates a random rows x cols binary matrix    
    def generate_maze(self):
        self.grid = [ [choice((free,LOCKED,free)) for c in range(self.cols)] for r in range(self.rows)]

    # Get the grid's number of rows
    def get_row(self):
        return self.rows

    # Get the grid's number of columns
    def get_col(self):
        return self.cols

    # Get the value of (x,y)'s grid cell
    def get_state(self,x,y):

        try:
            return self.grid[x][y]
        except IndexError:
            print("Out of bounds")
            exit(-1)
    
    # Returns whether (x,y) cell is occupied by an object
    def is_locked(self,x,y):

        return self.grid[x][y] == LOCKED

    
    # shows the grid in terminal
    def show_grid(self):

        for col in self.grid:
            for elem in col:
                print( elem, end='\t')
            print()

    

