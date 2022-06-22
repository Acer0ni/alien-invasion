import json


class Gamestats:
    """Track  statistics for alien invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start the Alien Invasion in an inactive state.
        self.game_active = False
        self.logged_in = False
        self.has_account = False
        with open("highscore.json") as json_file:
            data = json.load(json_file)
        # High scores should never be reset.
        self.high_score = data["highscore"]
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
