import pygame
pygame.init() # функция init импортирует массу других важных расширений

pygame.display.set_mode((600, 400)) # создание игрового окна

# Main Loop - главный цикл обработки событий
# pygame.event - очередь событий (итерируемый объект)
# event - ссылка на текущее событие из очереди событий
# pygame.QUIT - нажатие на крестик в углу окна
# exit() - выход из приложения

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()