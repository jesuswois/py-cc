# 12-3. Rocket: Make a game that begins with a rocket in the center of the
# screen. Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of the
# screen.

import pygame

def run_game():
    pygame.init()

    screen = pygame.display.set_mode((600,1200))
    pygame.display.set_caption("Rocket")
    rocket = Rocket(game_settings.rocket_movement_multiplier,screen)

    while True:


        pygame.display.flip()