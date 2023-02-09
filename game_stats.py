class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.score = 0

        # Start Alien Invasion in an Active state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0
        self.read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.lifes_left = self.ai_settings.life_limit
        self.score = 0
        self.level = 1
        self.game_over = False

    def read_high_score(self):
        try:
            with open('data/high_score.txt', 'r') as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
