
print("----Функции isinstance и type для проверки типов данных---")
a = 5
print(isinstance(a, int))
print(isinstance(a, float))

print("----")
b = True
print(isinstance(b, bool))  # True
print(isinstance(b, int))   # True
# Это связано с особенностью реализацией типа bool

print("----")
# type() функция различает булевы типы от целочисленных
print(type(b) == bool)
print(type(b) is bool)
print(type(b) is int) # False
print(type(b) in (bool, float, str))

print("--------------ex-----------")
data = (4.5, 4.6, True, "книга", 2, 3, -3, [True, False])

s = sum(filter(lambda x: isinstance(x, float), data))
print(s)
s = sum(filter(lambda x: isinstance(x, int), data)) # 3, т.к. True воспринял как 1
print(s)
s = sum(filter(lambda x: type(x) is int, data)) # строгая проверка
print(s)

print("------отличие isinstance() от type()---------")
#  isinstance() в отличие от type() делает проверку
# с учетом иерархии наследования объектов
# и была разработана для проверки принадлежности объекта тому или иному классу
# Например, тип bool наследуется от int,
# поэтому isinstance() выдает True для обоих типов, когда b – булева переменная

print("------множественные проверки---------")
# Например, мы хотим определить, относится ли число к целому или вещественному типу данных?
a = 5.5
print(isinstance(a, (int, float)))
print(isinstance(a, int) or isinstance(a, float))