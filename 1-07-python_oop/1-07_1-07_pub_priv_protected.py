# Основа механизма инкапсуляции - ограничение доступа к данным и методам класса извне

# attribute (без подчеркиваний вначале) – публичное свойство (public)

# _attribute (с одним подчеркиванием) – режим доступа protected
#             (служит для обращения внутри класса и во всех его дочерних классах)

# __attribute (с двумя подчеркиваниями) – режим доступа private
#             (служит для обращения только внутри класса)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

print("\n---public")
pt = Point(1, 2)
print(pt.x, pt.y)
pt.x = 200
pt.y = "coord_y"
print(pt.x, pt.y)


print("\n---protected")
# Хотя ошибок нет, и доступ к атрибутам все-таки возможен, нужно знать, что
# нижнее подчеркивание лишь предостерегает программиста
# от использования этого свойства вне класса.
# (Впоследствии это может стать причиной непредвиденных ошибок)
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

pt = Point(1, 2)
print(pt._x, pt._y)
pt._x = 200
pt._y = "coord_y"
print(pt._x, pt._y)


print("\n---private")

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y): # setter
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_сoord(self): # getter
        return self.__x, self.__y

pt = Point(1, 2)
# print(pt.__x, pt.__y) # AttributeError: 'Point' object has no attribute '__x'
pt.__x = 200            # Ошибки нет, но значения не присвоены
pt.__y = "coord_y"      # Ошибки нет, но значения не присвоены
print(pt.get_сoord())   # (1, 2)
# print(pt.__x, pt.__y) # AttributeError: 'Point' object has no attribute '__x'

# pt.set_coord(200, "coord_y")    # ValueError: Координаты должны быть числами
pt.set_coord(200, 300)
print(pt.get_сoord())   # (200, 300)


print("\n---Добавим приватный метод уровня класса")

class Point:

    @classmethod
    def __check_value (cls, x): #
        """Проверка корректности координат"""
        return type(x) in (int, float)

    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        if self.__check_value (x) and self.__check_value (y): #
            self.__x = x
            self.__y = y

    def set_coord(self, x, y):
        if self.__check_value (x) and self.__check_value (y): #
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_сoord(self):
        return self.__x, self.__y


pt = Point(7, 8)
print(pt.get_сoord())   # (7, 8)
pt.set_coord(134, 222)
print(pt.get_сoord())   # (134, 222)

print("\n---Как обратиться к приватным атрибутам извне?")

print(dir(Point)) # ['_Point__check_value',...
print(dir(pt)) # ['_Point__check_value', '_Point__x', '_Point__y',...

print(f"{pt._Point__x = }") # 134
print(f"{pt._Point__y = }") # 222

# Однако, так делать крайне не рекомендуется и двойное подчеркивание
# должно сигнализировать программисту,
# что работать с такими атрибутами
# нужно только через разрешенные интерфейсные методы

print("\n---Максимальная защита класса (pip install accessify)")
# # pip install accessify

# # from accessify import private, protected

# @private # @protected
# @classmethod
# def check_value(cls, x):
#     return type(x) in (int, float)

# pt.check_value(5)

# # Все, теперь мы можем обратиться к check_value только внутри класса