import pygame
from sys import exit

def display_score(): # use pygame.time.get_ticks() to get miliseconds passed since start of program
    # integer division by 1000 since we don't want miliseconds
    # global current_time
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    # or int((pygame.time.... - start_time) / 1000)
    return current_time

'''PRELIMINARIES'''
pygame.init()

# default surface for the game
screen = pygame.display.set_mode((900, 400))
pygame.display.set_caption('My Game')

# clock to manage the game's frame rate in the event loop
clock = pygame.time.Clock()

# for deciding between game/game-over page
game_active = False

# time the player survived
survival_time = 0
start_time = 0

# game title & death text
font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 50)
text_surface = font.render('Hell!', True, 'Red')
text_rect = text_surface.get_rect(center = (450, 50))

death_text_surf = pygame.font.Font(None, 36).render('To replay press [SPACE]', False, 'Black')
death_text_rect = death_text_surf.get_rect(midtop = (450, 370))

'''REGULAR SURFACES'''
sky_surface = pygame.image.load('gpics/background.png')
sky_rect = sky_surface.get_rect(topleft = (0, 0))

level_surface = pygame.Surface((900, 100))
level_surface.fill('Grey')
level_rect = level_surface.get_rect(midbottom = (450, 400))

player_surface = pygame.image.load('gpics/player.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (150, 300))
# player's gravity --> increases slowly
player_gravity = 1

enemy_surface = pygame.image.load('gpics/enemy_resized.png').convert_alpha()
enemy_rect = enemy_surface.get_rect(midbottom = (600, 320))

# beginning page content
game_name = font.render('Welcome to the game!', False, 'Red')
game_name_rect = game_name.get_rect(midtop = (450, 30))

game_msg = font.render('Press space to begin', False, 'Red')
game_msg_rect = game_msg.get_rect(midtop = (450, 290))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            # checking if either the character was clicked on or the space key was pressed via the event loop to jump
            if player_rect.bottom >= 300 and ( (event.type == pygame.MOUSEBUTTONDOWN and player_rect.collidepoint(event.pos)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) ):
                player_gravity = -20
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

        
        survival_time = display_score()
        

        # applying gravity and making sure player doesn't go under the level
        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)
        
        enemy_rect.x -= 7
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
        screen.fill('#4a4747')
        screen.blit(game_name, game_name_rect)
        screen.blit(game_msg, game_msg_rect)
        time_surf = small_font.render(f'time passed: {survival_time}', False, 'Red')
        time_rect = time_surf.get_rect(midtop = (450, 200))

        if survival_time == 0: screen.blit(game_msg, game_msg_rect)
        else: screen.blit(time_surf, time_rect)
        

    # updating the canvas with the newly applied changes at a rate of 1/60th of a second
    pygame.display.update()
    clock.tick(60)
