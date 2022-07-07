import pygame


class TextInput:
    def __init__(self, ai_game, left, top, width, height):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.text = ""
        self.base_font = pygame.font.Font(None, 75)
        self.color_active = pygame.Color("#14fff7")
        self.color_passive = pygame.Color("#090c9b")
        self.is_active = False
        self.input_rect = pygame.Rect(left, top, width, height)
        self.color = self.color_passive

    def draw_input_field(self):
        if self.is_active:
            self.color = self.color_active
        else:
            self.color = self.color_passive

        pygame.draw.rect(self.screen, self.color, self.input_rect)

        rendered_text = self.base_font.render(
            self.get_displayed_text(), True, (255, 255, 255)
        )
        self.screen.blit(rendered_text, (self.input_rect.x + 5, self.input_rect.y + 5))

    def get_displayed_text(self):
        return self.text
