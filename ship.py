import pygame

class Ship():
    def __init__(self,screen):
        """Инициализация  космического корабля."""
        self.screen = screen
        self.image = pygame.image.load('images/shop_2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """Рисование корабля."""
        self.screen.blit(self.image,self.rect)

    def update_ship(self):
        """Изменение позиции корабля"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1
