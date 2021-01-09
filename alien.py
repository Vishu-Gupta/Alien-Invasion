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
