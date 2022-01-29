class Settings:
    """a class to store all settings for ALien invasion."""

    def __init__(self):
        """initialize the game's settins."""
        #screen settings 
        self.screen_width =1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Ship settings
        self.ship_speed = 1.5