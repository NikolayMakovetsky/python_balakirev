# В стандартном поведении bool() возвращает
# True для непустых объектов
# и False – для пустых

bool(123)
bool(-1)
bool(0)
bool("python")
bool("")
bool([])


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(bool(p)) # True

# Мы можем переопределить ее поведение либо через магический метод __len__(),
# либо через метод __bool__():
# __len__() – вызывается функцией bool(), если не определен магический метод __bool__()
# __bool__() – вызывается в приоритетном порядке функцией bool()

print("\n---переопределим функцию __bool__()")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    # Если нет метода __bool__, то внутренним __bool__вызывается __len__
    # def __bool__(self):
    #     print("__bool__")
    #     return self.x == self.y

    # Если и __len__ не реализован, то всегда для объектов
    # пользовательского класса всегда будет возвращатся True
    # def __len__(self):
    #     print("__len__")
    #     return self.x * self.x + self.y * self.y


p = Point(0, 0)
p = Point(10, 20)

if p:
    print("объект p дает True")
else:
    print("объект p дает False")
