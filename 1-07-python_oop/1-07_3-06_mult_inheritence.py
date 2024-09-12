# Множественное наследование 


# Делаем интернет-магазин по продаже товаров:
#   ноутбуков
#   дисков
#   процессоров и т.п.

# Каждый товар будет определяться своим классом,
# а общим (базовым) для них всех будет класс Goods – товары. 

# Также у каждого товара обязательно будут поля:
#   name – наименование
#   weight – вес
#   price – цена

print("\n---Прямое наследование")

class Goods:
    def __init__(self, name, weight, price):
        print("init MixinLog")
        self.name = name
        self.weight = weight
        self.price = price
 
    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class NoteBook(Goods):
    pass

n = NoteBook("Acer", 1.5, 30000)

n.print_info()


# Но потом, к нам подходит тимлид и говорит:
# - Дорогой сеньор, добавь, пожалуйста, возможность логирования товаров магазина.

# Плохой сеньор начнет прописывать логику логирования
# либо непосредственно в базовом классе Goods,
# либо уровнем выше (в иерархии наследования).
# А хороший воспользуется идеей МИКСИНОВ!

# Этот класс работает совершенно независимо от классов Goods и Notebook
# и лишь добавляет функционал по логированию товаров с использованием их id.
# Такие независимые базовые классы и получили название миксинов – примесей

print("\n---Множественное наследование (класс-Миксин)")

# Иерархия:
#    object
#   /       \
# Goods MixinLog
#   \       /
#   NoteBook

# При создании объектов инициализатор ищется сначала в дочернем классе,
# но так как его там нет, то в первом базовом Goods.
# Он там есть, выполняется и на этом инициализация нашего объекта NoteBook
# завершается.
# Однако, нам нужно также взывать инициализатор
# и второго базового класса MixinLog.
# В данном случае, сделать это можно с помощью объекта-посредника super(),
# которая и делегирует вызов метода __init__ класса MixinLog


class Goods:
    def __init__(self, name, weight, price):
        super().__init__() # вызываем __init__ MixinLog КАК ТАК???
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price
 
    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар продан в 00:00 часов")


# Первый базовый класс, указанный при наследовании,
# выбирается первым (после дочернего, разумеется).
# И это важный момент.
# Вы всегда можете быть уверены, что инициализатор первого базового класса
# сработает в первую очередь.
class NoteBook(Goods, MixinLog):
    pass


n = NoteBook("Dell", 1.9, 44000)
n.print_info()
n.save_sell_log()


print("\n---MRO - порядок обхода классов")
print(NoteBook.__mro__)


print("\n---MixinLog_2")

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()  # вызываем __init__ (MixinLog) 
                            # (делегированный вызов инициализатора
                            # следующего по списку MRO базового класса)
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price
 
    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар продан в 00:00 часов")


class MixinLog2:
    # def __init__(self, p1, p2): # ДОП ПАРАМЕТРЫ СЮДА ЛУЧШЕ НЕ ПИСАТЬ
    def __init__(self):
        super().__init__()  # вызываем __init__ (MixinLog) 
                            # (делегированный вызов инициализатора
                            # следующего по списку MRO базового класса)
        print("init MixinLog 2")


class NoteBook(Goods, MixinLog2, MixinLog):
    pass

print(NoteBook.__mro__)
n = NoteBook("Acer", 1.4, 25000)
n.print_info()
n.save_sell_log()

# Чтобы в программах при множественном наследовании не возникало проблем
# с зависимостью последовательности наследования дополнительных базовых классов,
# их инициализаторы следует создавать с одним параметром self
# и в каждом из них прописывать делегированный вызов инициализатора
# следующего класса командой: super().__init__() БЕЗ ДОП ПАРАМЕТРОВ !!!
# Т.Е. ЕСЛИ ПОРЯДОК НАСЛЕДОВАНИЯ ПОЗЖЕ ПОМЕНЯЕТСЯ, ТО КОД ПЕРЕСТАНЕТ РАБОТАТЬ
