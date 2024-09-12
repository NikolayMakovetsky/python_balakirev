# pygame.draw
# pygame.draw.rect(surface=, ...)     | прямоугольник
# pygame.draw.line(surface=, ...)     | линия
# pygame.draw.aaline(surface=, ...)   | сглаженная линия
# pygame.draw.lines(surface=, ...)    | ломаная линия
# pygame.draw.aalines(surface=, ...)  | ломаная сглаженная линия
# pygame.draw.polygon(surface=, ...)  | полигон
# pygame.draw.circle(surface=, ...)   | круг
# pygame.draw.ellipse(surface=, ...)  | эллипс
# pygame.draw.arc(surface=, ...)      | дуга

# Элементы накладываются на surface (поверхность)
# функция pygame.display.set_mode((..., ...)) как раз и возвращает объект Surface
# Поверхностей может быть несколько 
# Базовая поверхность - клиентская область окна

# Базовая поверхность имеет 2 стороны: лицевую (B) и обратную (А) и
# использует механизм рисования "буферизация вывода", при котором
# объекты рисуются на обратной стороне поверхности.
# Чтобы увидеть объект после отрисовки поверхность нужно "перевернуть" методом flip()
# "буферизация вывода" дает возможность скрыть от пользователя сам процесс отрисовки примитивов

import pygame
pygame.init()

W, H = 600, 400
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Графические примитивы")

clock = pygame.time.Clock()
FPS = 30

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.draw.rect(sc, WHITE, (10, 10, 50, 100)) # (sc, colorRGB, (x, y, width, high))
                                                         # начало координат - лев верх угол окна
                                                         # px единица измерения                                                         
pygame.draw.rect(sc, BLUE, (70, 10, 50, 100), 2) # 2 толщина линии в px

pygame.draw.line(sc, GREEN, (200, 20), (350, 50), 3)
pygame.draw.aaline(sc, GREEN, (200, 40), (350, 70), 1) # для aaline толщина мб только 1 px

pygame.draw.lines(sc, RED, True, [(200, 80), (250, 80), (300, 200)], 3) # True означает что ломаную линию нужно замкнуть
pygame.draw.aalines(sc, RED, True, [(300, 80), (350, 80), (400, 200)], 3) # для сглаженных линий параметр толщины всегда выставляется в 1 px

pygame.draw.polygon(sc, WHITE, [[150, 210], [180, 250], [90, 290], [30, 230]])
pygame.draw.polygon(sc, WHITE, [[150, 310], [180, 350], [90, 390], [30, 330]], 1)

pygame.draw.circle(sc, BLUE, (300, 250), 40) # указываем центр и радиус
pygame.draw.ellipse(sc, BLUE, (300, 300, 100, 50), 1) # указываем прямоуг в который будет вписан эллипс

pi = 3.14
pygame.draw.arc(sc, RED, (450, 30, 50, 150), pi, 2*pi, 5) # указываем прямоуг в кот будет вписана дуга, начальный угол, коненчный угол

pygame.display.flip()
# pygame.display.update(rectangle= ...) # работает как flip, но перерисовывает только отдельную область экрана
                                        # update без параметров перерисует всю область
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)
