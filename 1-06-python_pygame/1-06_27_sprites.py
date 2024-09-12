# В игровом процессе спрайт – это любой подвижный объект
# И когда таких объектов много, то класс: pygame.sprite.Sprite
# значительно облегчает их обработку

import pygame
# from ball import Ball

# ===========================ball.py==============================
# лучшая практика разместить этот класс в отдельном файле ball.py 
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self) # конструктор базового класса Sprite
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

# Здесь мы определяем наш собственный класс Ball, наследуя его от базового класса Sprite.
# В результате мы расширяем функциональность этого базового класса,
# определяя в конструкторе два обязательных свойства:
#     image   | графическое представление спрайта (ссылка на Surface)
#     rect    | положение и размер спрайта
# Затем, эти свойства будут автоматически использоваться для обработки групп спрайтов
# Поэтому они необходимы и должны называться именно так
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
b1 = Ball(W//2, 'images/flowballs/ball_bear.png') # создаем шар (координата х, изображение)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # Прорисовка
    sc.blit(bg, (0, 0))         # рисуем фон
    sc.blit(b1.image, b1.rect)  # рисуем шар
    pygame.display.update()
 
    # Падение шара
    if b1.rect.y < H-20:
        b1.rect.y += speed
    else:
        b1.rect.y = 0
    
    clock.tick(FPS)        
 
