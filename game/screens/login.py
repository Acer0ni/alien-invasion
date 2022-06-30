import pygame
from game.ui.button import Button
from game.ui.text_input import TextInput
from game.ui.hidden_text_input import HiddenTextInput


class LoginScreen:
    def __init__(self, ai_game) -> None:
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.login_button = Button(self, 450, 450, "login")
        self.skip_button = Button(self, 450, 675, "skip login")
        self.create_button = Button(self, 450, 225, "create account")
        self.bg_color = ai_game.settings.bg_color
        self.username_field = TextInput(self, 200, 200, 750, 75)
        self.password_field = HiddenTextInput(self, 200, 300, 750, 75)

    def display_login_page(self):
        self.screen.fill(self.bg_color)
        self.username_field.draw_input_field()
        self.password_field.draw_input_field()
        self.login_button.draw_button()
        self.skip_button.draw_button()
        self.create_button.draw_button()
        pygame.display.flip()
