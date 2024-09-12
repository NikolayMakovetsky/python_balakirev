import pygame
 
pygame.init()
 
W = 600
H = 400
 
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Класс Rect")
 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
FPS = 60                # число кадров в секунду
clock = pygame.time.Clock()
 
ground = H-70           # высота земли
jump_force = 20         # сила прыжка
move = jump_force+1     # текущая вертикальная скорость

# Создание и установка героя на игровом окне
hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(centerx=W//2)  # герой по центру клиентского окна (по оси х)
rect.bottom = ground                # герой на уровне земли
print(rect.bottom)                  # 330 !!!

# Для перерисовки не всего окна, а только той части где прыгает герой
rect_update = pygame.Rect(rect.x, 0, rect.width, ground)

sc.fill(GREEN) # чтобы был однотонный фон можно тут белый цвет покраски установить
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN: # нажатие на клавишу пробел
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = -jump_force
    
    # ПРЫЖОК
    if move <= jump_force:
        if rect.bottom + move < ground:
            # rect.bottom = 330 (ground)
            rect.bottom += move # 330(-20)310(-19)291...120(+0)120(+1)121(+2)123...291(+19)310
            if move < jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force+1
 
    sc.fill(WHITE) # белую полоску получаем на экране из-за (rect_update) ниже!
    sc.blit(hero, rect)
    pygame.display.update(rect_update) # rect_update подставили, чтобы перерисовывалась только часть окна
 
    clock.tick(FPS)