import block

class Grid:
    """
    The Tetris playing grid
    """
    def __init__(self, width):

        if width*2 > ((width*2) + int(width/10)*4):
            raise IndexError('height must be twice of width')
        if width%10 != 0:
            raise IndexError('width must be a multiple of 10')

        self.width = width
        self.height = ((width*2) + int(width/10)*4)

        self.grid = []
        
        for ii in range(self.width):
            self.grid.append([])
            for jj in range(self.height):
                self.grid[ii].append(block.Block((0,0,0),self.width/10,self.height/24,(ii*(self.width/10),jj*(self.height/24))))

