import pygame
pygame.init()
 
W, H = 600, 400
 
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Перемещение текста с помощью мыши")
# pygame.display.set_icon(pygame.image.load("app.bmp"))
 
clock = pygame.time.Clock()
FPS = 60
 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)
 
f = pygame.font.Font('fonts/YandexSDLight.ttf', 24)
sc_text = f.render('Привет мир!', 1, RED, YELLOW)
pos = sc_text.get_rect(center=(W//2, H//2))
 
def draw_text():
    sc.fill(WHITE)
    sc.blit(sc_text, pos)
    pygame.display.update()
 
draw_text()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()   # обнуляем последнее смещение мыши, которое случилось перед нажатием на кнопку
    
    # get_focused() возвращает True если курсор мыши находится в пределах клиентского окна
    # pos.collidepoint(pygame.mouse.get_pos()) если курсор мыши находится над текстом pos!!! то возвращается True
    if pygame.mouse.get_focused() and pos.collidepoint(pygame.mouse.get_pos()):
        btns = pygame.mouse.get_pressed()
        if btns[0]:     # нажата левая кнопка мыши
            rel = pygame.mouse.get_rel()    # получаем смещение
            pos.move_ip(rel) # перемещаем прямоугольник pos на текущее значение rel
            draw_text()
 
    clock.tick(FPS)