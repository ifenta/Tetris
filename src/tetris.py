import pygame 
from pygame.locals import *

import grid
import timer

import random

# Initiate Grid
SCREEN_WIDTH = 300
grid = grid.Grid(SCREEN_WIDTH)

# initialize pygame 
pygame.init() 

# Define the dimensions of screen object and caption
screen = pygame.display.set_mode((grid.width, grid.height)) 
pygame.display.set_caption("Tetris Demo")
clock = pygame.time.Clock()

# Variable to keep our game loop running 
gameOn = True

# Set screen black initially
screen.fill((0,0,0))

# Place holder for initializing a block
# Set position
pos = [random.randint(0,9),0]
block = grid.grid[pos[0]][pos[1]]
# Set color
block.color = random.randint(0,255)
block.surf.fill(block.color)  
# Pass to screen
screen.blit( block.surf, block.position )
pygame.display.flip()

# Control Drop Speed
drop_speed_control = timer.Timer()
drop_delay = 1000

try:
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

				if event.key == K_LEFT:
					pos = grid.move_left(screen, pos)
					pygame.display.flip()

				elif event.key == K_RIGHT:
					pos = grid.move_right(screen, pos)
					pygame.display.flip()

				elif event.key == K_DOWN:
					drop_delay -= 100
					if drop_delay < 0:
						drop_delay = 0

				elif event.key == K_UP:
					drop_delay += 100
					if drop_delay > 2000:
						drop_delay = 2000

			# Check for QUIT event 
			elif event.type == QUIT: 
				gameOn = False

		
		if drop_speed_control.time_check(drop_delay):
			# Update the display using flip 
			pos = grid.move_down(screen, pos)
			pygame.display.flip() 

			if pos == None:
				# Create new block
				pos = [random.randint(0,9),0]

				block = grid.grid[pos[0]][pos[1]]

				block.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
				block.surf.fill( block.color )  
				screen.blit( block.surf, block.position )

		
except KeyboardInterrupt:
	print("Keyboard Interrupt")
finally: 
	pygame.quit()
	print("Finished Game")
	quit()