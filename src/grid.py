import block

class Grid:
    """
    The Tetris playing grid
    """
    def __init__(self, width):

        if width%10 != 0:
            raise IndexError('width must be a multiple of 10')

        self.width = width
        self.height = ((width*2) + int(width/10)*4)
        self.GRID_WIDTH = 10
        self.GRID_HEIGHT = 24
        self.block_width = self.width/self.GRID_WIDTH
        self.block_height = self.height/self.GRID_HEIGHT

        # index 0 = row on top of screen
        # counts number of alive blocks in each row
        # once the counter reachs 10 in any index, delete all blocks in those rows
        self.alive_blocks_in_rows = [0]*self.GRID_HEIGHT

        # index 0 = column on left of screen
        # counts number of alive blocks in each column
        # once the counter reachs 20 in any index, game over
        self.alive_blocks_in_columns = [0]*self.GRID_WIDTH

        self.grid = []
        
        for x in range(self.width):
            self.grid.append([])
            for y in range(self.height):
                self.grid[x].append(block.Block((0,0,0),self.block_width,self.block_height,(x*(self.block_width),y*(self.block_height))))

    def move_down(self, screen, position):
        if position != None and position[1] < self.GRID_HEIGHT-1:

            old_block = self.grid[position[0]][position[1]]
            new_block = self.grid[position[0]][position[1]+1]

            # Check if there is a block below
            if new_block.occupied:
                return None
            
            # Save color of block
            color = old_block.color

            # Fill initial position black
            old_block.occupied = False
            old_block.color = (0,0,0)
            old_block.surf.fill( (0,0,0) )  
            screen.blit( old_block.surf, old_block.position )

            # Fill new block with old color
            new_block.occupied = True
            new_block.color = color
            new_block.surf.fill(color)
            screen.blit( new_block.surf, new_block.position )

            position[1] += 1
            return position
    
        return None

    def move_left(self, screen, position):
        if position != None and position[0] > 0: 
            old_block = self.grid[position[0]][position[1]]
            new_block = self.grid[position[0]-1][position[1]]

            # Check if there is a block on the left
            if new_block.occupied:
                return position
            # Save color of block
            color = old_block.color

            # Fill initial position black
            old_block.occupied = False
            old_block.color = (0,0,0)
            old_block.surf.fill( (0,0,0) )  
            screen.blit( old_block.surf, old_block.position )

            # Fill new block with old color
            new_block.occupied = True
            new_block.color = color
            new_block.surf.fill(color)
            screen.blit( new_block.surf, new_block.position )

            position[0] -= 1
        return position

    def move_right(self, screen, position):
        if position != None and position[0] < self.GRID_WIDTH-1:
            old_block = self.grid[position[0]][position[1]]
            new_block = self.grid[position[0]+1][position[1]]

            # Check if there is a block on the right
            if new_block.occupied:
                return position

            # Save color of block
            color = old_block.color

            # Fill initial position black
            old_block.occupied = False
            old_block.color = (0,0,0)
            old_block.surf.fill( (0,0,0) )  
            screen.blit( old_block.surf, old_block.position )

            # Fill new block with old color
            new_block.occupied = True
            new_block.color = color
            new_block.surf.fill(color)
            screen.blit( new_block.surf, new_block.position )

            position[0] += 1
        return position

    ##def kill_row(self, row: int):
        ##for 