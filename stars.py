import pygame

class Stars(pygame.sprite.Sprite):
    """Создание звезд."""
    def __init__(self, screen):
        """Инициализация звезды."""
        super(Stars, self).__init__()
        self.screen = screen
        self.image_star = pygame.image.load('images/star.png')
        self.rect = self.image_star.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_star(self):
        """Отрисовка звезд."""
        self.screen.blit(self.image_star, self.rect)
