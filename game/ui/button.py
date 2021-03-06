import pygame.font


class Button:
    def __init__(self, ai_game, left, top, msg, width=200, height=50):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimensions and properties of the button.
        self.width, self.height = width, height
        self.button_color = pygame.Color("#14fff7")
        self.text_color = ai_game.settings.font_color
        self.font = pygame.font.Font("game/fonts/Orbitron-Regular.ttf", 24)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(left, top, self.width, self.height)
        # self.rect.center = self.screen_rect.center

        # the button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """TUrn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()

    def draw_button(self):
        # Draw blank button and then draw message.=
        self.msg_image_rect.center = self.rect.center
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
