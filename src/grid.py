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

        self.grid = []
        
        for ii in range(self.width):
            self.grid.append([])
            for jj in range(self.height):
                self.grid[ii].append(block.Block((0,0,0),self.block_width,self.block_height,(ii*(self.block_width),jj*(self.block_height))))

    def move_down(self, screen, pos):
        if pos != None:
            if pos[1] < self.GRID_HEIGHT-1:
                old_blk = self.grid[pos[0]][pos[1]]
                new_blk = self.grid[pos[0]][pos[1]+1]
                if new_blk.alive:
                    return None
                
                # Save color of block
                color = old_blk.color

                # Fill initial position black
                old_blk.alive = False
                old_blk.color = (0,0,0)
                old_blk.surf.fill( (0,0,0) )  
                screen.blit( old_blk.surf, old_blk.position )

                # Fill new block with old color
                new_blk.alive = True
                new_blk.color = color
                new_blk.surf.fill(color)
                screen.blit( new_blk.surf, new_blk.position )

                pos[1] += 1
                return pos
        
        return None

    def move_left(self, screen, pos):
        if pos != None: 
            if pos[0] > 0:
                old_blk = self.grid[pos[0]][pos[1]]

                # Save color of block
                color = old_blk.color

                # Fill initial position black
                old_blk.alive = False
                old_blk.color = (0,0,0)
                old_blk.surf.fill( (0,0,0) )  
                screen.blit( old_blk.surf, old_blk.position )

                # Fill new block with old color
                new_blk = self.grid[pos[0]-1][pos[1]]
                new_blk.alive = True
                new_blk.color = color
                new_blk.surf.fill(color)
                screen.blit( new_blk.surf, new_blk.position )

                pos[0] -= 1
        return pos

    def move_right(self, screen, pos):
        if pos != None:
            if pos[0] < self.GRID_WIDTH-1:
                old_blk = self.grid[pos[0]][pos[1]]
                # Save color of block
                color = old_blk.color

                # Fill initial position black
                old_blk.alive = False
                old_blk.color = (0,0,0)
                old_blk.surf.fill( (0,0,0) )  
                screen.blit( old_blk.surf, old_blk.position )

                # Fill new block with old color
                new_blk = self.grid[pos[0]+1][pos[1]]
                new_blk.alive = True
                new_blk.color = color
                new_blk.surf.fill(color)
                screen.blit( new_blk.surf, new_blk.position )

                pos[0] += 1
        return pos
        
        

