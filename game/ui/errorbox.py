import pygame
from game.ui.button import Button


class ErrorBox:
    def __init__(self, ai_game, button_text):
        self.clock = pygame.time.Clock()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.message = ""
        self.rect = pygame.Rect(0, 0, 350, 200)
        self.rect.center = self.screen_rect.center
        self.exit_button = Button(
            ai_game, self.rect.left + 115, self.rect.bottom - 50, button_text, 100, 30
        )

    def set_message(self, message):
        self.message = message

    def draw_error_box(self):
        self.screen.fill((0, 255, 255), self.rect)
        self.message_image = self.font.render(
            self.message, True, self.text_color, (0, 255, 255)
        )
        self.message_image_rect = self.message_image.get_rect()
        self.screen.blit(self.message_image, self.rect)
        self.exit_button.draw_button()

        self.clock.tick(60)
