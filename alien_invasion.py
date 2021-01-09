"""Main File for Alien Invasion project"""
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AleinInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        #initialize the game, and create resource
        pygame.init()
        self.settings = Settings() # assign Settings from Settings class to self
        self.screen =pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) #create a ship attribute for this instance and pass this instance to Ship class
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        #start the main loop for the game
        while True:
            self._check_events()
            #update ships,bullets etc
            self.ship.update()
            self._update_bullets()
            self._update_screen()


    def _check_events(self):
        """Responds to Key presses and other events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP : 
                self. _check_keyup_events(event)

 
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True # move the ship right by 1 position
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        self.bullets.update()
        # delete bullets that leave the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _update_screen(self):
        """Updates display"""
        self.screen.fill(self.settings.screen_bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #make display visible
        pygame.display.flip()

    def fire_bullet(self):
        """Create a new bullet and add it to the current bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)



if __name__ == "__main__":
    ai = AleinInvasion()
    ai.run_game()