
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


flStartDraw = False # flag
sp = None # start point of rect
ep = None # end point of rect

sc.fill(WHITE)
pygame.draw.rect(sc, BLUE, (100, 100, -50, -50))
pygame.display.update()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # единичное событие
            flStartDraw = True
            sp = event.pos
        elif event.type == pygame.MOUSEMOTION: # постоянно генерирующееся событие
            if flStartDraw:
                pos = event.pos

                width = pos[0] - sp[0]
                height = pos[1] - sp[1]
                # print(width, height)

                sc.fill(WHITE)
                pygame.draw.rect(sc, RED, (sp[0], sp[1], width, height))
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: # единичное событие
            flStartDraw = False



    clock.tick(FPS)