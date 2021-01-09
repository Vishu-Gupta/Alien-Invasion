"""Main File for Alien Invasion project"""
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        #start the main loop for the game
        while True:
            self._check_events()
            #update ships,bullets etc
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        #Check for any bullets that have hit aliens
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet -alien collision."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens , True, True) # kills colliding objects
        if not self.aliens:
            #destroy bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Create Alien fleet"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3* alien_height ) - ship_height
        number_rows = available_space_y // (2*alien_height)
        available_space_x = self.settings.screen_width - ( 2 * alien_width)
        number_aliens_x = available_space_x // (2*alien_width)
        
        #creat fleet
        for row_no in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_no)



    def _create_alien(self, alien_number, row_no):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width*alien_number
        alien.y = alien_height + 2* alien_height * row_no
        alien.rect.y = alien.y
        alien.rect.x = alien.x

        self.aliens.add(alien)

    def _update_aliens(self):
        """Update position of all aliens"""
        self._check_fleet_edges()
        self.aliens.update()


    def _update_screen(self):
        """Updates display"""
        self.screen.fill(self.settings.screen_bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen) # draws the whole group
        #make display visible
        pygame.display.flip()

    def fire_bullet(self):
        """Create a new bullet and add it to the current bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites(): # why use .sprites()
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Drop the entire fleet and change the fleets direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 # reverse direction

if __name__ == "__main__":
    ai = AleinInvasion()
    ai.run_game()