import pygame
from sys import exit

pygame.init() 
screen = pygame.display.set_mode((800, 400))                            
pygame.display.set_caption('paigaim')
clock = pygame.time.Clock()                                             

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

''' SURFACES '''
sky_surface = pygame.image.load('graphics/Sky.png').convert()           
ground_surface = pygame.image.load('graphics/ground.png').convert()     

score_surf = test_font.render('My Game', False, (64, 64, 64))   # rgb tuple for the color
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

'''MAIN GAME LOOP'''
while True:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:      
            pygame.quit()                   
            exit()   
        # event loop checking for mouse & keyboard input  
        # note: checking for mousemotion is more efficient than checking for a collision   
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # only jumping if the player is on/below the ground
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: # note: using and might make it more difficult for the input to register for some reason
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: 
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True      
                # above not enough to work because we have to keep spacing until the player and enemy do not collide
                snail_rect.left = 800     
    '''GAME'''
    if game_active:
        # drawing sky & ground
        screen.blit(sky_surface, (0,0))             
        screen.blit(ground_surface, (0,300))
        
        # drawing outline for score text
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        screen.blit(score_surf, score_rect)

        # managing the snail's movements
        snail_rect.x -= 4                      # x, y coordinates of rectangles can be accessed                 
        if snail_rect.right <= 0:   snail_rect.left = 800   
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
        
        # collision 
        if snail_rect.colliderect(player_rect):
            screen.fill('Yellow')
            game_active = False
            

    pygame.display.update()                                                         
    clock.tick(60)                          
