import pygame
from random import randint

# ===========================ball.py==============================

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.score = score
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 20: 
            self.rect.y += self.speed
        else:
            self.kill()

# ==============================================================

pygame.mixer.pre_init(44100, -16, 1, 512) # важно прописать до pygame.init()
pygame.init()

# Воспроизведение фоновой музыки
pygame.mixer.music.load('sounds/bird.mp3')
pygame.mixer.music.play(-1)

# Звук ловли шаров
s_catch = pygame.mixer.Sound('sounds/catch.ogg')

pygame.time.set_timer(pygame.USEREVENT, 2000)

f = pygame.font.SysFont('arial', 30) 

W, H = 1000, 570
sc = pygame.display.set_mode((W, H))
 
clock = pygame.time.Clock()
FPS = 60
game_score = 0

bg = pygame.image.load('images/flowballs/back1.jpg').convert()
score = pygame.image.load('images/flowballs/score_fon.png').convert_alpha()
telega = pygame.image.load('images/flowballs/telega.png').convert_alpha()
t_rect = telega.get_rect(centerx=W//2, bottom=H-5)


balls_data = ({'path': 'ball_bear.png', 'score': 100},
              {'path': 'ball_fox.png', 'score': 150},
              {'path': 'ball_panda.png', 'score': 200})
balls_surf = [pygame.image.load('images/flowballs/'+data['path']).convert_alpha() for data in balls_data]
balls = pygame.sprite.Group()


def createBall(group):
    """Создание шара со случайными параметрами"""
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1, 4)
    
    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)


def collideBalls():
    """Проверка на столкновение телеги и шара"""
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            s_catch.play() # воспроизведение звука при поимке шара
            game_score += ball.score
            ball.kill()


tlg_speed = 10 
createBall(balls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)  

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        t_rect.x -= tlg_speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += tlg_speed
        if t_rect.x > W-t_rect.width:
            t_rect.x = W-t_rect.width

    # Проверка на наличие столкновений + удаление столкнувшихся с телегой шаров
    collideBalls()

    # Отрисовка объектов
    sc.blit(bg, (0, 0)) # фон
    balls.draw(sc)
    sc.blit(score, (0, 0)) # счет
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10)) # вывод чисел
    sc.blit(telega, t_rect) # телега
    pygame.display.update()

    # реализация падения всех шаров группы
    balls.update(H)
     
    clock.tick(FPS)        
 
