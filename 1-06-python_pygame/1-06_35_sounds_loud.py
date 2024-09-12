# Работа со звуком

# set_volume(volume)  | установить уровень громкости (volume – вещественное значение от 0 до 1)
# get_volume()        | получить текущее значение уровня громкости

import pygame
pygame.init()
 
pygame.mixer.music.load("sounds/bird.mp3")
pygame.mixer.music.play(-1) 

W, H = 500, 300
sc = pygame.display.set_mode((W, H))
 
clock = pygame.time.Clock()
FPS = 60

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

    clock.tick(FPS)