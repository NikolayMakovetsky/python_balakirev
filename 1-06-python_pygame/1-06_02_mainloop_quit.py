import pygame
pygame.init() # функция init импортирует массу других важных расширений

pygame.display.set_mode((600, 400)) # создание игрового окна

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False

print("---\nПрограмма продолжает работу даже после закрытия игрового окна!\n---")
            