import pygame
import pygame.font
import os
from pygame.sprite import Sprite


class Heart(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the ship and sets its starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get its rect
        self.image = pygame.image.load('images/heart.png')
        self.image = pygame.transform.scale(self.image, (31.25, 31.25))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


class Controls():
    """A class to show the controls."""

    def __init__(self, screen, play_button):
        """Initialize controls attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Font settings for controls
        self.text_color = 255, 255, 255
        self.font = pygame.font.Font(os.path.join("fonts", "Mouse.otf"), 24)

        # prepare the images
        self.prep_images(play_button)

    def prep_images(self, play_button):
        """Prepare all images."""
        self.prep_text(play_button)
        self.prep_arrows()
        self.prep_space()

    def prep_text(self, play_button):
        """Prepare the text image."""
        text = "How to play:"
        self.text_image = self.font.render(text, True, self.text_color)

        # display it below the play button
        self.text_rect = self.text_image.get_rect()
        self.text_rect.top = play_button.rect.bottom + 30
        self.text_rect.centerx = self.screen_rect.centerx

    def prep_arrows(self):
        """Prepare the arrows."""
        self.prep_arrow_left()
        self.prep_arrow_right()

    def prep_arrow_left(self):
        """Prepare the left arrow."""
        self.arrow_left_image = pygame.image.load('images/left_key.png')
        self.arrow_left_image = pygame.transform.scale(
            self.arrow_left_image, (45.5, 42))
        self.arrow_left_rect = self.arrow_left_image.get_rect()

        self.arrow_left_rect.top = self.text_rect.bottom + 10
        self.arrow_left_rect.x = self.text_rect.left - 32

    def prep_arrow_right(self):
        """Prepare the right arrow."""
        self.arrow_right_image = pygame.image.load('images/right_key.png')
        self.arrow_right_image = pygame.transform.scale(
            self.arrow_right_image, (45.5, 42))
        self.arrow_right_rect = self.arrow_right_image.get_rect()

        self.arrow_right_rect.top = self.text_rect.bottom + 10
        self.arrow_right_rect.left = self.arrow_left_rect.right + 10

    def prep_space(self):
        """Prepare the space key"""
        self.space_image = pygame.image.load('images/space_key.png')
        self.space_image = pygame.transform.scale(
            self.space_image, (105, 42))
        self.space_rect = self.space_image.get_rect()

        self.space_rect.top = self.text_rect.bottom + 10
        self.space_rect.left = self.arrow_right_rect.right + 10

    def show_controls(self):
        """Draw images to the screen"""
        self.screen.blit(self.text_image, self.text_rect)
        self.screen.blit(self.arrow_left_image, self.arrow_left_rect)
        self.screen.blit(self.arrow_right_image, self.arrow_right_rect)
        self.screen.blit(self.space_image, self.space_rect)


class GameOver():
    """A class that show a game over title."""

    def __init__(self, screen):
        """Initialize game over title attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Font settings for game over title
        self.text_color = 255, 255, 255
        self.font = pygame.font.Font(
            os.path.join("fonts", "Mouse.otf"), 42)

        text = 'Game Over'
        self.text_image = self.font.render(text, True, self.text_color)

        # position the text
        self.text_rect = self.text_image.get_rect()
        self.text_rect.y = 100
        self.text_rect.centerx = self.screen_rect.centerx

    def draw_text(self):
        """Draw the game over text to the screen."""
        self.screen.blit(self.text_image, self.text_rect)
