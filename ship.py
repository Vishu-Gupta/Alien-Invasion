import pygame

class Ship:
    """A Class to manage Ship"""
    def __init__(self,game):
        """Initalize ship and its starting position"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.ship_height = 150
        self.ship_width = 90
        self.moving_right = False # Will move right when this flag is True
        self.moving_left = False # will move left when this flas is True
        #load the ship image and get its rectangle
        self.image = pygame.image.load('Images/ship.png')
        self.image = pygame.transform.scale(self.image,(self.ship_width, self.ship_height)) # resizing the image
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom # Align both the ships position with screend midbottom

        self.x = float(self.rect.x) #store  decimal value for ships horizontal position

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed 
        
        # moves ships position to new calculated positon
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)