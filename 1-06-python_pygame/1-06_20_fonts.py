# pygame.font - модуль работы со шрифтами
# SysFont(fontname, size) | класс для выбора предустановленного (существующего на устройстве) шрифта (по имени fontname) с размером size (в пикселях)
# Font(path, size)        | класс для загрузки шрифта (несуществующего на устройстве) по указанному пути path с размером size (в пикселях)
# get_fonts()             | функция, возвращающая имена предустановленных в системе шрифтов
# match_font(fontname)    | функция возвращающая путь к предустановленному шрифту по его имени

import pygame
pygame.init()
print( pygame.font.get_fonts() ) # ['arial', 'arialblack', ... , 'extra', 'teamviewer15']

f_sys = pygame.font.SysFont('arial', 12) # класс SysFont возвращает объект Font, с которым мы уже можем работать


# f = pygame.font.Font('fonts/YandexSDLight.ttf', 24) # добавление собственного шрифта

