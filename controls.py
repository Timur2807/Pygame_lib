import pygame
import sys
from bullet import Bullet
from ino import Ino
import time
from stats import Stats
def events(screen, ship, bullets):
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
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.mright = False
            elif event.key == pygame.K_LEFT:
                ship.mleft = False

def update(bg_color, screen, stats, scores, ship, inos, bullets):
    """Обновление Экрана."""
    screen.fill(bg_color)
    scores.score_show()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, scores, inos, bullets,settings, ship):
    """Обновлять позиции пули."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,inos,True,True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        scores.image_score()
        chekc_rec_score(stats, scores)
        scores.image_ships()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos, settings, ship)

def update_inos(stats, screen, ship, scores, inos, bullets, settings):
    """Обновление позиции пришельцев."""
    inos.update()
    if pygame.sprite.spritecollideany(ship, inos):
        ship_kill(stats, screen, ship, scores, inos, bullets, settings)
    inos_chekc(stats, screen, ship, scores, inos, bullets, settings)

def ship_kill(stats, screen, ship, scores, inos, bullets, settings):
    """Столкновение корабля с пришельцами."""
    if stats.ship_left > 0:
        stats.ship_left -= 1
        scores.image_ships()
        inos.empty()
        bullets.empty()
        create_army(screen, inos, settings, ship)
        ship.create_ship()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def inos_chekc(stats, screen, ship, scores, inos, bullets, settings):
    """Проверка положекния пришельцев."""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            ship_kill(stats, screen, ship, scores, inos, bullets, settings)
            break


def create_army(screen, inos, settings, ship):
    """Создаем армию пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_width = int((settings.screen_width - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_height = int((settings.screen_height - ship.ship_height - 2 * ino_height) / ino_height)
    for ino_row in range(number_ino_height):
        for ino_number in range(number_ino_width):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * ino_row
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * ino_row
            inos.add(ino)

def chekc_rec_score(stats, scores):
    """Прверка новых рекордов."""
    if stats.score > stats.rec_score:
        stats.rec_score = stats.score
        scores.image_rec_score()
        with open('rec_score.txt', 'w') as file2:
            file2.write(str(stats.rec_score))