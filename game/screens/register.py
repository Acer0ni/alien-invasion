import pygame
from game.ui.button import Button
from game.ui.text_input import TextInput
from game.ui.hidden_text_input import HiddenTextInput


class RegisterScreen:
    def __init__(self, ai_game) -> None:
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.bg_color = ai_game.settings.bg_color
        self.username_field = TextInput(self, 200, 200, 750, 75)
        self.password_field = HiddenTextInput(self, 200, 300, 750, 75)
        self.register_button = Button(self, 450, 450, "register")
        self.back_button = Button(self, 450, 675, "back ")

    def draw_register_screen(self):
        self.screen.fill(self.bg_color)
        self.username_field.draw_input_field()
        self.password_field.draw_input_field()
        self.register_button.draw_button()
        self.back_button.draw_button()
        pygame.display.flip()
