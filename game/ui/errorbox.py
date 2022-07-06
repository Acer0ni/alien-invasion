from typing import NoReturn
import pygame
from game.ui.button import Button


class ErrorBox:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.message = ""

        self.rect = pygame.Rect(0, 0, 350, 200)
        self.rect.center = self.screen_rect.center
        self.exit_button = Button(
            ai_game, self.rect.bottom - 25, self.rect.left + 75, "exit", 100, 30
        )

    def set_message(self, message) -> NoReturn:
        self.message = message
