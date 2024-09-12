# pygame.MOUSEBUTTONDOWN  | нажатие кнопки мыши
# pygame.MOUSEBUTTONUP    | отпускание кнопки мыши
# pygame.MOUSEMOTION      | перемещение курсора мыши
# pygame.MOUSEWHEEL       | кручение колесика мыши

# event.button = 1    нажата левая кнопка мыши
# event.button = 2    нажата средняя кнопка-колесико
# event.button = 3    нажата правая кнопка мыши
# event.button = 4    колесико перемещено вверх
# event.button = 5    колесико перемещено вниз

# event.pos = (x, y)    x, y - координаты мыши на главном экране
# event.rel существует только для MOUSEMOTION !
# event.rel = (x, y)    x, y - параметры смещения курсора относительно предыдущего положения

import pygame



pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от мыши")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60 # число кадров в сек
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка:", event.button) # нажатия
        elif event.type == pygame.MOUSEMOTION:
            print("Позиция мыши:", event.pos) # текущая позиция
            print("Смещение:", event.rel) # смещение относит предыдущ положения

    clock.tick(FPS)