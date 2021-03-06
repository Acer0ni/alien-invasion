import pygame
import pygame.font
import ptext
from game.ui.button import Button
from game.ui.text_input import TextInput
from game.ui.hidden_text_input import HiddenTextInput


class LoginScreen:
    def __init__(self, ai_game) -> None:
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.title_image = pygame.image.load("game/images/title.png").convert_alpha()
        self.text_color = ai_game.settings.font_color
        self.font = ai_game.settings.font_primary
        self.login_button = Button(ai_game, 500, 575, "login")
        self.skip_button = Button(ai_game, 725, 575, "skip login")
        self.create_button = Button(ai_game, 275, 575, "signup")
        self.bg_color = ai_game.settings.bg_color
        self.username_field = TextInput(ai_game, 425, 375, 450, 75)
        self.password_field = HiddenTextInput(ai_game, 425, 475, 450, 75)
        self.rect = self.screen.get_rect()
        self.username_field.input_rect.centerx = self.rect.centerx
        self.password_field.input_rect.centerx = self.rect.centerx

    def display_login_page(self):
        self.screen.fill(self.bg_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.top = 50
        self.title_image_rect.centerx = self.rect.centerx

        self.username_field.draw_input_field()
        self.password_field.draw_input_field()
        self.login_button.draw_button()
        self.skip_button.draw_button()
        self.create_button.draw_button()
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
        ptext.draw(
            "Please create an account if this your first time playing. If you skip logging in, \nthe global highscore will still attempt to load but your score will only be saved locally",
            (self.create_button.rect.left, self.create_button.rect.bottom + 25),
            color=self.text_color,
            fontname="game/fonts/Orbitron-Regular.ttf",
            fontsize=20,
            centerx=self.rect.centerx,
        )
