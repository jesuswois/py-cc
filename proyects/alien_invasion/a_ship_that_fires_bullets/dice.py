import pygame

class Dice:
    def __init__(self, screen):
        self.screen = screen
        
        # Load character and save a reference to his rectangle
        self.image = pygame.image.load('images/dice.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start the dice at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)