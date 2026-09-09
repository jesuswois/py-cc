# 12-3. Rocket: Make a game that begins with a rocket in the center of the
# screen. Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of the
# screen.

import pygame
from settings import Settings
from rocket import Rocket
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Rocket")
    rocket = Rocket(game_settings, screen)

    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(game_settings.bg_color, screen, rocket)

run_game()
