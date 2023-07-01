import pygame
from sys import exit

pygame.init() # starts pygame and initiates all its components
screen = pygame.display.set_mode((800, 400))    # display surface (width, height) in px
pygame.display.set_caption('paigaim')
clock = pygame.time.Clock()                     # clock object

while True:
    for event in pygame.event.get():    # gets all events from Pygame
        if event.type == pygame.QUIT:   # if user wants to exit
            pygame.quit()               # opposite of pygame.init() --> uninitializes everything
            exit()                      # (from sys) closes all processes that are running

    # draw all elements & update everything
    pygame.display.update()             # updates display surface
                                        # and puts changes on display surface
    clock.tick(60)                      # loop doesn't run faster than 60 miliseconds
