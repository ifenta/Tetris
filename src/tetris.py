import pygame 
from pygame.locals import *

import block
import grid

import random

from time import sleep


# Initiate Grid
SCREEN_WIDTH = 300
grid = grid.Grid(SCREEN_WIDTH)

# initialize pygame 
pygame.init() 

# Define the dimensions of screen object and caption
screen = pygame.display.set_mode((grid.width, grid.height)) 
pygame.display.set_caption("Tetris Demo")

# Variable to keep our game loop running 
gameOn = True

# Set screen black initially
screen.fill((0,0,0))


# Sets each block in the grid to a random color
for x in grid.grid:
	for y in x:
		y.surf.fill( ( random.randint(0,255),random.randint(0,255),random.randint(0,255) ) )  
		screen.blit(y.surf, y.position)

# Our game loop 
while gameOn: 
	# for loop through the event queue 
	for event in pygame.event.get(): 
		
		# Check for KEYDOWN event 
		if event.type == KEYDOWN: 
			
			# If the Backspace key has been pressed set 
			# running to false to exit the main loop 
			if event.key == K_BACKSPACE: 
				gameOn = False

		# Check for QUIT event 
		elif event.type == QUIT: 
			gameOn = False


	# Update the display using flip 
	pygame.display.flip() 
