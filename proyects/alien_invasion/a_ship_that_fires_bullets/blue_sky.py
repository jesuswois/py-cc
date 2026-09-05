# 12-1. Blue Sky: Make a Pygame window with a blue background.
import sys
import pygame

def run_game():
    pygame.init()

    screen = pygame.display.set_mode((1200,600))
    pygame.display.set_caption("Blue Sky")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill((0, 0, 150))
        pygame.display.flip()

run_game()
