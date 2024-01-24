import pygame.font

class Scores():
    """Вывод игровой информации."""
    def __init__(self, screen, stats):
        """Инициализируем подсчет очков."""
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()
        self.text_color = (250, 0, 0)
        self.font = pygame.font.SysFont(None,32)
        self.image_score()
        self.image_rec_score()

    def image_score(self):
        """Преобразовывает текст счета в графическое изображение. """
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color,(0, 0, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_rec_score(self):
        """Отрисовывает рекорд прошлых игр."""
        self.rec_score_img = self.font.render(str(self.stats.rec_score),
        True, self.text_color, (0, 0, 0))
        self.score_rec_rect = self.rec_score_img.get_rect()
        self.score_rec_rect.centerx = self.screen_rect.centerx
        self.score_rec_rect.top = self.screen_rect.top + 20

    def score_show(self):
        """Выводит на экран СЧЕТ."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.rec_score_img, self.score_rec_rect)


