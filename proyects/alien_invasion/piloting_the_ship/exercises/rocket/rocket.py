import pygame
class Rocket():
    def __init__(self, settings, screen):
        # Configuration
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.movement_multiplier = settings.rocket_movement_multiplier

        self.image = pygame.image.load('images/rocket.bmp')

        self.rect = self.image.get_rect()

        # Center upon creation
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.center_x_axis = float(self.rect.centerx)
        self.center_y_axis = float(self.rect.centery)

        # Initialize constant moving
        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False

    def blitme(self):
        """Draw the Rocket at his current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up and self.center_y_axis < self.screen_rect.top:
            self.center_y_axis -= self.movement_multiplier
        if self.moving_right and self.center_x_axis < self.screen_rect.right:
            self.center_x_axis += self.movement_multiplier
        if self.moving_down and self.center_y_axis > self.screen_rect.bottom:
            self.center_y_axis += self.movement_multiplier
        if self.moving_left and self.center_x_axis > self.screen_rect.left:
            self.center_x_axis -= self.movement_multiplier

        self.rect.centerx = self.center_x_axis
        self.rect.centery = self.center_y_axis
