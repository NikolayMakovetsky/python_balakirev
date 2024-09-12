# Работа со звуком
# pygame.mixer        | для работы со звуковыми эффектами
# pygame.mixer.music  | для добавления фоновой музыки | звуковые форматы: mp3, ogg, wav...

# Воспроизведение файла с помощью функции play(loops=0, start=0.0, fade_ms = 0)
# loops       | число повторений (0 – проигрывать один раз, 1 – два раза и т.д, -1 – бесконечное повторение)
# start       | начальное время проигрывания файла (в секундах)
# fade_ms     | затухание звука при окончании проигрывания (в мс)

# pygame.mixer.music.stop()       | остановить воспроизведение
# pygame.mixer.music.rewind()     | начать воспроизведение сначала

# set_volume(volume)  | установить уровень громкости (volume – вещественное значение от 0 до 1)
# get_volume()        | получить текущее значение уровня громкости

import pygame
pygame.init()
 
pygame.mixer.music.load("sounds/bird.mp3") # загрузка файла (пока без воспроизведения)
pygame.mixer.music.play(-1) # фоновая музыка (бесконечный цикл повторения)

W, H = 500, 300
sc = pygame.display.set_mode((W, H))
 
clock = pygame.time.Clock()
FPS = 60

flPause = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause # смена значения флага
                if flPause:
                    pygame.mixer.music.pause() # pause() – поставить воспроизведение на паузу
                else:
                    pygame.mixer.music.unpause() # unpause() – продолжить воспроизведения с места паузы        
 
    clock.tick(FPS)