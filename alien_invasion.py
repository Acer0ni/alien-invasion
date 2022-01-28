import sys 
import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """init the game ,and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        pygame.display.set_caption("alien invasion")

        #set the background color.
        self.bg_color =(230,230,230)
    def run_game(self):
        """star the main loop for the game"""
        while True:
            #watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()