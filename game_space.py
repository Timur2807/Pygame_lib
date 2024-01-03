import pygame
import sys
from ship import Ship

def run():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Инопланетное вторжение.')
    bg_color = (230,230,230)
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        ship.output()
        pygame.display.flip()

run()