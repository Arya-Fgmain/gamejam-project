import pygame
from sys import exit

def time_elapsed(): # use pygame.time.get_ticks() to get miliseconds passed since start of program
    # integer division by 1000 since we don't want miliseconds
    # global current_time
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    # or int((pygame.time.... - start_time) / 1000)
    return current_time

'''PRELIMINARIES'''
pygame.init()

# default surface for the game
screen = pygame.display.set_mode((900, 400))
pygame.display.set_caption('Peak Rider')

# clock to manage the game's frame rate in the event loop
clock = pygame.time.Clock()

# for deciding between game/game-over page
game_active = False

# is the character 'peaking' their performance
transformed = False

# speed of enemy / player
speed = 7

# time the player survived
survival_time = 0
start_time = 0
peak_time = 0

# game title & death text
font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 50)
text_surface = small_font.render("Earth's Core", True, 'Red')
text_rect = text_surface.get_rect(center = (450, 50))

death_text_surf = pygame.font.Font(None, 36).render('To replay press [SPACE]', False, 'Black')
death_text_rect = death_text_surf.get_rect(midtop = (450, 370))

'''REGULAR SURFACES'''
sky_surface = pygame.image.load('gpics/background.png').convert()
sky_rect = sky_surface.get_rect(topleft = (0, 0))

# level_surface = pygame.Surface((900, 100))
# level_surface.fill('Grey')
level_surface = pygame.image.load('gpics/level.png').convert()
leve_surface = pygame.transform.scale(level_surface, (1500, 150))
level_rect = level_surface.get_rect(midtop = (450, 300))

player_surface = pygame.image.load('gpics/player.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (150, 300))

# player's gravity --> increases slowly
player_gravity = 1

enemy_surface = pygame.image.load('gpics/enemy.png').convert_alpha()
enemy_surface = pygame.transform.scale(enemy_surface, (110, 90))
enemy_rect = enemy_surface.get_rect(midbottom = (600, 320))

# intro page content
backg_surf = pygame.image.load('gpics/intro_background.png').convert()
backg_surf = pygame.transform.scale(backg_surf, (900, 400))
backg_rect = backg_surf.get_rect()   

game_name = font.render('Peak Rider', False, 'Red')
game_name_rect = game_name.get_rect(midtop = (450, 30))

game_msg = small_font.render('press space to begin', False, 'Red')
game_msg_rect = game_msg.get_rect(midtop = (450, 350))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # checking if either the character was clicked on or the space key was pressed via the event loop to jump
            if player_rect.bottom >= 300 and ( (event.type == pygame.MOUSEBUTTONDOWN and player_rect.collidepoint(event.pos)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) ):
                player_gravity = -20
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                if transformed:
                    # recreate surface and rect to properly place the surface on the LEVEL
                    # --> rotation casues leveling issues
                    player_surface = pygame.image.load('gpics/player.png').convert_alpha()
                    player_rect = player_surface.get_rect(midbottom = (150, 300))
                    speed = 7
                    transformed = False
                else:
                    # recreate surface and rect to properly place the surface on the LEVEL
                    # --> rotation casues leveling issues
                    player_surface = pygame.transform.rotozoom(player_surface, 45, 1)
                    player_rect = player_surface.get_rect(midbottom = (150, 300))
                    speed = 10
                    transformed = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # reset the game if user presses SPACE in death screen
            game_active = True
            enemy_rect.x = 600
            start_time = pygame.time.get_ticks()
        
                
            
    if game_active:
        # drawing the setting & text on the screen
        screen.blit(sky_surface, sky_rect)
        pygame.draw.rect(screen, '#ffbf00', text_rect, 10)
        pygame.draw.rect(screen, '#ffbf00', text_rect)
        screen.blit(text_surface, text_rect)
        screen.blit(level_surface, level_rect)

        # update survival time to reflect new games played & check for peak riding time
        survival_time = time_elapsed()
        if (survival_time > peak_time): 
            peak_time = survival_time
        

        # applying gravity and making sure player doesn't go under the level
        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)
        
        # moving the enemy rectangle
        enemy_rect.x -= speed
        if enemy_rect.x <= -130:
            enemy_rect.x = 900
        screen.blit(enemy_surface, enemy_rect)

        # collision has happened
        if enemy_rect.colliderect(player_rect):
            game_active = False

            temp_surface = pygame.Surface((900, 400))
            temp_surface.fill('White')
            temp_rect = temp_surface.get_rect(topleft = (0,0))
            screen.blit(temp_surface, temp_rect)

            temp_content_surf = pygame.image.load('gpics/death.png').convert_alpha()
            temp_content_rect = temp_content_surf.get_rect(center = (450, 200))
            
            
            pygame.draw.rect(screen, '#dfdfdf', death_text_rect)
            pygame.draw.rect(screen, 'Red', death_text_rect, 2)

            screen.blit(temp_content_surf, temp_content_rect)
            screen.blit(death_text_surf, death_text_rect)

            
    else:
        # intro / game over screen
        # screen.fill('#4a4747')
        screen.fill('#000000')
        # screen.blit(backg_surf, backg_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(game_msg, game_msg_rect)
        peak_surf = small_font.render(f'peak time: {peak_time} sec', False, 'Red')
        peak_rect = peak_surf.get_rect(midtop = (450, 260))      
        screen.blit(peak_surf, peak_rect)
        time_surf = small_font.render(f'time passed: {survival_time} sec', False, 'Red')
        time_rect = time_surf.get_rect(midtop = (450, 200))
        screen.blit(time_surf, time_rect) 
            
            
        

    # updating the canvas with the newly applied changes at a rate of 1/60th of a second
    pygame.display.update()
    clock.tick(60)
