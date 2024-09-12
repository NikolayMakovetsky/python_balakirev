# Как работает __slots__ с property и при наследовании



class Point2D:
    # '__length' с двумя подчеркиваниями - приватный атрибут/метод
    __slots__ = ('x', 'y', '__length') # slot = щель
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (x*x + y*y) ** 0.5

    @property
    def length(self): # используем length без __ и все работает
        return self.__length
 
    @length.setter
    def length(self, value): # используем length без __ и все работает
        self.__length = value


pt = Point2D(1, 2)
print(pt.length) # 2.23606797749979
pt.length = 3.66
print(pt.length) # 3.66

# Смотрите, мы здесь обращаемся к свойству length,
# хотя в __slots__ нет такого разрешенного имени.
# И при этом нет никаких ошибок выполнения.
# В принципе, так и должно быть,
# потому что length – это не локальная переменная экземпляра класса,
# а атрибут класса Point2D.
# Коллекция __slots__ не накладывает ограничения на атрибуты класса,
# только на локальные атрибуты его экземпляров.
# Благодаря этому и появляется свойство length,
# которое работает как геттер и сеттер класса Point2D.


print("\n---Поведение __slots__ при наследовании классов")


class Point2D:
    __slots__ = ('x', 'y', '__length')
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (x*x + y*y) ** 0.5

    @property
    def length(self):
        return self.__length
 
    @length.setter
    def length(self, value):
        self.__length = value


class Point3D(Point2D):
    pass


# Для экземпляров этого класса будет разрешено создание локальных свойств,
# несмотря на то, что в базовом классе присутствует коллекция __slots__:


pt3 = Point3D(10, 20)
pt3.z = 30
print(pt3.__dict__) # __dict__ Работает т.к. в дочернем классе нет __slots__


print("\n---Добавление __slots__ в дочерний класс")


class Point2D:
    __slots__ = ('x', 'y', '__length')
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (x*x + y*y) ** 0.5

    @property
    def length(self):
        return self.__length
 
    @length.setter
    def length(self, value):
        self.__length = value


class Point3D(Point2D):
    __slots__ = ('z') # добавили z

    # Так ограничения сразу вступят в свои права
    # и __slots__ будет как бы унаследована от базового класса Point2D.
    # То есть, в классе Point3D сейчас доступны только локальныe атрибуты x и y,
    # а мы еще добавляем z

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


pt3 = Point3D(10, 20, 30)
print(pt3.length) # 22.360679774997898 (функция работает)

# Теперь, наш дочерний класс содержит уникальный код,
# расширяющий функционал базового класса без каких-либо повторений.
# При этом, в обоих классах используется ограничение,
# но с разным набором локальных свойств

