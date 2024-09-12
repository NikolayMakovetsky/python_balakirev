# В питоне помимо «стандартных» (standart) методов класса можно задавать
# - методы уровня класса (@classmethod)
# - статические методы (@staticmethod)


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    #  classmethod может работать только с атрибутами класса, но не объекта
    @classmethod
    def validate(cls, arg): # cls – ссылка на класс
        """ФУНКЦИЯ ПРОИЗВОДЯЩАЯ ПОЛЕЗНУЮ РАБОТУ ВНУТРИ КЛАССА"""
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    # staticmethod независимая самостоятельная функция, объявленная внутри класса
    # Она не имеет доступа ни к атрибутам класса, ни к атрибутам его экземпляров
    @staticmethod
    def norm2(x, y):
        """CЕРВИСНАЯ ФУНКЦИЯ, связанная с векторами,
        для вычисления квадратичной нормы любого радиус-вектора"""
        return x*x + y*y        

    def __init__(self, x, y): # self – ссылка на объект класса
        self.x = 0
        self.y = 0
        # if self.validate(x) and self.validate(y): # такая запись тоже отработает, т.к.
        # интерпретатор Python сам подставит нужный класс в параметр cls данного метода,
        # так как экземпляр содержит информацию о классе, от которого был образован
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y
 
    def get_coord(self): # standart method
        return self.x, self.y

print("\n---standart method")
# Обычные методы требуют создавать экземпляр класса!
v = Vector(3, 4)
print(f"{v.get_coord()}")
print(f"{Vector.get_coord(v)}")

print("\n---@classmethod")
print(f"{Vector.validate(5) = } [{Vector.MIN_COORD}, {Vector.MAX_COORD}]")

v = Vector(3, 4)
print(f"{v.x = }, {v.validate(v.x) = }")
v.validate(10)


print("\n---@staticmethod")
print(f"{Vector.norm2(5, 6) = }") # Использование функции без создания экземпляра

v = Vector(3, 4)
print(f"{v.norm2(v.x, v.y) = }")
Vector.norm2(Vector.MIN_COORD, 5)

print("\n---Обращение к @classmethod, @staticmethod при наследовании")
class MyClass(Vector):
    pass

m = MyClass(3, 4)
print(m.validate(5)) # @classmethod
print(m.norm2(2, 5)) # @staticmethod
