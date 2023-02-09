import pygame.font
import os
from pygame.sprite import Group

from extras import Heart


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information
        self.text_color = 255, 255, 255
        self.font = pygame.font.Font(os.path.join("fonts", "Mouse.otf"), 24)

        # Prepare the initial score images
        self.prep_images()

    def prep_images(self):
        """Prepare all images."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_hearts()

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            "Score: " + score_str, True, self.text_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 24

    def show_score(self):
        """Draw scores and ships to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Draw ships
        self.hearts.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            "High score: " + high_score_str, True, self.text_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into an rendered image."""
        self.level_image = self.font.render(
            "Level " + str(self.stats.level), True, self.text_color)

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.bottom = self.score_rect.bottom + 50

    def prep_hearts(self):
        """Show how many hearts are left."""
        self.hearts = Group()
        for ship_number in range(self.stats.lifes_left):
            heart = Heart(self.ai_settings, self.screen)
            heart.rect.x = 20 + ship_number * (heart.rect.width + 20)
            heart.rect.y = 20
            self.hearts.add(heart)
