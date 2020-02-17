import pygame
from pygame.locals import *

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
    def __init__(self, color, width, height, position):
        """
        :param 

        kind: tuple (red,green,blue) determines color of block (0-255)
        kind: int width of block
        kind: int height of block
        kind: tuple (int,int) (x,y) posiiton of block
        """
        self.color = color
        self.width = width
        self.height = height
        self.position = position
        self.occupied = False

        self.surf = pygame.Surface((width,height)) 
		
		# Define the color of the surface using RGB color coding. 
        self.surf.fill(color) 
        self.rect = self.surf.get_rect() 