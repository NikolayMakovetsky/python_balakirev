print("---------аннотация базовых типов----------")
cnt: int        # указываем int как ожидаемый тип
cnt = -5.3      # значение float хоть и будет присвоено, но интерпретатор подсветит
print(cnt)      # vs code по умолчанию не подсвечивает

# Аннотация типов носит информационный характер,
# на ход выполнения программы она никак не влияет.
# Активно аннотации стали внедряться, начиная с версии Python 3.5

# Зачем использовать аннтации:
# 1. Для удобства восприятия стороннего кода.
# 2. Для удобства редактирования кода, когда IDE «подсказывает» атрибуты
# указанного типа переменных.
# 3. Для отслеживания некоторых явных ошибок на уровне несоответствия типов.

print("---------аннотация типов в функциях----------")
print("----mul2")
def mul2(x: int):
    return x * 2

print(mul2("5"), type(mul2("5")))
print(mul2.__annotations__)

print("----mul3")
def mul3(x: float, y: int = 2) -> float:
    return x * y

print(mul3.__annotations__)

print("----show_x")
def show_x(x: float) -> None:
    print(f"x = {x}")

print(show_x.__annotations__)

print("--------list, tuple, set, dict-----------")
lst: list[int] = [1, 2, 3]
lst: list[int, str] = ['1', 2, 3]

book: tuple[str, str, int]
book = ('Фио', 'Название_книги', 2022)

elems: tuple[int, ...] # аннотация кортежа с произв числом элементов
elems = (1,)
elems = (1, 2)
elems = (1, 2, 3)

# для версий языка Python ниже 3.9 следует вместо tuple использовать тип Tuple
# from typing import List, Tuple, Dict, Set

persons: set[str] = {'Сергей', 'Михаил', 'Наталья'}

words: dict[str, int] = {'one': 1, 'two': 2}

print("--------Callable-----------")
#  тип Callable из модуля typing, который позволяет аннотировать вызываемые объекты
from typing import Callable

def even(x):
    return bool(x % 2 == 0)

def is_even(flt: Callable, lst: list) -> str:
    res = ""
    for _ in lst:
        res += str(flt(_))
    return res

print(is_even(even, [1, 2, 3, 4]))
print(is_even.__annotations__)