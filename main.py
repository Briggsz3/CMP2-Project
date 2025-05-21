import pygame
from pygame.locals import *

f1_logo = pygame.image.load("./images/f1.256px.png")  # from Code with prince, YT video
pygame.display.set_icon(f1_logo)

# Initialize Pygame
pygame.init()

# Set up the game window
pygame.display.set_caption("Silverstone hotlap") # geeksforgeeks (7-24)


# load f1 images
f1_car = pygame.image.load("./images/racing-car.png")
car_x = 275
car_y = 600





# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((1500, 750))

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the solid rectangle
pygame.draw.rect(window, (0,   0, 200), # color
                [50, 300, 75, 50], 10) # position, position, size, size


# background
background = pygame.image.load("./images/trackv2.webp") # buildwithpython - pygame tutorial -10-


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
	
	if keys[pygame.K_LEFT] and car_x>0: 
		car_x -= vel/50

	if keys[pygame.K_RIGHT] and car_x<1500-width: 
		car_x += vel/50

		
	if keys[pygame.K_UP] and car_y>0: 
		car_y -= vel/50
		
	if keys[pygame.K_DOWN] and car_y<750-height: 
		car_y += vel/50
	
	if keys[pygame.K_a]:
		angle +=6
		f1_car = pygame.transform.rotate(f1_car, angle)
		f1_car = pygame.image.load("./images/racing-car.png")
	window.blit(f1_car,(car_x, car_y))
	pygame.display.flip()
	pygame.display.update()

		

# Quit Pygame
pygame.quit()

    
