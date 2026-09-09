# 12-4. Keys: Make a Pygame file that creates an empty screen. In the event
# loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected.
# Run the program and press various keys to see how Pygame responds.

import pygame
from settings import Settings
from game_functions import check_events

def run_game():
    pygame.init()

    # Game Configuration
    settings = Settings()
    pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Keys")

    while True:
        check_events()
        pygame.display.flip()

run_game()