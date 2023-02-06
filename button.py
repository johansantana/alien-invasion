import pygame.font


class Button():
    def __init__(self, ai_settings, screen, img_path, size):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the dimensions and properties of the button
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()

        # build the button's rect object and center it.
        self.rect.center = self.screen_rect.center

        # the button message needs to be prepped only once.
    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.blit(self.image, self.rect)
