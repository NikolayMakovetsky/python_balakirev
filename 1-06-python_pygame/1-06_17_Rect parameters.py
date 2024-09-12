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

# Surface.get_rect() имеет ряд дополнительных именованых параметров
# Для определения начального положения координат объекта Rect есть доп параметры
# rect = hero.get_rect(topleft=(200, 50)) # появление героя с отступом 200 по горизонтали, 50 по вертикали
# rect = hero.get_rect(center = (W//2, H//2)) # герой на старте по центру клиентского окна
# rect = hero.get_rect(centerx = W//2, centery = H//2) # центрируем отдельно по x и по y

 
hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(center = (W//2, H//2))
print(rect)
print(rect.center)

sc.fill(WHITE)
sc.blit(hero, rect) # метод blit автоматом вытащит из rect координаты topleft угла !!!
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)    