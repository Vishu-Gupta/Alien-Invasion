class Settings:
    """Define all settings for Game"""
    def __init__(self):
        #intialie game's settings
        #screen base settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = ( 230, 230, 230)
        # Ship settings
        self.ship_speed = 1.
        self.ship_limit = 3
        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #alien settings
        self.alien_width = 100
        self.alien_height = 80
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10.0
        self.fleet_direction = 1 # 1 indicates right, -1 indicates left
