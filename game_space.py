import pygame
from ship import Ship
from controls import events

def run():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Инопланетное вторжение.')
    bg_color = (230,230,230)
    ship = Ship(screen)

    while True:
        ship.update_ship()
        events(ship)
        screen.fill(bg_color)
        ship.output()
        pygame.display.flip()

run()