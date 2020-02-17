class Tetromino:
    """Represents one Tetris block"""
    shapes = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

    def __init__(self, kind: int):
        """
        :param kind: int (0-6) that determines what kind of block to init
        """
        if kind < 0 or kind >= 7:
            raise IndexError('kind must be an int 0-6')
        self.shape = Tetromino.shapes[kind]


class Block:
    def __init__(self):
        pass