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


surf = pygame.Surface((200, 200))
surf.fill(RED)
pygame.draw.circle(surf, GREEN, (100, 100), 80)

surf_alpha = pygame.Surface((W, 100))
pygame.draw.rect(surf_alpha, BLUE, (0, 0, W, 100))
surf_alpha.set_alpha(128)

# Сначала отображается sc, потом на ней surf, потом на surf уже surf_alpha полупрозрачно
surf.blit(surf_alpha, (0, 50))
sc.blit(surf, (50, 50)) # отображение поверхности surf на главной поверхности sc
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    clock.tick(FPS)            