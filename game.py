import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((900, 400))
pygame.display.set_caption('My Game')

font = pygame.font.Font(None, 100)

text_surface = font.render('My Game', True, 'Red')
text_rect = text_surface.get_rect(center = (450, 50))

sky_surface = pygame.image.load('gpics/background.png')
sky_rect = sky_surface.get_rect(topleft = (0, 0))

level_surface = pygame.Surface((900, 100))
level_surface.fill('Grey')
level_rect = level_surface.get_rect(midbottom = (450, 400))

player_surface = pygame.image.load('gpics/player.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (450, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
	
    
    screen.blit(sky_surface, sky_rect)
    screen.blit(text_surface, text_rect)
    screen.blit(level_surface, level_rect)
    if player_rect.left > 900:
        player_rect.left = 0
    player_rect.right += 1
    screen.blit(player_surface, player_rect)

    pygame.display.update()
