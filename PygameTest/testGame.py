# import the pygame module 
import pygame 

# import pygame.locals for easier 
# access to key coordinates 
from pygame.locals import *

# Define our square object and call super to 
# give it all the properties and methods of pygame.sprite.Sprite 
# Define the class for our square objects 
class Square(pygame.sprite.Sprite): 
	def __init__(self, color, size): 
		super(Square, self).__init__() 
		
		self.color = color
		# Define the dimension of the surface 
		# Here we are making squares of side 25px 
		self.surf = pygame.Surface(size) 
		
		# Define the color of the surface using RGB color coding. 
		self.surf.fill(self.color) 
		self.rect = self.surf.get_rect() 

# initialize pygame 
pygame.init() 

# Define the dimensions of screen object 
screen = pygame.display.set_mode((800, 600)) 

pygame.display.set_caption("Tetris Demo")

# instantiate all square objects 
square1 = Square((0, 200, 255),(25,25)) 

# Variable to keep our game loop running 
gameOn = True

square_position = [40,40]
key_change = [0,0]

MIN_X = 25
MIN_Y = 25
MAX_X = 550
MAX_Y = 550

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

			square1.surf.fill((255,0,0)) 
			if event.key == K_UP:
				key_change[1] = -25
			elif event.key == K_LEFT:
				key_change[0] = -25
			elif event.key == K_RIGHT:
				key_change[0] = 25
			elif event.key == K_DOWN:
				key_change[1] = 25

		elif event.type == KEYUP:
			square1 = Square((0, 200, 255),(25,25)) 
			key_change[0] = 0
			key_change[1] = 0

		# Check for QUIT event 
		elif event.type == QUIT: 
			gameOn = False

	if key_change[0] != 0 or key_change[1] != 0:
		square_position[0] += key_change[0]
		square_position[1] += key_change[1]

		if square_position[0] < MIN_X:
			square_position[0] = MIN_X
		elif square_position[0] > MAX_X:
			square_position[0] = MAX_X

		if square_position[1] < MIN_Y:
			square_position[1] = MIN_Y
		elif square_position[1] > MAX_Y:
			square_position[1] = MAX_Y

	# Define where the squares will appear on the screen 
	# Use blit to draw them on the screen surface 
	screen.fill((0,0,0))
	screen.blit(square1.surf, (square_position[0], square_position[1])) 

	# Update the display using flip 
	pygame.display.flip() 
