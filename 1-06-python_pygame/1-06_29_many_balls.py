# Cпрайт – это любой подвижный объект

import pygame
# from ball import Ball

# ===========================ball.py==============================

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
    
    # Падение шара
    def update(self, *args): # переопределение метода базового класса Sprite
        if self.rect.y < args[0] - 20: # args[0] - высота клиентской области окна (см. класс Sprite)
            self.rect.y += self.speed
        else:
            self.rect.y = 0

# ==============================================================


pygame.init()
 
BLACK = (0, 0, 0)
W, H = 1000, 570
 
sc = pygame.display.set_mode((W, H))
 
clock = pygame.time.Clock()
FPS = 60

# Загрузка фона
bg = pygame.image.load('images/flowballs/back1.jpg').convert()

speed = 1
# создаем шары
b1 = Ball(W//2, speed, 'images/flowballs/ball_bear.png')
b2 = Ball(W//2-250, 2, 'images/flowballs/ball_fox.png')
b3 = Ball(W//2+100, 3, 'images/flowballs/ball_panda.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # рисуем фон
    sc.blit(bg, (0, 0))

    # рисуем шары
    sc.blit(b1.image, b1.rect)
    sc.blit(b2.image, b2.rect)
    sc.blit(b3.image, b3.rect)
  
    pygame.display.update()
    
    # падение шаров
    b1.update(H)
    b2.update(H)
    b3.update(H)
     
    clock.tick(FPS)        
 
