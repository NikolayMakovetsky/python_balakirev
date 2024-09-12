# __str__()  – магический метод для отображения информации об объекте класса
#              для пользователей (например, для функций print, str)
# __repr__() – магический метод для отображения информации об объекте класса
#              в режиме отладки (для разработчиков)

print("\n---str, repr")

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"

cat = Cat('Васька')

print(cat)
print(repr(cat))


print("\n---len, abs")

# __len__() – позволяет применять функцию len() к экземплярам класса
# __abs__() - позволяет применять функцию abs() к экземплярам класса


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list( map(abs, self.__coords) )


p = Point(1, -2)
print(len(p))
print(abs(p))
