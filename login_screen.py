import pygame
from button import Button


class Login_Screen:
    def __init__(self, ai_game) -> None:
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.username_text = ""
        self.password_text = ""
        self.base_font = pygame.font.Font(None, 32)
        self.base_font = pygame.font.Font(None, 32)
        self.username_rect = pygame.Rect(200, 200, 140, 32)
        self.color_active = pygame.Color("lightskyblue3")
        self.color_passive = pygame.Color("chartreuse4")
        self.username_active = False
        self.password_active = False
        self.login_button = Button(self, "login")
        self.bg_color = ai_game.settings.bg_color

    def display_login_page(self):
        self.screen.fill(self.bg_color)
        if self.username_active:
            self.username_color = self.color_active
        else:
            self.username_color = self.color_passive

        pygame.draw.rect(self.screen, self.username_color, self.username_rect)

        username_img = self.base_font.render(self.username_text, True, (255, 255, 255))
        self.screen.blit(
            username_img, (self.username_rect.x + 5, self.username_rect.y + 5)
        )
        self.login_button.draw_button()
        pygame.display.flip()
