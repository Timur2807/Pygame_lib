import pygame
from ship import Ship
from controls import events, update, update_bullets
from pygame.sprite import Group
from ino import Ino

def run():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
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