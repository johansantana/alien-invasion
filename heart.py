import pygame
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
