# pygame.mouse.get_pressed() возвращает кортеж (1, 0, 0) # левая нажата, средняя отпущена, правая отпущена

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

FPS = 60 
clock = pygame.time.Clock()

sp = None 

sc.fill(WHITE)
pygame.display.update()

pygame.mouse.set_visible(False) # Установить невидимым курсор мыши

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # отрисовка собственного курсора мыши
    sc.fill(WHITE)
    pos = pygame.mouse.get_pos()
    print(pos)
    if pygame.mouse.get_focused(): # отрисовываем только если курсор в пределах клиентской области окна
        pygame.draw.circle(sc, GREEN, pos, 7)


    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        if sp is None:
            sp = pos
        
        width = pos[0] - sp[0]
        height = pos[1] - sp[1]

        sc.fill(WHITE)
        pygame.draw.rect(sc, BLUE, (sp[0], sp[1], width, height))
        
    else:
        sp = None
    
    pygame.display.update()
 
    clock.tick(FPS)