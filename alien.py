import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to define general characterstics of the aliens"""
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        #load the alien image and set its rect attributes
        self.image = pygame.image.load("images/alien1.png")
        self.image = pygame.transform.scale(self.image,(self.settings.alien_width,self.settings.alien_height))
        self.rect = self.image.get_rect()
        #Load all aliens at top corner
        self.rect.x= self.rect.width
        self.rect.y= self.rect.height

        self.x = float(self.rect.x) # storing x position

    def update(self):
        """ Move alien right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0 :
            return True

