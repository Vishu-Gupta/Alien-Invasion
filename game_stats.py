"""Module that manages all Gamestats"""
class GameStats:
    """ Track statistics for Alien Invasion """

    def __init__(self, game):
        """ Initialize statistics"""
        self.settings = game.settings
        self.reset_stats()
        self.score = 0
        self.high_score = 0
        self.level = 1
        self.game_active = False # flag to monitor if game is active or not

    def reset_stats(self):
        """"Initialize stats that can change during the game"""
        self.ships_left = self.settings.ship_limit