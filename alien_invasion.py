import pygame
import pygame.mixer
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from extras import Controls, GameOver

# initializes game and create screen object
pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption('Alien Invasion')

# Create an instance to store game statistics and create a scoreboard.
stats = GameStats(ai_settings)
sb = Scoreboard(ai_settings, screen, stats)

# start music
pygame.mixer.music.load("sounds/bg_music.wav")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

ship = Ship(ai_settings, screen)

# make a group to store bullets in
bullets = Group()

# make an alien
aliens = Group()

# create the fleet of aliens
gf.create_fleet(ai_settings, screen, ship, aliens)

# make the play button
play_button = Button(ai_settings, screen,
                     img_path='images/play.png', size=(100, 100))
controls = Controls(screen, play_button)
game_over_title = GameOver(screen)

# start the main loop for the game.
while True:
    gf.check_events(ai_settings, screen, stats, sb,
                    play_button, ship, aliens, bullets)

    if stats.game_active:
        ship.update()
        gf.update_bullets(ai_settings, screen, stats,
                          sb, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen,
                         sb, ship, aliens, bullets, game_over_title)

    gf.update_screen(ai_settings, screen, stats, sb, ship,
                     aliens, bullets, play_button, controls)
