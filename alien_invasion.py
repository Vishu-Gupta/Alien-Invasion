"""Main File for Alien Invasion project"""
import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AleinInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        #initialize the game, and create resource
        pygame.init()
        self.settings = Settings() # assign Settings from Settings class to self
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.stats = GameStats(self) # instance to store game statistics
        self.play_button = Button(self, "Play")
        self.sb = Scoreboard(self)

    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            #update ships,bullets etc
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


    def _check_events(self):
        """Responds to Key presses and other events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self. _check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Starts a new game when Player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game stats
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            #Rest the game settings
            self.settings.initialize_dynamic_settings()

            # clear remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #hide the mouse cursor
            pygame.mouse.set_visible(False)
            
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True # move the ship right by 1 position
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
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
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) # kills colliding objects

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            #destroy bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #Increase level
            self.stats.level += 1
            self.sb.prep_level()
 
    def _check_aleins_bottom(self):
        """Check if any alien reached bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat similar to ship gets hit
                self._ship_hit()
                break

    def _create_fleet(self):
        """Create Alien fleet"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3* alien_height) - ship_height
        number_rows = available_space_y // (2*alien_height)
        available_space_x = self.settings.screen_width - (2 * alien_width)
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

    def _ship_hit(self):
        """Respond to ship getting hit by an alien"""
        if self.stats.ships_left > 0 :
            self.stats.ships_left -=1 # reduce ships left by 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            #create new fleet and ship
            self._create_fleet()
            self.ship.center_ship()
            # Pause
            sleep(0.5)
        else :
            self.stats.game_active = False
            pygame.mouse.set_visible(True)



    def _update_aliens(self):
        """Update position of all aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aleins_bottom()

    def _update_screen(self):
        """Updates display"""
        self.screen.fill(self.settings.screen_bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen) # draws the whole group
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
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