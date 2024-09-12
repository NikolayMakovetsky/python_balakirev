# Модуль pygame.key отвечает за работу с клавиатурой
# функция pygame.key.get_pressed() возвращает информацию о состояниях клавиш в виде кортежа
# фактически эта функция даёт маску нажатых на клавиатуре клавиш
# Индекс клавиши 0 1 2 3 4 ... 100 ... 115 ...
#        кортеж (0 0 1 0 0 ...  1  ...  0  ...) 1 означает что клавиша нажата

# МИНУС pygame.key.get_pressed() !!!
# ТАМ НЕТ ИНДЕКСОВ ДЛЯ КЛАВИШ-МОДИФИКАТОРОВ: Shift, Ctrl, Alt и др.
# Соответственно для нажатия этих клавиш необходимо писать обработчики

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
speed = 5


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed() # получаем кортеж со статусами клавиш
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    
        
    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)