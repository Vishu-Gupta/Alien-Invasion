"""Main File for Alien Invasion project"""
import sys
import pygame
from settings import Settings
from ship import Ship

class AleinInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        #initialize the game, and create resource
        pygame.init()
        self.settings = Settings() # assign Settings from Settings class to self
        self.screen =pygame.display.set_mode((self.settings.
                                    screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) #create a ship attribute for this instance and pass this instance to Ship class 

    def run_game(self):
        #start the main loop for the game
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """Responds to Key presses and other events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True # move the ship right by 1 position
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP : 
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
 
    
    def _update_screen(self):
        """Updates display"""
        self.screen.fill(self.settings.screen_bg_color)
        self.ship.blitme()
        self.ship.update()
        #make display visible
        pygame.display.flip()


if __name__ == "__main__":
    ai = AleinInvasion()
    ai.run_game()