import sys
import pygame

class AleinInvasion:
    #Overall class to manage game assets and behaviour

    def __init__(self):
        #initialize the game, and create resource
        pygame.init()
        
        self.screen =pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color=(230,230,230) #Setting the backgroud color

    def run_game(self):
        #start the main loop for the game
        while True:
            #Watch for Keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    sys.exit()

            self.screen.fill(self.bg_color)

            #make displaly visible

            pygame.display.flip()

if __name__ == "__main__":
    ai=AleinInvasion()
    ai.run_game()