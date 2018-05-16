"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (171, 227, 152)
RED = (255, 0, 0)
BLUE = (152, 208, 227)
BROWN = (158, 138, 27)
GREY = (89, 85, 97)
YELLOW = (193, 204, 75)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Relearning Drawing")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen , GREEN, [0,300,700,200])
    pygame.draw.rect(screen , BLUE, [0,0,700,300])
    
    for xoffset in range(10):
        pygame.draw.rect(screen, GREY, [25+xoffset*75, 200, 50, 200])
        for i in range(38):
        	for j in range (8):
        		if random.randrange(2)==0:
        			color=BLACK
        		else:
        			color=YELLOW
        		pygame.draw.rect(screen, color, [30+xoffset*75+j*5,205+i*5,3,3])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()