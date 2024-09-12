# Rect.move(x, y)     | возвращает новый прямоугольник и помещает его в x, y
# Rect.move_ip(x, y)  | меняет координаты текущего прямоугольника перемещая его в x, y
# Rect.clip(Rect)     | обрезает границы прямоугольника по указанным размерам переданного прямоугольника
# Rect.union(Rect)    | возвращает новый прямоугольник с результатом объединения двух прямоугольников в один
# Rect.union_ip       | объединяет два прямоугольника в один, указанный перед точкой
# Rect.fit(Rect)      | возвращает новый прямоугольник, смещенный и измененный по размеру переданного прямоугольника
# Rect.contains(Rect) | проверяет: содержится ли один прямоугольник внутри другого
# суффикс _ip означает что изменения коснутся текущего прямоугольника (как если бы метод применялся к конкретному объекту)

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


rect1 = pygame.Rect((0, 0, 30, 30))
rect2 = pygame.Rect((30, 30, 30, 30))

rect2.move_ip(20, 20) 
print(rect2) # <rect(50, 50, 30, 30)>

rect3 = rect2.union(rect1)
print(rect3) # <rect(0, 0, 80, 80)>
# при объединении два прямоугольника обрисовываются одним большим


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)    