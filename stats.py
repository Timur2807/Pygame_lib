class Stats():
    """Отслеживание статистики."""

    def __init__(self):
        """Создает статистику."""
        self.reset_stats()
        self.run_game = True
        with open('rec_score.txt', 'r') as file:
            self.rec_score = int(file.readline())

    def reset_stats(self):
        """Статистика изменяющаяся во время игры."""
        self.ship_left = 3
        self.score = 0