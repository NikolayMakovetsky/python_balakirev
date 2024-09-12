class Point:
    MAX_COORD = 100
    MIN_COORD = 0
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def set_coord(self, x, y):
        self.x = x
        self.y = y
    
    # # Логическая ошибка, т.к. 
    # # когда мы через self (ссылку на объект) записываем имя атрибута
    # # и присваиваем ему какое-либо значение,
    # # то оператор присваивания создает этот атрибут в локальной области видимости,
    # # то есть, в самом объекте
    # def set_bound(self, left):
    #     self.MIN_COORD = left

    # А вот так правильно
    @classmethod
    def set_bound(cls, left):
        """Установка левой границы диапазона"""
        cls.MIN_COORD = left

pt1 = Point(1, 2)
pt2 = Point(10, 20)

print("\n---Атрибуты и методы класса – общие данные для всех его экземпляровЭ")
# Атрибуты и методы (MAX_COORD, MIN_COORD, __init__, set_coord)
# остаются в пространстве имен класса, а не копируются в экземпляры.
# Но из экземпляров мы можем совершенно спокойно к ним обращаться,
# так как пространство имен объектов содержит ссылку на внешнее ПИ класса.
# Если какой-либо атрибут не существует в экземпляре,
# то поиск переходит во внешнее пространство, то есть, в класс
# и поиск продолжается там. 

print("\n---Магические методы для работы с атрибутами")

# __getattribute__(self, item)     # автоматически вызывается
#                                  # при получении свойства класса с именем item

# __setattr__(self, key, value)    # автоматически вызывается
#                                  # при изменении свойства key класса

# __getattr__(self, item)          # автоматически вызывается
#                                  # при получении несуществующего свойства item класса

# __delattr__(self, item)          # автоматически вызывается
#                                  # при удалении свойства item
#                                  # (не важно: существует оно или нет)


class Point:
    MAX_COORD = 100
    MIN_COORD = 0
 
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
 
    def __getattribute__(self, item):
        if item == "_Point__x":
            raise ValueError("Private attribute")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("Недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)
            # self.__x = value неверный код, т.к.
            # в этом случае метод __setattr__ начнет выполняться по рекурсии,
            # пока не возникнет ошибка достижения максимальной глубины рекурсии.
            # Если нужно сделать что-то подобное, то используйте коллекцию __dict__:
            # self.__dict__[key] = value

    def __getattr__(self, item):
        print("__getattr__: " + item)

    def __delattr__(self, item):
        print("__delattr__: "+item)
        object.__delattr__(self, item)

print("\n---__getattribute__")
pt = Point(3, 2) # в момент создания экземпляров класса в инициализаторе __init__
                 # создаются локальные свойства __x и __y (__setattr__ работает)
print(f"{pt.MIN_COORD = }")
# print(pt._Point__x) # ValueError: Private attribute


print("\n---__setattr__")
pt = Point(3, 2)
# pt.z = 5 # AttributeError: Недопустимое имя атрибута

print("\n---__getattr__")
print(pt.a)         # __getattr__: a; None
print(pt.MAX_COORD) # 100 (отработал __getattribute__)

print("\n---__delattr__")
pt.a = 10
del pt.a # __delattr__: a