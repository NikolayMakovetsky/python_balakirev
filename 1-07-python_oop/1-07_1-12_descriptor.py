# DESCRIPTOR = ОПИСАТЕЛЬ
# Класс для представления точек в трехмерном пространстве

# _attribute (с одним подчеркиванием) – режим доступа protected
#            (служит для обращения внутри класса и во всех его дочерних классах)

print("\n---Класс без дескриптора")

class Point3D:
    def __init__(self, x, y, z):
        # Верификация и protected атрибуты _x, _y, _z скрыты в сеттерах
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    @property
    def x(self):
        return self._x
 
    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord
 
    @property
    def y(self):
        return self._y
 
    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord
 
    @property
    def z(self):
        return self._z
 
    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord


p = Point3D(1, 2, 3)
print(p.__dict__)
print(f"{p.x = }")
print(f"{p._x = }")


# В нашем классе Point3D получилось своеобразное дублирование:
# мы три раза прописывали свойства, фактически, с одинаковым функционалом.
# Как можно все это оптимизировать?
 

print("\n---Что такое дескриптор?")
# Дескриптор - это класс, который содержит или один магический метод __get__:

print("\n---non-data descriptor")
# class A называется non-data descriptor (дескриптор не данных)
# class A:
#     def __get__(self, instance, owner): 
#         return ...

print("\n---data descriptor")
# Или класс, в котором дополнительно прописаны методы __set__ и/или __del__:

# class B называется data descriptor (дескриптор данных)
# class B:
#     def __get__(self, instance, owner):
#         return ...
 
#     def __set__(self, instance, value):
#         ...
 
#     def __del__(self):
#         ...

print("\n---Класс с дескриптором")

class Integer: # имя определили сами
    """Дескриптор данных"""
    # В этом методе мы формируем локальное свойство с именем атрибута,
    # добавляя перед ним одно нижнее подчеркивание
    # (так принято делать при определении дескрипторов)
    # self  - ссылка на создаваемый экземпляр класса
    # owner – ссылка на класс Point3D
    # name  – имя атрибута (для первого объекта x, затем, y и z)
    def __set_name__(self, owner, name): # (аналог __init__)
        print("Execute set name method")
        self.name = "_" + name

    # self     – это ссылка на объект Integer
    # instance – ссылка на экземпляр класса pt
    # owner    – ссылка на класс Point3D
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
 
    # self     – ссылка на объект дескриптора
    # instance – ссылка на объект pt, из которого произошло обращение к дескриптору
    # value    – присваиваемое значение
    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        instance.__dict__[self.name] = value


class Point3D:
    # атрибуты и есть дескрипторы данных, через которые будет проходить взаимодействие
    x = Integer() #  __set_name__ (генерация сеттера, используя Integer)
    y = Integer() #  __set_name__
    z = Integer() #  __set_name__

    def __init__(self, x, y, z):
        print("Before set x:")        
        self.x = x # Integer.__dict__(_x) = value (x)
        print("After set x:")        
        self.y = y
        self.z = z

pt = Point3D(1, 2, 3) # __set__, __set__, __set__
pt.x = 56
print(pt.x, pt._x)
print(pt.__dict__)


# Теперь, сколько бы интерфейсов взаимодействия нам не понадобилось,
# мы легко их можем добавить в наш класс и все будет выглядеть понятно и компактно.

print("\n---Верификация в дексрипторе")

class Integer:
    """Дескриптор данных"""
    @classmethod
    def verify_coord(cls, coord): #
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")
 
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) # убрали __dict__, добавили getattr
 
    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value) # убрали __dict__, добавили setattr
        # так будет правильнее, с точки зрения Python,
        # нежели обращение напрямую к специальной коллекции __dict__


class Point3D:
    # атрибуты и есть дескрипторы данных, через которые будет проходить взаимодействие
    x = Integer() #  __set_name__
    y = Integer() #  __set_name__
    z = Integer() #  __set_name__
 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# pt = Point3D('1', 2, 3) # TypeError: Координата должна быть целым числом
pt = Point3D(7, 8, 9)
print(pt.__dict__)


# В итоге, мы с вами определили дескриптор данных (data descriptor)
# и на его основе создали три объекта x, y, z
# для интерфейса взаимодействия с координатами точки объектов класса Point3D

print("\n---ОТЛИЧИЕ ДЕСКРИПТОРОВ non-data/data descriptor")

# Дескрипторы не данных:
# 1. Не могут менять значения какого-либо свойства,
# так как не имеют сеттера и делитера.
# Они служат только для считывания информации.

# 2. Они имеют тот же приоритет доступа, что и обычные атрибуты класса !!!
# Рассмотрим пример:

class ReadIntX:
    """Дескриптор не данных
    Для считывания локального свойства _x"""
    def __set_name__(self, owner, name):
        self.name = "_x"
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class Point3D:
    xr = ReadIntX()
    x = Integer()
    y = Integer()
    z = Integer()
 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

pt = Point3D(4, 5, 6)

print(pt.xr, pt.__dict__) # считался атрибут х класса Point3D
pt.xr = 99
print(pt.xr, pt.__dict__) # считался атрибут хr экземпляра pt

# Это, как раз и говорит о том, что приоритет доступа к локальным свойствам объекта
# и к дескриптору не-данных одинаков.


print("\n---Создание data descriptor из non-data")

class ReadIntX:
    """Дескриптор не данных
    Для считывания локального свойства _x"""
    def __set_name__(self, owner, name):
        self.name = "_x"
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value): # добавили
        setattr(instance, self.name, value)

class Point3D:
    xr = ReadIntX()
    x = Integer()
    y = Integer()
    z = Integer()
 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt = Point3D(10, 11, 12)

pt.__dict__['xr'] = 77
print(pt.xr, pt.__dict__) # pt.xr вернул 10, а не 77
