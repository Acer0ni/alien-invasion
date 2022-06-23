import pygame
from button import Button
from auth.text_input import TextInput
from auth.password_input import PasswordInput


class LoginScreen:
    def __init__(self, ai_game) -> None:
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.login_button = Button(self, 350, 450, "login")
        self.bg_color = ai_game.settings.bg_color
        self.username_field = TextInput(self, 200, 200, 750, 75)
        self.password_field = PasswordInput(self, 200, 300, 750, 75)

    def display_login_page(self):
        self.screen.fill(self.bg_color)
        self.username_field.draw_input_field()
        self.password_field.draw_input_field()
        self.login_button.draw_button()
        pygame.display.flip()
