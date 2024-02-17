from ship import Ship
from controls import *
from pygame.sprite import Group
from setting import Settings
from stats import Stats
from scores import Scores


def run():
    settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Инопланетное вторжение.')
    bg_color = (0, 0, 0)
    ship = Ship(screen)
    bullets = Group()
    inos = Group()
    create_army(screen, inos, settings, ship)
    stats = Stats()
    scores = Scores(screen, stats)


    while True:
        events(screen, ship, bullets)
        if stats.run_game:
            ship.update_ship()
            update(bg_color, screen, stats, scores, ship, inos, bullets)
            update_bullets(screen, stats, scores, inos, bullets, settings, ship)
            update_inos(stats, screen, ship, scores, inos, bullets, settings)


run()