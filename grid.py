class Grid:
    """
    The Tetris playing grid
    """
    def __init__(self, width=10, height=20, buffer=4):
        self.width = width
        self.height = height + buffer
        self.player_height = height

        self.grid = [[None] * self.height
                     for _ in range(self.width)]
