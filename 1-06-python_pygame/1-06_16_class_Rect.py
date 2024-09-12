# class Rect
# помогает определять границы персонажей и окружающих предметов,
# а также узнавать моменты их столкновений
# Каждая поверхность Surface имеет метод Surface.get_rect(), который возвращает экземпляр класса Rect

import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Класс Rect")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60 
clock = pygame.time.Clock()


 
hero = pygame.Surface((40, 50))
hero.fill(BLUE)

rect = hero.get_rect() # возвратится прямоуг с коорд (0, 0) размером (40, 50)
print(rect) # <rect(0, 0, 40, 50)> вывели в консоль
            # иначе говоря мы получили ссылку на класс Rect
print(rect.center) # (20, 25)

# Свойства класса Rect:
# (x, y) topleft  | координаты верхнего левого угла
# top             | верхняя сторона (точка)
# topright        | правый верхний угол
# right           | правая сторона (точка)
# borromright     | правый нижний угол
# bottom          | нижняя сторона (точка)
# bottomleft      | левый нижний угол
# left            | левая сторона (точка)
# center          | координаты центра прямоугольника

# Surface.get_rect() имеет ряд дополнительных именованых параметров
 
sc.fill(WHITE)
sc.blit(hero, (100, 50))
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)    