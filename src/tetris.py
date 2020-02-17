import pygame 
from pygame.locals import *

import block
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

'''
# Sets each block in the grid to a random color
for x in grid.grid:
	for y in x:
		y.surf.fill( ( random.randint(0,255),random.randint(0,255),random.randint(0,255) ) )  
		screen.blit(y.surf, y.position)
'''

pos = [4,0]

blk = grid.grid[pos[0]][pos[1]]

blk.color = (0,200,255)
blk.surf.fill( (0,200,255) )  
screen.blit( blk.surf, blk.position )

drop_speed_control = timer.Timer()
drop_speed = 1000

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
					drop_speed -= 100
					if drop_speed < 0:
						drop_speed = 0

				elif event.key == K_UP:
					drop_speed += 100
					if drop_speed > 2000:
						drop_speed = 2000

			# Check for QUIT event 
			elif event.type == QUIT: 
				gameOn = False

		
		if drop_speed_control.time_check(drop_speed):
			# Update the display using flip 
			pos = grid.move_down(screen, pos)
			pygame.display.flip() 

			if pos == None:
				# Create new block
				pos = [random.randint(0,9),0]

				blk = grid.grid[pos[0]][pos[1]]

				blk.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
				blk.surf.fill( blk.color )  
				screen.blit( blk.surf, blk.position )

		
except KeyboardInterrupt:
	print("Keyboard Interrupt")
finally: 
	pygame.quit()
	print("Finished Game")
	quit()