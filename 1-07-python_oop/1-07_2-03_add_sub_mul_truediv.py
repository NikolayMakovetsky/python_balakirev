# __add__()     – для операции сложения
# __sub__()     – для операции вычитания
# __mul__()     – для операции умножения
# __truediv__() – для операции деления



# Оператор    Метод оператора             Оператор    Метод оператора
# x + y       __add__(self, other)        x += y      __iadd__(self, other)
# x - y       __sub__(self, other)        x -= y      __isub__(self, other)
# x * y       __mul__(self, other)        x *= y      __imul__(self, other)
# x / y       __truediv__(self, other)    x /= y      __itruediv__(self, other)
# x // y      __floordiv__(self, other)   x //= y     __ifloordiv__(self, other)
# x % y       __mod__(self, other)        x %= y      __imod__(self, other)


class Clock:
    __DAY = 86400   # число секунд в одном дне
 
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY # 90000 % 86400 = 3600 (защита)


    def get_time(self):
        s = self.seconds % 60            # секунды
        m = (self.seconds // 60) % 60    # минуты
        h = (self.seconds // 3600) % 24  # часы
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"


    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")


    def __add__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError("Правый операнд должен быть типом int")
 
        return Clock(self.seconds + other)


    def __radd__(self, other):
        print("__radd__")
        return self + other


    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")
 
        sc = other if isinstance(other, int) else other.seconds
        self.seconds += sc
 
        return self




c1 = Clock(1000)
print(c1.get_time())

c1.seconds = c1.seconds + 100   # __add__
print(c1.get_time())

c1 = 100 + c1                   # __radd__
print(c1.get_time())

c2 = Clock(500)     
c2 += c1                        # __iadd__
print(c2.get_time())
