import json
import os


class GameStats:
    """Track  statistics for alien invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start the Alien Invasion in an inactive state.
        self.local_high_score = self.load_high_scores()
        self.high_score = self.load_high_scores()
        self.level = 1

    def load_high_scores(self):
        if not os.path.isfile("highscore.json"):
            return 0
        with open("highscore.json") as f:
            data = json.load(f)

        return data.get("highscore", 0)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
