"""
Pygame base template for opening a window, done with functions
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
 
# The use of the main function is described in Chapter 9.
 
# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
def draw_tank(screen,x,y):
	pygame.draw.rect(screen,GREEN, [x-30,y-15,60,30],0)
	pygame.draw.polygon(screen,GREEN,[[x-70,y+15],[x-30,y+50],[x+30,y+50],[x+70,y+15]],0)
	pygame.draw.rect(screen,GREEN,[x+30,y-5,60,10],0)	

def draw_rocket(screen,x,y):
	pygame.draw.rect(screen,RED,[x-30,y-5,60,10],0)
	pygame.draw.polygon(screen,RED,[[x-30,y-15],[x-20,y-5],[x-30,y-5]],0)
	pygame.draw.polygon(screen,RED,[[x-30,y+15],[x-20,y+5],[x-30,y+5]],0)
	pygame.draw.polygon(screen,RED,[[x+30,y-5],[x+40,y],[x+30,y+5]],0)
 
def main():
    """ Main function for the game. """
    pygame.init()
    pygame.mouse.set_visible(False)
 	
    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
 	#coordinates
    tank_coords=[100,100]
    x_speed=0
    y_speed=0
 
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
		    # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    x_speed = 3
                elif event.key == pygame.K_UP:
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    y_speed = 3
                    
    	    # User let up on a key
            elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
            
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        rocket_pos=pygame.mouse.get_pos()
        tank_coords[0]+=x_speed
        tank_coords[1]+=y_speed
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        draw_tank(screen,tank_coords[0],tank_coords[1])
        draw_rocket(screen,rocket_pos[0],rocket_pos[1])
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)
 
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
 
if __name__ == "__main__":
    main()
