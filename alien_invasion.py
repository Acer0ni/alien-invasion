import sys 
import pygame 

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(Self):
        """init the game ,and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("alien invasion")
    def run_game(self):
        """star the main loop for the game"""
        while True:
            #watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            
            pygame.display.flip()
if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()