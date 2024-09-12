# Cоздадим пакет 'courses' из модулей по обучающим курсам:
# HTML
# Java

# Пакет в Python – это обычный каталог,
# в котором обязательно должен располагаться
# специальный файл __init__.py

# NB!
# Для корректной обработки модулей в пакете,
# все файлы следует создавать с кодировкой UTF-8

import courses

print( dir(courses) )
print("-----------------")
print(f"{courses.NAME = }")

print("---------------Абсолютный импорт----------------")
import courses.html
courses.html.get_html()

from courses.java import get_java
get_java()

print("--------------Относительный импорт----------------")
print("Смотри инициализатор пакетов __init__.py")
import courses as cr
cr.get_html_five()
