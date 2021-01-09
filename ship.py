import pygame

class Ship:
    """A Class to manage Ship"""
    def __init__(self,game):
        """Initalize ship and its starting position"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.ship_height = 150
        self.ship_width = 90

        #load the ship image and get its rectangle
        self.image = pygame.image.load('Images/ship.png')
        self.image = pygame.transform.scale(self.image,(self.ship_width, self.ship_height)) # resizing the image
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom # Align both the ships position with screend midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)