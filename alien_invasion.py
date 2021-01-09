"""Main File for Alien Invasion project"""
import sys
import pygame
from settings import Settings
class AleinInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        #initialize the game, and create resource
        pygame.init()
        self.settings = Settings() # assign Settings from Settings class to self
        self.screen =pygame.display.set_mode((self.settings.
            screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        #start the main loop for the game
        while True:
            #Watch for Keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    sys.exit()

            self.screen.fill(self.settings.screen_bg_color)

            #make displaly visible

            pygame.display.flip()

if __name__ == "__main__":
    ai = AleinInvasion()
    ai.run_game()