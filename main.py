import pygame
from sys import exit

pygame.init() # starts pygame and initiates all its components
screen = pygame.display.set_mode((800, 400))    # display surface (width, height) in px
pygame.display.set_caption('paigaim')
clock = pygame.time.Clock()                     # clock object

#test_surface = pygame.Surface((100, 200))       # creates a REGULAR surface
                                                # that we can put on the display surface

sky_surface = pygame.image.load('graphics/Sky.png')    # literally loading an image using a relative path
ground_surface = pygame.image.load('graphics/ground.png')
#test_surface.fill('Red')    



while True:
    for event in pygame.event.get():    # gets all events from Pygame
        if event.type == pygame.QUIT:   # if user wants to exit
            pygame.quit()               # opposite of pygame.init() --> uninitializes everything
            exit()                      # (from sys) closes all processes that are running

    
    screen.blit(sky_surface, (0,0))         # blit = block image transfer 
                                            # blocking display surface transfer to put this on top
                                            # (surface, position - (x,y))
                                            # coordinate system starts from top-left! 
                                            # note: the order of blitting stacks surfaces on top of one another
    screen.blit(ground_surface, (0,300))
    # draw all elements & update everything
    pygame.display.update()             # updates display surface
                                        # and puts changes on display surface
    clock.tick(60)                      # loop doesn't run faster than 60 miliseconds
