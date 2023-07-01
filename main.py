import pygame
from sys import exit

pygame.init() # starts pygame and initiates all its components
screen = pygame.display.set_mode((800, 400))                            # display surface (width, height) in px
pygame.display.set_caption('paigaim')
clock = pygame.time.Clock()                                             # clock object

'''
pygame.Surface(...)
creates a REGULAR surface
that we can put on the display surface
pygame.fill(color) fills the surface (even imported images) with color
'''
#test_surface = pygame.Surface((100, 200))                              # creates a REGULAR surface
                                                                        # that we can put on the display surface

'''
create a font --> (font type = could be files or None, font size in px)
'''
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

''' SURFACES '''
sky_surface = pygame.image.load('graphics/Sky.png')                     # loading an image using a relative path
ground_surface = pygame.image.load('graphics/ground.png') 

'''
renders a font based on the created font object instance
(text, Anti-Aliasing: use font edges/not (for pixelated font) with True/False, color)
'''
text_surface = test_font.render('My Game', False, 'Black')

while True:
    for event in pygame.event.get():        # gets all events from Pygame
        if event.type == pygame.QUIT:       # if user wants to exit
            pygame.quit()                   # opposite of pygame.init() --> uninitializes everything
            exit()                          # (from sys) closes all processes that are running

    '''
    blit = block image transfer = blocking display surface transfer to put this on top
    (surface, position - (x,y))
    coordinate system starts from top-left! 
    note: the order of blitting stacks surfaces on top of one another
    '''
    screen.blit(sky_surface, (0,0))             
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))

    
    pygame.display.update()                 # updates display surface & puts changes (draws them) on display surface
                                            
    clock.tick(60)                          # loop doesn't run faster than 60 miliseconds
