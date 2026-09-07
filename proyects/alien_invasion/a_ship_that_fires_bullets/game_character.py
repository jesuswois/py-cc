# 12-2. Game Character: Find a bitmap image of a game character you like or
# convert an image to a bitmap. Make a class that draws the character at the
# center of the screen and match the background color of the image to the back-
# ground color of the screen, or vice versa.

import sys
import pygame

from dice import Dice

def run_game():
    # Init the game 
    pygame.init()
    
    # Settings
    screen = pygame.display.set_mode((1200,600))
    pygame.display.set_caption("Game Character! (Dice)")
    bg_color = (125, 250, 125)
    dice = Dice(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        dice.blitme()
        pygame.display.flip()
    
run_game()