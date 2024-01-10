import pygame
from ship import Ship
from controls import events, update, update_bullets
from pygame.sprite import Group
from ino import Ino
from setting import Settings

def run():
    settings = Settings(screen_width=800, screen_height=600)
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Инопланетное вторжение.')
    bg_color = (0,0,0)
    ship = Ship(screen)
    bullets = Group()
    ino = Ino(screen)

    while True:
        events(screen, ship, bullets)
        ship.update_ship()
        update(bg_color, screen, ship, ino, bullets)
        update_bullets(bullets)


run()