import pygame
from button import Button
from text_input import Text_Input


class Login_Screen:
    def __init__(self, ai_game) -> None:
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.login_button = Button(self, "login")
        self.bg_color = ai_game.settings.bg_color
        self.username_field = Text_Input(self, 200, 200, 750, 75)
        self.password_field = Text_Input(self, 200, 300, 750, 75)

    def display_login_page(self):
        self.screen.fill(self.bg_color)
        self.username_field.draw_input_field()
        self.password_field.draw_input_field()
        self.login_button.draw_button()
        pygame.display.flip()
