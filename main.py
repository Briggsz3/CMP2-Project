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
car_x = 500
car_y = 375





# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((1500, 750))

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the solid rectangle
pygame.draw.rect(window, (0,   0, 200), # color
                [50, 300, 75, 50], 10) # position, position, size, size



def car():
    window.blit(f1_car,(car_x, car_y))

car()

# Draws the surface object to the screen.

pygame.display.update()

# Game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  vel = 10
run = True

# infinite loop 
	pygame.time.delay(10) 
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False
	keys = pygame.key.get_pressed() 
	
	if keys[pygame.K_LEFT] and x>0: 
		x -= vel 
		
	if keys[pygame.K_RIGHT] and x<500-width: 
		x += vel 
		
	if keys[pygame.K_UP] and y>0: 
		y -= vel 
		
	if keys[pygame.K_DOWN] and y<500-height: 
		y += vel 


# Quit Pygame
pygame.quit()

    
