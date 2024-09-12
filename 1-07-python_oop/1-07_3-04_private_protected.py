# _attribute (с одним подчеркиванием) – режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах)
# __attribute (с двумя подчеркиваниями) – режим доступа private (служит для обращения только внутри класса)

# Давайте посмотрим, как ведут себя атрибуты
# с этими режимами доступа при наследовании !!!

print("\n---private")

class Geom:
    name = 'Geom'
 
    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)

 
class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill

    # # Здесь нет доступа к приватным атрибутам Geom
    # def get_coords(self):
    #     return (self.__x1, self.__y1, self.__x2, self.__y2)


r = Rect(0, 0, 10, 20)
print(r.__dict__)
print(r.get_coords())


print("\n---protected")

class Geom:
    name = 'Geom'
 
    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
 
 
class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    # Здесь доступны защищенные атрибуты Geom
    def get_coords(self):
        return (self._x1, self._y1, self._x2, self._y2)


r = Rect(0, 0, 10, 20)
print(r.__dict__)
print(r.get_coords())


# Нижнее подчеркивание лишь предупреждает (сигнализирует) программиста
# о защищенном атрибуте, к которому напрямую лучше не обращаться.


print("\n---Атрибуты private и protected на уровне класса")

class Geom:
    __name = 'Geom' # доступ будет закрыт всюду, кроме самого класса Geom
 
    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор {self.__name}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2


    def __verify_coord(self, coord):
        print(f"{coord} verified")
        return 0 <= coord <= 100

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        # super().__verify_coord(x1) # не сработает в дочернем классе
        self._fill = fill

r = Rect(0, 0, 10, 20)


# приватность запрещает переопределение методов в дочерних классах.
# Если же у метода прописать только одно подчеркивание,
# то его можно будет вызывать во всех дочерних классах.
