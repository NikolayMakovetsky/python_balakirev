# Все в Python – это объекты, даже классы.
# Да, классы – это объекты, которые позволяют создавать другие
# объекты с конкретным содержимым.
# А раз классы – это объекты, то должно быть нечто, что создает и их.
# И это нечто в Python называется метаклассом.
# Причем, метакласс – это тоже объект (в Python все объекты).
# Но это объект особого рода, который нельзя динамически порождать
# каким-нибудь другим мета-метаклассом.
# Он является вершиной, отправной точкой для создания обычных классов и,
# как следствие, их объектов.

print(type(int))    # <class 'type'>
print(type(bool))   # <class 'type'>

class A: pass
print(type(A))      # <class 'type'>


# Тим Питерс
# Метаклассы – это глубокая магия,
# о которой 99% пользователей даже не нужно задумываться.
# Если вы думаете, нужно ли вам их использовать — вам не нужно
# (люди, которым они реально нужны, точно знают, зачем они им,
# и не нуждаются в объяснениях, почему)


print("\n---Создадим свой класс с помощью метакласса type")
# type(<имя класса>,
#      <кортеж родительских классов>,
#      <словарь с атрибутами и их значениями>)

class Point:
    MAX_COORD = 100
    MIN_COORD = 0


A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD': 0})
# Здесь переменная A – ссылка на новый созданный класс с именем Point

pt = A() # Создаем экземпляр класса

# Вот мы с вами только что динамически в программе сформировали новый класс
# через метакласс type и увидели, что новый класс
# корректно работает – создает свои экземпляры


print("\n---Пример 2")
# При необходимости, можно дополнительно прописывать базовые классы,
# передавая их список вторым аргументом метаклассу type

# Также, при динамическом создании новых классов, в них можно определять и методы

class Point:
    MAX_COORD = 100
    MIN_COORD = 0

class B1: pass
class B2: pass

def method1(self):
    print("method1:", self.__dict__)

A = type('Point', (B1, B2), {'MAX_COORD': 100,
                             'MIN_COORD': 0,
                             'method1': method1,
                             'method2': lambda self: self.MAX_COORD})

print(A.__mro__)
pt = A()
pt.method1()
print(pt.method2())

