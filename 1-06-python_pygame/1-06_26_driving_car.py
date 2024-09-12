# Трансформация поверхностей

# pygame.transform.scale
# pygame.transform.flip
# pygame.transform.rotate

# pygame.transform.scale(Surface, (width, height), DestSurface = None) -> Surface
# Surface - масштабируемая поверхность
# (width, height) новая ширина и высота


import pygame
pygame.init()

W, H = 600, 400
 
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Трансформация поверхностей")

 
clock = pygame.time.Clock()
FPS = 60
 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

# Получаем подготовленные поверхности с изображениями
bg_surf = pygame.image.load("images/car/sand.jpg").convert()
car_surf = pygame.image.load("images/car/car.bmp").convert()
finish_surf = pygame.image.load("images/car/finish.png").convert_alpha()

# Делаем прозрачный фон для машинки
car_surf.set_colorkey((255, 255, 255))

# Возможные положения машинки в пространстве
car_up = car_surf
car_down = pygame.transform.flip(car_surf, 0, 1) # переворот вдоль оси y = 1, переворот вдоль оси y = 0
car_left = pygame.transform.rotate(car_surf, 90) # поворот
car_right = pygame.transform.rotate(car_surf, -90)

# Вставили scale для масштабирования песка
bg_surf = pygame.transform.scale(bg_surf, (bg_surf.get_width()//3, bg_surf.get_height()//3))

# Выставили машинку по середине экрана
car_rect = car_surf.get_rect(center=(W//2, H//2))

car = car_up    # Текущее положение машинки
speed = 5       # Скорость машинки


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    bt = pygame.key.get_pressed()
    if bt[pygame.K_LEFT]:
        car = car_left
        car_rect.x -= speed
        if car_rect.x < 0:
            car_rect.x = 0
    elif bt[pygame.K_RIGHT]:
        car = car_right
        car_rect.x += speed
        if car_rect.x > W-car_rect.height:
            car_rect.x = W-car_rect.height
    elif bt[pygame.K_UP]:
        car = car_up
        car_rect.y -= speed
        if car_rect.y < 0:
            car_rect.y = 0
    elif bt[pygame.K_DOWN]:
        car = car_down
        car_rect.y += speed
        if car_rect.y > H-car_rect.height:
            car_rect.y = H-car_rect.height
 
    sc.blit(bg_surf, (0, 0))
    sc.blit(finish_surf, (0, 0))
    sc.blit(car, car_rect)
 
    pygame.display.update()
 
    clock.tick(FPS)