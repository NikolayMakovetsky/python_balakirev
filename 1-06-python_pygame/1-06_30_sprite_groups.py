# Чтобы избежать дублирования кода спрайты группируют, используя pygame.sprite.Group()


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

# Создадим группу спрайтов (шаров в нашем случае)
balls = pygame.sprite.Group()

# Загрузка фона
bg = pygame.image.load('images/flowballs/back1.jpg').convert()

speed = 1
# добавляем шары в группу
balls.add(Ball(W//2, 1, 'images/flowballs/ball_bear.png'),
          Ball(W//2-250, 2, 'images/flowballs/ball_fox.png'),
          Ball(W//2+100, 3, 'images/flowballs/ball_panda.png'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # рисуем фон
    sc.blit(bg, (0, 0))

    # отрисовка группы шаров
    balls.draw(sc)
  
    pygame.display.update()
    
    # реализация падения всех шаров группы
    balls.update(H)
     
    clock.tick(FPS)        
 
