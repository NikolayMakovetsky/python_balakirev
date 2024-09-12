print("\n---try-except else")

try:
    x, y = map(int, "6 2".split())
    res = x / y
except ZeroDivisionError as z:
    print(z)
except ValueError as z:
    print(z) 
else: # выполнится только в случае если блок try-except выполнится без ошибок
    print("Исключений не произошло")

try:
    x, y = map(int, "5 0".split())
    res = x / y
except ZeroDivisionError as z:
    print(z)
except ValueError as z:
    print(z) 
else: # выполнится только в случае если блок try-except выполнится без ошибок
    print("Исключений не произошло")


print("\n---try-except finally")


try:
    x, y = map(int, "6 2".split())
    res = x / y
except ZeroDivisionError as z:
    print(z)
except ValueError as z:
    print(z) 
else: # выполнится только в случае если блок try-except выполнится без ошибок
    print("Исключений не произошло")
finally:
    print("Блок finally выполняется всегда")

print("\n---Используем finally для закрытия файла")
f = 0
try:
    f = open("myfile.txt")
    f.write("hello")
except FileNotFoundError as z:
    print(z)
except:
    print("Другая ошибка")
finally:
    if f:
        f.close()
        print("Файл закрыт")
    else:
        print("Файл не открывался")

print("\n---Файловый мендежер позволяет сократить код")
try:
    with open("myfile.txt") as f:
        f.write("hello")
except FileNotFoundError as z:
    print(z)
except:
    print("Другая ошибка")

print("\n---finally для обработки исключений внутри функций")

def get_values(vls: str) -> tuple:
    try:
        x, y = map(int, vls.split())
        return x, y
    except ValueError as v:
        print(v)
        return 0, 0
    finally:
        print("finally выполняется до return")
 
print("---")
tup = get_values("5 hi")
print(type(tup), *tup)

print("---")
tup = get_values("5 6")
print(type(tup), *tup)

print("\n---Вложенные блоки try / except")

try:
    x, y = map(int, "5 0".split())
    try:
        res = x / y
    except ZeroDivisionError:
        print("Деление на ноль") #
except ValueError as z:
    print("Ошибка ValueError")

try:
    x, y = map(int, "5 hi".split())
    try:
        res = x / y
    except ZeroDivisionError:
        print("Деление на ноль")
except ValueError as z:
    print("Ошибка ValueError") #

print("\n---Выносим внутренний блок try / except в функцию")


def div(a, b) -> str | float: # неудачная практика
    try:
        return a / b
    except ZeroDivisionError:
        return "Деление на ноль"

print(div(5, 2))
print(div(5, 0))
