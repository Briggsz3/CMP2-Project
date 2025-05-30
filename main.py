import pygame
from pygame.locals import *
import math 



f1_logo = pygame.image.load("./images/f1.256px.png")  # from Code with prince, YT video
pygame.display.set_icon(f1_logo)

# Initialize Pygame
pygame.init()

# Set up the game window
pygame.display.set_caption("F1 hotlap") # geeksforgeeks (7-24)

# load f1 images
f1_car = pygame.image.load("./images/racing-car.png")
f1_w = f1_car.get_width()
f1_h = f1_car.get_height()
f1_car = pygame.transform.scale(f1_car,(f1_w*1.25, f1_h*1.25))
car_x = 540
car_y = 600





# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((1500, 750))


# background
background = pygame.image.load("./images/trackv2.webp") # buildwithpython - pygame tutorial -10-
w = background.get_width()
h = background.get_height() # Coding with Russ
background = pygame.transform.scale(background,(w*2,h))



# Draws the surface object to the screen.

pygame.display.update()

# Game loop
width = 20
height = 20
running = True
vel = 10
change_x_pos = 0
angle = 0

# infinite loop 
while running: 
	# generates the background
	window.fill((0,0,0))
	window.blit(background, (10,10))
	for game_event in pygame.event.get():
		if game_event.type == pygame.QUIT:
			running = False
			pygame.time.delay(10) 
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False
	keys = pygame.key.get_pressed() 
	
	# make the image rotate
	if keys[pygame.K_LEFT] and car_x>0: 
		angle += (1/2)
		surf = pygame.transform.rotate(f1_car, angle)


	if keys[pygame.K_RIGHT] and car_x<1500-width:
		angle -= (1/2)
		surf = pygame.transform.rotate(f1_car, angle) # YouTube video

	
	
	if keys[pygame.K_UP] and car_y>0: 
		car_x += (vel/15)*math.cos(math.radians(angle))  # changes the x and y coordinates at the same time to make the car go forward
		car_y -= (vel/15)*math.sin(math.radians(angle)) # YouTube video
		
	if keys[pygame.K_DOWN] and car_y<750-height: 
		car_x -= (vel/25)*math.cos(math.radians(angle))
		car_y += (vel/25)*math.sin(math.radians(angle))
			
	# generate the image
	surf = pygame.transform.rotate(f1_car, angle)
	window.blit(surf,(car_x,car_y))
	pygame.display.flip()
	pygame.display.update()

		

# Quit Pygame
pygame.quit()

    
