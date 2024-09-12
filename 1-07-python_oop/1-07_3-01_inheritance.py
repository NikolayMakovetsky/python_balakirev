# Наследование

print("\n---Простейший пример наследования")

class Geom:
    name = 'Geom'

class Line:
    def draw(self):
        print("Рисование линии")


g = Geom()
print(g.name)

l = Line()
l.draw()


class Line(Geom): # Простейший пример наследования
    def draw(self):
        print("Рисование линии")

l = Line()
print(l.name) # Теперь у линии есть атрибут name


print("\n---Простейший пример наследования")
# Иерархия классов:
#   Geom
#   /   \
# Line Rect

class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def draw(self):
        print("Рисование примитива")


class Line(Geom):
    name = 'Line'

    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def draw(self):
        print("Рисование прямоугольника")

l = Line()
r = Rect()
l.set_coords(1, 1, 2, 2) # обращение к методу предка
r.set_coords(1, 1, 2, 2) # обращение к методу предка


g = Geom()
g.set_coords(0, 0, 0, 0)

print(l.name) # Line
print(r.name) # Geom, атрибут берется из предка т.к. в дочернем его нет

l.draw() # Рисование линии
r.draw() # Рисование прямоугольника
g.draw() # Рисование примитива

