# Модифицируем программу
# 1. Пусть новый шар появляется каждые 2 секунды
# 2. Пусть каждый шар падает только до земли, а потом исчезает

import pygame
# from ball import Ball
from random import randint

# ===========================ball.py==============================
# Что нам дает наследование от класса Sprite?
# 1. add() добавление в группу объектов
# 2. kill() удаление из всех групп
# 3. remove(group1) удаление из конкретной группы 

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group): # изменили конструктор класса!!!
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)

    # Падение шара
    # Шар долетающий до земли теперь должен исключаться из группы (и из игры)
    def update(self, *args):
        if self.rect.y < args[0] - 20: 
            self.rect.y += self.speed
        else:
            self.kill() # исключение шара из группы

# ==============================================================

pygame.init()

# эта функция каждые 2000мс(2с) будет генерировать событие pygame.USEREVENT
# в списке событий, и по этому событию мы будем создавать новый шар
pygame.time.set_timer(pygame.USEREVENT, 2000)

BLACK = (0, 0, 0)
W, H = 1000, 570
 
sc = pygame.display.set_mode((W, H))
 
clock = pygame.time.Clock()
FPS = 60

# Подготовим поверхности с разными изображениями шаров
balls_images = ['ball_bear.png', 'ball_fox.png', 'ball_panda.png']
balls_surf = [pygame.image.load('images/flowballs/'+path).convert_alpha() for path in balls_images]


def createBall(group):
    """Создание шара со случайными параметрами"""
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1, 4)
 
    return Ball(x, speed, balls_surf[indx], group)

# Загрузка фона
bg = pygame.image.load('images/flowballs/back1.jpg').convert()

# Создадим группу спрайтов (шаров в нашем случае)
balls = pygame.sprite.Group()

# Создаем первый шар в группе balls до начала главного цикла
createBall(balls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)            
    # рисуем фон
    sc.blit(bg, (0, 0))

    # отрисовка группы шаров
    balls.draw(sc)
  
    pygame.display.update()
    
    # реализация падения всех шаров группы
    balls.update(H)
     
    clock.tick(FPS)        
 
