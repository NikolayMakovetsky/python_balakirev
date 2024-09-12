# Звуки с использованием модуля Mixer

# Как управлять звуками?
# =======================
# pygame.mixer:                   -> (методы mixer-a: play, stop, pause, unpause для всех дорожек)
#     channel 1: [Sound.play()]   -> (методы channel 1: play, stop, pause, unpause только для первой дорожки)
#     channel 2: [Sound.play()]   и так далее
#     channel 3: [Sound.play()]
#     ...
#     channel N: [Sound.play()]

# А как обратиться к конкретному каналу чтобы вызывать методы канала?
# ch = s.play()
# Когда вызывается метод s.play(), то он возвращает ссылку на канал в котором происходит воспроизведение
# ch.pause() - ПРИМЕР (постановка на паузу конкретного канала)
# pygame.mixer.pause() - ПРИМЕР (постановка на паузу всех каналом миксера)

import pygame

# эта строчка позволит избежать задержек при воспроизведении звуков
pygame.mixer.pre_init(44100, -16, 1, 512) # важно вызвать до pygame.init()

pygame.init()
 
pygame.mixer.music.load("sounds/bird.mp3")
pygame.mixer.music.play(-1) 

W, H = 500, 300
sc = pygame.display.set_mode((W, H))
 
clock = pygame.time.Clock()
FPS = 60

s = pygame.mixer.Sound("sounds/catch.ogg") # сохраняем ссылку на экземпляр класса Sound

flPause = False
vol = 1.0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause 
                if flPause:
                    pygame.mixer.music.pause() 
                else:
                    pygame.mixer.music.unpause()
            
            elif event.key == pygame.K_LEFT:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
                print( pygame.mixer.music.get_volume() )
            elif event.key == pygame.K_RIGHT:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
                print( pygame.mixer.music.get_volume() )
            elif event.key == pygame.K_RETURN:
                s.play() # при нажатии Enter воспроизводим файл


    clock.tick(FPS)