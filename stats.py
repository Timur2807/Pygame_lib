class Stats():
    """Отслеживание статистики."""

    def __init__(self):
        """Создает статистику."""
        self.reset_stats()

    def reset_stats(self):
        """Статистика изменяющаяся во время игры."""
        self.ship_left = 2