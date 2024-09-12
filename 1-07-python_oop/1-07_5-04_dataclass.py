# Как сократить писанину при создании классов?

print("\n---Стандартное объявление класса")

class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"Thing: {self.__dict__}"

t = Thing("Учебник по Python", 100, 1024)
print(t)

print("\n---Объявление класса с использованием декоратора @dataclass")
from pprint import pprint
from dataclasses import dataclass, field

# ThingData эквивалентен ранее объявленному классу Thing
@dataclass
class ThingData:
    name: str
    weight: int
    price: float


pprint(ThingData.__dict__)
# Видим, что __dict__ ссылается на объект типа mappingproxy,
# внутри которого имеется инициализатор __init__() и магический метод __repr__()
# а также __eq__()

print("\n---------")
td = ThingData("Учебник по Python", 100, 1024)
print(td)
print(repr(td))

td_2 = ThingData("Python ООП", 80, 512)
print(td == td_2) # False

td_3 = ThingData("Python ООП", 80, 512)
print(td_2 == td_3) # True

print("\n---Сделаем свой вариант метода __eq__")

@dataclass
class ThingData:
    name: str
    weight: int
    price: float
 
    def __eq__(self, other):
        """Cравнeние объектов только по весу"""
        return self.weight == other.weight

td_2 = ThingData("Python ООП", 80, 640)
td_3 = ThingData("Python ООП 2", 80, 512)
print(td_2 == td_3) # True т.к. веса равны, и этого нам достаточно



print("\n---Атрибуты с начальными значениями, Атрибут-список")
# Но здесь есть один маленький нюанс:
# все атрибуты со значениями по умолчанию должны идти последними!!!
# Так как эти атрибуты, по сути, являются параметрами метода __init__()
# и идут в том порядке, в котором записаны в классе

# Также при объявлении Data Classes атрибутам нельзя присваивать
# изменяемые объекты в качестве значений по умолчанию
# Иначе может возникнуть ошибка при которой разные экземпляры
# будут ссылаться например на один и тот же изменяемый список

@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    # функция field() позволяет сделать список атрибутом
    dims: list = field(default_factory=list)

td = ThingData("Учебник по Python", 100)
print(td)

td = ThingData("Учебник по Python", 100, 512)


# Вообще с помощью функции field() можно довольно тонко
# настраивать поведение атрибутов в Data Classes,
# но об этом и других вещах мы продолжим говорить на следующем занятии

