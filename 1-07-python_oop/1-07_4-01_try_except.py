# Группы исключений:
# - исключения при компиляции (до исполнения кода)
# - исключения в момент исполнения

print("\n---FileNotFoundError")
try:
    file = open("myfile2.txt")
except FileNotFoundError:
    print("Невозможно открыть файл")


print("\n---ZeroDivisionError")
try:
    x, y = map(int, "5 0".split()) # "5 hi"
    res = x / y
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
except ValueError:
    print("Ошибка типа данных")

print("\n---Неудачный стиль обработки исключений")
# Блоков except может быть сколько угодно
# Чтобы отловить в блоке except сразу несколько типов исключений
# можно написать так:
# except (ZeroDivisionError, ValueError):
#     res = "деление на ноль или нечисловое значение"

print("\n---Взаимодействие с объектами классов исключений")
try:
    x, y = map(int, "5 0".split()) # "5 hi"
    res = x / y
except ZeroDivisionError as z:
    print(z, type(z))
except ValueError as z:
    print(z, type(z))

print("\n---Иерархия классов исключений")
# Exception – общий для классов ArithmeticError и ValueError
# Блоком exception отлавливаются все типовые исключения
# В нашем примере блок ZeroDivisionError никогда выполнен не будет
# Поэтому здесь есть одно простое правило.
# Сначала прописываются блоки со специализированными классами исключений,
# а затем с более общими (базовыми)

try:
    x, y = map(int, "5 0".split())
    res = x / y
except Exception:
    print("Какая-то ошибка") # Какая-то ошибка
except ZeroDivisionError:
    print("Ошибка типа данных") 

print("\n---Блок except без каких-либо классов")
try:
    x, y = map(int, "5 0".split())
    res = x / y
except:
    print("Ошибка")


print("""\n---СПРАВОЧНИК ИСКЛЮЧЕНИЙ
BaseException
 +-- BaseExceptionGroup
 +-- GeneratorExit
 +-- KeyboardInterrupt
 +-- SystemExit
 +-- Exception
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ExceptionGroup [BaseExceptionGroup]
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- StopAsyncIteration
      +-- StopIteration
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- BytesWarning
           +-- DeprecationWarning
           +-- EncodingWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- PendingDeprecationWarning
           +-- ResourceWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UnicodeWarning
           +-- UserWarning
""")