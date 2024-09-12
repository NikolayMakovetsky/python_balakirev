import pygame
pygame.init()
 
W, H = 600, 400
 
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Изображения")

 
clock = pygame.time.Clock()
FPS = 60
 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

# Отображение фона в виде песка
bg_surf = pygame.image.load("images/car/sand.jpg")
sc.blit(bg_surf, (0, 0))

# Машина
car_surf = pygame.image.load("images/car/car.bmp") # load возвращает поверхность, на кот будет нарисовано изображение из файла
car_rect = car_surf.get_rect(center=(W//2, H//2))

# Укажем какой цвет на картинке с машиной необходимо воспринимать как прозрачный
car_surf.set_colorkey((255, 255, 255)) # RGB(255, 255, 255) параметры белого цвета

# Отображение машины
sc.blit(car_surf, car_rect)

# Отображение финишных флагов (ОНИ УЖЕ НА ПРОЗРАЧНОМ ФОНЕ)
finish_surf = pygame.image.load("images/car/finish.png")
sc.blit(finish_surf, (0, 0))

# Прорисовка экрана
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)