import pygame
import pygame.font
from game.ui.button import Button
from game.ui.text_input import TextInput
from game.ui.hidden_text_input import HiddenTextInput


class RegisterScreen:
    def __init__(self, ai_game) -> None:
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.title_image = pygame.image.load("game/images/title.png").convert_alpha()
        self.bg_color = ai_game.settings.bg_color
        self.username_field = TextInput(ai_game, 425, 375, 450, 75)
        self.password_field = HiddenTextInput(ai_game, 425, 475, 450, 75)
        self.register_button = Button(ai_game, 375, 575, "register")
        self.back_button = Button(ai_game, 625, 575, "back ")
        self.font = self.settings.font_primary
        self.text_color = self.settings.font_color
        self.username_field.input_rect.centerx = self.rect.centerx
        self.password_field.input_rect.centerx = self.rect.centerx

    def draw_register_screen(self):
        self.screen.fill(self.bg_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.top = 50
        self.title_image_rect.centerx = self.rect.centerx
        self.username_field.draw_input_field()
        self.password_field.draw_input_field()
        self.register_button.draw_button()
        self.back_button.draw_button()
        self.username_text_img = self.font.render(
            "Username:", True, self.text_color, self.bg_color
        )

        self.username_rect = self.username_text_img.get_rect()
        self.username_rect.right = self.username_field.input_rect.left - 10
        self.username_rect.top = self.username_field.input_rect.top + 20
        self.username_rect.centery = self.username_field.input_rect.centery
        self.screen.blit(self.username_text_img, self.username_rect)
        self.password_text_img = self.font.render(
            "Password:", True, self.text_color, self.bg_color
        )
        self.password_rect = self.password_text_img.get_rect()
        self.password_rect.right = self.username_field.input_rect.left - 10
        self.password_rect.top = self.password_field.input_rect.top + 20
        self.password_rect.centery = self.password_field.input_rect.centery
        self.screen.blit(self.password_text_img, self.password_rect)
        self.screen.blit(self.title_image, self.title_image_rect)
