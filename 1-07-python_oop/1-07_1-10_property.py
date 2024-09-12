# На этом занятии вы узнаете о более удобном способе работы
# с приватными атрибутами через специальный объект property,
# который переводится как свойство.

print("\n---Класс без декораторов")

class Person:
    def __init__(self, name, old):
        # Приватные атрибуты (имя и возраст)
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old
 
    def set_old(self, old):
        self.__old = old

# При такой реализации нам нужно прописывать функции-сеттеры и геттеры
# при работе с атрибутами, что неудобно

p = Person('Сергей', 20)
p.set_old(35)
print(p.get_old())

print("\n---Использование экземпляра класса property (Некорректный вариант)")

class Person:
    
    def __init__(self, name, old):
        # Приватные атрибуты (имя и возраст)
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old
 
    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)

p = Person('Сергей', 20)
p.old = 35      # отработает set_old вместо создания атрибута экземпляра !!! ВАЖНО !
print(p.old)    # get_old

print(Person.__dict__['old'])   # <property object at 0x000002DF3CF12200>
# print(p.__dict__['old'])      # KeyError: 'old' т.к. атрибут в экземпляре
                                # не создается при использовании property

p.__dict__['old'] = 'old in p'  # принудительно создадим 'old' в экземпляре
print(p.old, p.__dict__)        # 35, {...}
                                # всё равно видим 35 при обращении к p.old
                                # то есть, было обращение именно
                                # к объекту-свойству old класса Person!!!


# Сейчас мы можем работать с приватным свойством __old
# и через сеттер/геттер и через свойство класса old.
# Было бы лучше иметь ОДИН интерфейс взаимодействия со свойством __old.
# Как это можно сделать?


print("\n---Использование экземпляра класса property (Рабочий вариант)")
# a = property()
# a.getter()      декоратор для сеттера
# a.setter()      декоратор для геттера
# a.deleter()     декоратор для делитера

class Person:
    
    def __init__(self, name, old):
        # Приватные атрибуты (имя и возраст)
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old
 
    def set_old(self, old):
        self.__old = old

    old = property()          # создаем объект класса property
    old = old.setter(set_old) # встраивание метода set_old в алгоритм работы объекта property
    old = old.getter(get_old) # встраивание метода get_old в алгоритм работы объекта property

p = Person('Сергей', 20)
p.old = 35      # setter
print(p.old)    # getter

print("\n---Декоратор @property (Лучший вариант)")
# Лучше всего использовать декораторы, чтобы нужный нам метод класса
# сразу превратить в объект-свойство property

class Person:
    
    def __init__(self, name, old):
        # Приватные атрибуты (имя и возраст)
        self.__name = name
        self.__old = old
    
    @property # этот декоратор прописывается именно перед геттером
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

# Теперь у нас остался один единственный интерфейс взаимодействия
# с приватным атрибутом __old через объект-свойство old класса property!

p = Person('Сергей', 20)
p.old = 35      # setter
print(p.old)    # getter
print(p.__dict__)
# print(p.__old)  # AttributeError: 'Person' object has no attribute '__old'
del p.old       # deleter
print(p.__dict__)
p.old = 98
print(p.__dict__)
