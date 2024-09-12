import pygame
pygame.init()
 
W, H = 600, 400
 
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Шрифты")
# pygame.display.set_icon(pygame.image.load("app.bmp")) # подходящую иконку не нашел
 
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

# метод render формирует поверхность на которой пишется текст
f = pygame.font.Font('fonts/YandexSDLight.ttf', 24) # загружаем наш собственный шрифт
# f = pygame.font.Font(None, 48)        # pygame шрифт по умолчанию
# f = pygame.font.SysFont(None, 48)     # pygame шрифт по умолчанию
sc_text = f.render('Привет мир!', 1, RED, YELLOW) # 1 означает сглаженный текст; 0 несглаженный
pos = sc_text.get_rect(center=(W//2, H//2))
 
sc.fill(WHITE)
sc.blit(sc_text, pos)
pygame.display.update()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    clock.tick(FPS)