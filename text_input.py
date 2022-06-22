import pygame


class Text_Input:
    def __init__(self, ai_game, left, top, width, height):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.text = ""
        self.base_font = pygame.font.Font(None, 32)
        self.color_active = pygame.Color("lightskyblue3")
        self.color_passive = pygame.Color("chartreuse4")
        self.is_active = False
        self.input_rect = pygame.Rect(left, top, width, height)
        self.color = self.color_passive

    def draw_input_field(self):
        if self.is_active:
            self.color = self.color_active
        else:
            self.color = self.color_passive

        pygame.draw.rect(self.screen, self.color, self.input_rect)

        rendered_text = self.base_font.render(self.text, True, (255, 255, 255))
        self.screen.blit(rendered_text, (self.input_rect.x + 5, self.input_rect.y + 5))
