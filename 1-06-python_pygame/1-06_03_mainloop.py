import pygame
pygame.init()

pygame.display.set_mode((600, 400), pygame.RESIZABLE)
# pygame.display.set_mode((600, 400), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN) # применение сразу нескольких констант
pygame.display.set_caption("Каркас приложения")
# pygame.display.set_icon(pygame.image.load("app.bmp"))
# формат bmp в отличие от ico родной для pygame,
# его можно использовать в любом месте программы

# Main Loop - главный цикл обработки событий
# Недостаток простой записи цикла событий в том, что он будет крутиться очень быстро
# А события не могут так быстро генерироваться
# Для анимации вполне достаточно 60 кадров в секунду!
# Задержка и формирование нужного FPS(от англ. frame per second) 'Кадровая частота':
# Для динамических игр 1/60 сек = 17 миллисекунд
# Для статических игр 1/30 сек = 34 миллисекунд

clock = pygame.time.Clock()
FPS = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS) # устанавливаем 30 итераций цикла за 1 секунду
                    # причем метод tick учитавает и время работы самих обработчиков событий!
        

# Стили отображения игрового окна:
# pygame.FULLSCREEN   | полноэкранный режим
# pygame.DOUBLEBUF    | двойная буферизация (рекомендуется при совместном использовании HWSURFACE или OPENGL)
# pygame.HWSURFACE    | аппаратное ускорение отрисовки (только для режима FULLSCREEN)
# pygame.OPENGL       | обоработка отображений с помощью библиотеки OpenGL
# pygame.RESIZABLE    | окно с изменяемыми размерами
# pygame.NOFRAME      | окно без рамки и заголовка
# pygame.SCALED       | разрешение, зависящее от размеров рабочего стола
