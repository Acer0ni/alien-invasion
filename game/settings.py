import pygame


class Settings:
    """a class to store all settings for ALien invasion."""

    def __init__(self):
        """initialize the game's static settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = pygame.Color("#1c1c1c")
        self.font_color = pygame.Color("#7c77b9")

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings

        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speedup_scale = 1.25
        # Howm quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction ofg 1 represents right; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
