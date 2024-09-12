# dunder-методы (от англ. сокращения double underscore) т.е. 'двойное подчеркивание'

print("\n---Обычный класс")

class Counter:
    def __init__(self):
        self.__counter = 0

c = Counter() # класс можно вызывать подобно функции
              # благодаря встроенной для него реализации магического метода __call__

print("\n---Класс с реализацией метода __call__")
# Классы, экземпляры которых можно вызывать подобно функциям,
# получили название ФУНКТОРЫ

class Counter:
    def __init__(self):
        self.__counter = 0
 
    def __call__(self, *args, **kwargs):
        print("__call__")
        self.__counter += 1
        return self.__counter

c = Counter()
res = c()   # c.__call__()
print(res)  # 1
res = c()
res = c()
print(res)  # 3

c2 = Counter()
res2 = c2()
print(res2) # 1 (счетчики работают независимо)


print("\n---Усовершенствуем наш класс-счетчик")


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        self.__counter += step
        return self.__counter

c3 = Counter()
res3 = c3(step = 5)
res3 = c3(step = 6)
print(res3) # 5+6=11

print("\n---Использование класса с методом __call__ вместо замыканий функций")

class StripChars:
    """Класс для удаления в начале и в конце строки заданных символов"""
    def __init__(self, chars):
        self.__chars = chars
 
    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Аргумент должен быть строкой")
 
        return args[0].strip(self.__chars)


s1 = StripChars("?:!.; ")
res = s1(" Hello World! ")
print(res)


print("\n---Класс-декоратор с методом __call__")
import math


class Derivate:
    """Вычисление производной функции в определенной точке"""
    def __init__(self, func):
        self.__fn = func
 
    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


def f_sin(x):
    return math.sin(x)


print(f_sin(math.pi/4))

df_sin = Derivate(f_sin)
print(df_sin(math.pi/4))

