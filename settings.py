class Settings():
    def __init__(self):
        """Initialize the game's static settings"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = 12, 15, 20
        self.pixel_size = 6.25

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = self.pixel_size
        self.bullet_height = 15
        self.bullet_color = 240, 100, 60
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 8

        # how quickly the game speeds up
        self.speedup_scale = 1.3
        # how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.7

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
