# def main():
    # pass

# if __name__ == '__main__':
    # main()

import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("F1 hotlap") # geeksforgeeks (7-24)


from pygame.locals import *

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the solid rectangle
pygame.draw.rect(window, (0,   0, 200), # color
                [50, 300, 75, 50], 10) # position, position, size, size

# Draws the surface object to the screen.
pygame.display.update()

# Game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

    