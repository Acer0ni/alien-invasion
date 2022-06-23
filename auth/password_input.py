import pygame
from auth.text_input import TextInput


class PasswordInput(TextInput):
    def get_displayed_text(self):
        return "*" * len(self.text)
