"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the height and width of the screen
screen_width = 700
screen_height = 400

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
        if self.rect.x>screen_width-15:
        	self.rect.x=screen_width-15
        	bump.play()
        if self.rect.x<0:
        	self.rect.x=0
        	bump.play()
        if self.rect.y>screen_height-15:
        	self.rect.y=screen_height-15
        	bump.play()
        if self.rect.y<0:
        	self.rect.y=0
        	bump.play()
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
#     def __init__(self, color, width, height):
#         """ Constructor. Pass in the color of the block,
#         and its x and y position. """
#  
#         # Call the parent class (Sprite) constructor
#         super().__init__()
#  
#         # Create an image of the block, and fill it with a color.
#         # This could also be an image loaded from the disk.
#         self.image = pygame.Surface([width, height])
#         self.image.fill(color)
#  
#         # Fetch the rectangle object that has the dimensions of the image
#         # image.
#         # Update the position of this object by setting the values
#         # of rect.x and rect.y
#         self.rect = self.image.get_rect()
        
    def __init__(self, pic):
        super().__init__() 
 
        self.image = pygame.image.load(pic).convert()
 
        # Set background color to be transparent. Adjust to WHITE if your
        # background is WHITE.
        self.image.set_colorkey(WHITE)
 
        self.rect = self.image.get_rect()
 
# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])

# used for player position
x_speed=0
y_speed=0

# sounds
good_sound=pygame.mixer.Sound('good_block.wav')
bad_sound=pygame.mixer.Sound('bad_block.wav')
bump=pygame.mixer.Sound('bump.wav')
 
#lists of 'sprites.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()

# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = Block('good.png')
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width-32)
    block.rect.y = random.randrange(screen_height-32)
 
    # Add the block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)

for i in range(50):
	block=Block('bad.png')
	
	block.rect.x = random.randrange(screen_width-32)
	block.rect.y = random.randrange(screen_height-32)
	
	bad_block_list.add(block)
	all_sprites_list.add(block)
 
# Create a BLUE player block
player = Player(20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0

# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 25, True, False)
 
# -------- Main Program Loop -----------
while not done:
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
 
	#move player
    player.rect.x+=x_speed
    player.rect.y+=y_speed
    player.update()
 	
    # Clear the screen
    screen.fill(WHITE)
 
    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
 
    # Check the list of collisions.
    for block in good_blocks_hit_list:
        score += 1
        good_sound.play()
        

    for block in bad_blocks_hit_list:
    	score -= 1
    	bad_sound.play()
    
    text = font.render("Score: " + str(score),True,BLACK)
    
    # Draw all the sprites
    all_sprites_list.draw(screen)
    
    screen.blit(text, [250, 250])
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
