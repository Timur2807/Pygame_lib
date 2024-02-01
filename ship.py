import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen):
        """Инициализация космического корабля."""
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ship3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.ship_height = self.rect.height
        self.mright = False
        self.mleft = False

    def output(self):
        """Рисование корабля."""
        self.screen.blit(self.image,self.rect)

    def update_ship(self):
        """Изменение позиции корабля"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_ship(self):
        """Повторно отрисовывает корабль по центру экрана (снизу)"""
        self.center = self.screen_rect.centerx
