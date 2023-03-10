import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and sets its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load animation images
        self.main_image = pygame.image.load('images/ship.png')
        self.right_image = pygame.image.load('images/right_ship.png')
        self.left_image = pygame.image.load('images/left_ship.png')

        # load the ship image and get its rect
        self.size = (50, 50)
        self.image = self.main_image
        self.image = pygame.transform.scale(self.image, self.size)

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        self.center = float(self.rect.centerx)

        # movement flag
        self.movement_right = False
        self.movement_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.movement_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            self.image = self.right_image
            self.image = pygame.transform.scale(self.image, self.size)
        if self.movement_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            self.image = self.left_image
            self.image = pygame.transform.scale(self.image, self.size)
        if not self.movement_left and not self.movement_right:
            self.image = self.main_image
            self.image = pygame.transform.scale(self.image, self.size)

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx
