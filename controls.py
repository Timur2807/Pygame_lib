import pygame
import sys

def events(ship):
    """Обработка событий (нажатие клавиш.)"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # нажатие клавиши вправо
            if event.key == pygame.K_RIGHT:
                ship.mright = True
            elif event.key == pygame.K_LEFT:
                ship.mleft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.mright = False
            elif event.key == pygame.K_LEFT:
                ship.mleft = False
