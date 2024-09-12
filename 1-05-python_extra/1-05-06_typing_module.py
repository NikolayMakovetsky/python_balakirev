print("--------Модуль typing и типы Union, Optional, Any, Final----------")

from typing import Union, Optional, Any, Final

print("-----Union----составной тип")
def mul2(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x * y

# Синтаксис с версии Python 3.10 
def mul2(x: int | float, y: int | float) -> Union[int, float]:
    return x * y

# Union фактически, определяет новый объект – новый тип данных.
Digit = Union[int, float]
def mul2(x: Digit, y: Digit) -> Digit:
    return x * y
print(Digit, type(Digit))

print("-----Optional---")
# тип Optional позволяет указать один какой-либо тип данных
# и еще автоматически добавляется тип None

Str = Optional[str] # StrType = Union[str, None]

# Этот случай выделили отдельно в тип Optional,
# т.к. такая комбинация с None довольно часто используется на практике

def show_x(x: float, descr: Optional[str] = None) -> None:
    if descr:
        print(f"{descr} {x}")
    else:
        print(f"x = {x}")

show_x(55.6768)
show_x(55.6768, "число = ")

print("-----Any---")
# Следующий тип Any означает буквально любой тип данных.
# Он используется, если параметр или переменная или возвращаемое значение функции
# может принимать любой тип

def show_x(x: Any, descr: Optional[str] = None) -> None:
    if descr:
        print(f"{descr} {x}")
    else:
        print(f"x = {x}")

print("-----Final---")
# последний тип Final появился в версии Python 3.10
# и служит для отметки констант в программе
MAX_VALUE: Final = 1000
# при попытке позже поменять это значение
# интегрированная среда нам подсветит эту переменную
MAX_VALUE = 2000

