# Функция issubclass(). Наследование от встроенных типов и от object


# Иерархия:
#      object
#       /
#    Geom 
#    /
# Line 

class Geom: # Geom(object)
    pass

class Line(Geom):
    pass


print(Geom.__class__)   # <class 'type'>
print(Line.__class__)   # <class 'type'>
print(object.__class__) # <class 'type'>

print(type.__class__)   # <class 'type'>
# That's because type is its own type.
# The parent-child relationships of the Python type system must stop somewhere,
# and type is that point.

g = Geom()
print(g) # <__main__.Geom object at 0x000001DE2A397D60>

l = Line()

print("\n---функция issubclass()")
# мы можем определять, является ли тот или иной класс подклассом другого класса.
# Это делает функция issubclass()
print(issubclass(Line, Geom))
print(issubclass(Geom, Line))
# print(issubclass(l, Geom)) # TypeError: issubclass() arg 1 must be a class

print("\n---isinstance() - принадлежность объекта классу")
print(isinstance(l, Line))
print(isinstance(l, Geom))
print(isinstance(l, object))


print("\n---Наследование от встроенных типов данных")
# Интересный факт языка Python, что все стандартные типы данных являются классами
print(issubclass(int, object))  # True
print(issubclass(list, object)) # True


class Vector(list): # наследуем от класса list
    def __str__(self):
        return "|".join(map(str, self))
 
 
v = Vector([1, 2, 3])
print(v, type(v))
