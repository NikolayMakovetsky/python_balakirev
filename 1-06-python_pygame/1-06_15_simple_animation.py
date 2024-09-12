# Surface.blit(source, pos, ...)  | отображение графической информации на поверхность
# Surface.set_alpha(alpha)        | (0...255) задает степень прозрачности

import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Класс Surface")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60 
clock = pygame.time.Clock()

surf = pygame.Surface((W, 200)) # полоса во всю ширину окна
bita = pygame.Surface((50, 10)) # горизонтальный прямоугольник
surf.fill(BLUE)
bita.fill(RED)

x, y = 0, 0     # положение поверхности surf на поверхности sc
bx, by = 0, 150 # положение поверхности bita на поверхности surf

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf.fill(BLUE)
    surf.blit(bita, (bx, by)) # на поверхности surf отобразить bita
    if bx < W: # логика движения bita (красный прямоугольник)
        bx += 5
    else:
        bx = 0
 
    if y < H: # логика движения surf (синяя полоса)
        y += 1
    else:
        y = 0
 
    sc.fill(WHITE)
    sc.blit(surf, (x, y)) # на поверхности sc отобразить surf
    
    pygame.display.update() # обновить экран
    
    clock.tick(FPS)            