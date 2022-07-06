import pygame
import pygame.font
from game.ui.button import Button
from game.ui.text_input import TextInput
from game.ui.hidden_text_input import HiddenTextInput


class LoginScreen:
    def __init__(self, ai_game) -> None:
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.login_button = Button(self, 575, 500, "login")
        self.skip_button = Button(self, 575, 725, "skip login")
        self.create_button = Button(self, 575, 275, "signup")
        self.bg_color = ai_game.settings.bg_color
        self.username_field = TextInput(self, 425, 375, 450, 75)
        self.password_field = HiddenTextInput(self, 425, 475, 450, 75)

    def display_login_page(self):
        self.screen.fill(self.bg_color)
        self.username_field.draw_input_field()
        self.password_field.draw_input_field()
        self.login_button.draw_button()
        self.skip_button.draw_button()
        self.create_button.draw_button()
        self.username_text_img = self.font.render(
            "Username", True, self.text_color, self.bg_color
        )
        self.username_rect = self.username_text_img.get_rect()
        self.username_rect.right = self.username_field.input_rect.left - 10
        self.username_rect.top = self.username_field.input_rect.top + 20
        self.screen.blit(self.username_text_img, self.username_rect)
        self.password_text_img = self.font.render(
            "Password", True, self.text_color, self.bg_color
        )
        self.password_rect = self.password_text_img.get_rect()
        self.password_rect.right = self.username_field.input_rect.left - 10
        self.password_rect.top = self.password_field.input_rect.top + 20
        self.screen.blit(self.password_text_img, self.password_rect)
        pygame.display.flip()
