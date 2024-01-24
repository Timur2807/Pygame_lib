import pygame

class Bullet(pygame.sprite.Sprite):
    """Отрисовка пули."""
    def __init__(self,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 200, 12)
        self.color = 250, 0, 0
        self.speed = 1.5
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули по оси У."""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Отрисовка на экране пули."""
        pygame.draw.rect(self.screen, self.color, self.rect)