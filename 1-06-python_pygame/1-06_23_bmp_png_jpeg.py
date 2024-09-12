# bmp (Bitmap Picture) - родной формат изображений в pygame
# это несжатые наборы пикселей изображения
# такие графические файлы занимают много места по сравнению с другими графич форматами:
# PNG (расширение png)    | используется сжатие без потерь с использованием алгоритмов ДИКМ и LZW
# JPEG (расширение jpg)   | используется сжатие с потерями (алгоритм ДКП – аналог Фурье-преобразования с косинусными гармониками)

# PNG или JPEG?
# Для фотореалистичных изображений лучше всего использовать JPEG,
# т.к. незначительные потери практически не скажутся на визуальном восприятии,
# но изображение будет хорошо сжато.
# Для искусственных изображений с большим наличием однотонных областей
# (например, клип-арт) где четкость границ и однотонность заливки
# имеет первостепенное значение, лучше выбирать формат PNG.
# Кроме того, этот формат хранит альфа-канал для прозрачного фона
# (в JPEG такой возможности нет).


import pygame
pygame.init()

print(pygame.image.get_extended())
# True, значит на моем ПК pygame может использовать форматы PNG, JPEG и некоторые другие
# False, значит на моем ПК pygame может использовать только формат BMP
