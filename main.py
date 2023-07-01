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
sky_surface = pygame.image.load('graphics/Sky.png').convert()           # loading an image using a relative path
ground_surface = pygame.image.load('graphics/ground.png').convert()     # convert() converts images to a format that's more convenient for pygame

'''
renders a font based on the created font object instance
(text, Anti-Aliasing: use font edges/not (for pixelated font) with True/False, color)
'''
text_surface = test_font.render('My Game', False, 'Black')

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()  # convert_alpha converts without the background graphics = alpha values of the snake so that it looks right on the screen

snail_rect = snail_surf.get_rect(bottomright = (600, 300))


player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
'''
pygame.Rec(left, top, width, height)
or create a rectangle with the exact same size as the surface using get_rect()
'''
player_rect = player_surf.get_rect(midbottom = (80,300))


while True:
    for event in pygame.event.get():        # gets all events from Pygame
        if event.type == pygame.QUIT:       # if user wants to exit
            pygame.quit()                   # opposite of pygame.init() --> uninitializes everything
            exit()                          # (from sys) closes all processes that are running
        # if event.type == pygame.MOUSEMOTION:    # or MOUSEBUTTONDOWN or MOUSEBUTTONUP
        #     print(event.pos)                # prints position of the mouse wrt the grid
        # if event.type == pygame.MOUSEMOTION and player_rect.collidepoint(event.pos):
        #     # other way to check if the mouse is over the player rectangle
        #     print('mouse in player rectangle')
    '''
    blit = block image transfer = blocking display surface transfer to put this on top
    (surface, position - (x,y))
    coordinate system starts from top-left! 
    note: the order of blitting stacks surfaces on top of one another
    '''
    screen.blit(sky_surface, (0,0))             
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))
    #if snail_x_pos < -100: snail_x_pos = 800   # prevent snail from getting lost outside of the display surface
    snail_rect.x -= 4                           # can move based on coordinates
    if snail_rect.right <= 0:   snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    snail_rect.left -= 1

    # player_rect.left += 1                       # moving the rectangle
    # print(player_rect.left)                     # printing info
    screen.blit(player_surf, player_rect)       # blit(surface, rectangle) if we've instantiated a rectangle
    
    '''
    important: the blit method keeps adding these images to the display surface for every new frame
    so if we just run the code without the sky and ground/text, we see the snail leaves a trail because that's the previously-drawn snail surfaces
    '''
    
    # if player_rect.colliderect(snail_rect):         # returns 0/1 but python translates it automatically
    #     print('collision!')                         # note collision happens in every frame where the rectangles overlap

    # mouse_pos = pygame.mouse.get_pos()                # gets mouse coordinates from pygame.mouse
    # if player_rect.collidepoint(mouse_pos):           # is mouse in the player rectangle?
    #     print(pygame.mouse.get_pressed())             # returns a tuple dictating whether (left, middle, right) mouse buttons are currently pressed or not

    pygame.display.update()                 # updates display surface & puts changes (draws them) on display surface
                                            
    clock.tick(60)                          # loop doesn't run faster than 60 miliseconds
