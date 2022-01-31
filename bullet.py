import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship"""
    def _init_(self,ai_game):
        """Create a bullet object at the ship's currect position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Creat a bullet rect at (0,0) and then set the correct position.
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullets positon as a decimal value.
        self.y = float(self.rect.y)