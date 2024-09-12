# pygame.event - модуль отвечающий за обработку событий
# В очереди событий pygame.event.get() находятся объекты Event c атрибутом type
# event.type == pygame.KEYDOWN    | клавиша на клавиатуре нажата
# event.type == pygame.KEYUP      | клавиша на клавиатуре отпущена

import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от клавиатуры")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60 # число кадров в сек
clock = pygame.time.Clock()

# начальное положение прямоугольника на экране
x = W // 2
y = H // 2
# скорость перемещения прямоугольника
speed = 5

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN: # event.type
            if event.key == pygame.K_LEFT: # event.key
                x -= speed
            elif event.key == pygame.K_RIGHT: # event.key
                x += speed
    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)