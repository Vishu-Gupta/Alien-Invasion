"""Module for all details related to Bullet"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, game):
        super().__init__() # inherit __init__
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        #create a bullet at 0,0 of req size and then align with ships top.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # Store bullets position
        self.y = float(self.rect.y)

    def update(self):
        """ Move the bullet up"""
        self.y -= self.settings.bullet_speed
        #update Bullet position to calculated location
        self.rect.y = self.y
        
    def draw_bullet(self):
        """ Draw the bullet as per settings"""
        pygame.draw.rect(self.screen, self.color, self.rect)
