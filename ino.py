import pygame

class Ino(pygame.sprite.Sprite):
    """Инициализация пришельцев."""
    def __init__(self, screen):
        super(Ino, self).__init__()
        """Инициализируем и задаем начальную позицию."""
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Отрисовка пришельцев."""
        self.screen.blit(self.image, self.rect)

