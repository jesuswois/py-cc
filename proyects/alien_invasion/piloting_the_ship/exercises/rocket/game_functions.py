import sys
import pygame

def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)

def check_keydown_events(event, rocket):
    if event.key == pygame.K_UP:
        rocket.moving_up = True
        print("up")
    elif event.key == pygame.K_RIGHT:
        rocket.moving_right = True
        print("right")
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
        print("left")
    elif event.key == pygame.K_DOWN:
        print("down")
        rocket.moving_down = True

def check_keyup_events(event, rocket):
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False

def update_screen(bg_color, screen, rocket):
    screen.fill(bg_color)
    rocket.blitme()
    pygame.display.flip()
