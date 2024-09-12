import pygame
pygame.init()
 
W, H = 600, 400
 
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Конвертация пикселей загруженных изображений")

 
clock = pygame.time.Clock()
FPS = 60
 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

# Формат представления пикселей поверхностей:
# bg_surf, car_surf, finish_surf
# отличается от формата представления пикселей базовой поверхности sc
# Из-за этого метод blit выполняется медленно, так как перед его исполнением
# происходит преобразование пикселей в нужный формат
# Как ускорить процесс?
# Принудительно осуществить
# Перевод пикселей загруженных изображений в формат пикселей главной поверхности
# методы convert() и convert_alpha()
# это методы класса Surface, которые возвращают новую поверхность
# с измененным представлением пикселей
# При этом прежняя поверхность остается без изменений

bg_surf = pygame.image.load("images/car/sand.jpg").convert()
car_surf = pygame.image.load("images/car/car.bmp").convert()
finish_surf = pygame.image.load("images/car/finish.png").convert_alpha() # изображение в формате PNG с альфа-каналом преобразуется методом convert_alpha(), а не convert()

# bg_surf_converted = bg_surf.convert() # можно и так, но неудобно

car_rect = car_surf.get_rect(center=(W//2, H//2))
car_surf.set_colorkey((255, 255, 255))

# По итогу мы привели пиксели 3-х изображений в формат пикселей поверхности sc
# И теперь прорисовка будет происходить быстрее
sc.blit(bg_surf, (0, 0))
sc.blit(car_surf, car_rect)
sc.blit(finish_surf, (0, 0))

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)