import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initialize game, settings and create a screen object.
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_hight))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)

        # Ship moving
        ship.update()

        bullets.update()

        gf.update_bullets(bullets)

        # Update the screen
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
