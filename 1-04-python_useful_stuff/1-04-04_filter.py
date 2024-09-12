# filter(func, *iterables)
# служит для фильтрации (отбора) элементов указанного итерированного объекта

print("------------filter with lambda--------------")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

print("------------example SIMPLE NUMERIC--------------")
#  простым называется любое натуральное число, которое делится только на себя и на единицу

# исключаем         исключаем 
# ... -2, -1, 0] 1 [2, 3, 4, 5] 6 # анализ числового ряда при проверке числа 6

def is_prost(x):
    d = x-1
    if d < 0:
        return False
    
    while d > 1:
        if x % d == 0:
            return False
        d -= 1
 
    return True

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(is_prost, a)
print(list(b))

print("------------ex filter with str--------------")
lst = ("Москва", "Рязань1", "Смоленск", "Тверь2", "Томск")
b = filter(str.isalpha, lst)
 
for x in b:
    print(x)

print("------------Вложенная функция filter--------------")
# Например, первая (вложенная) функция filter() будет формировать простые числа,
# а вторая (внешняя) выбирать из простых чисел только нечетные.

def is_prost(x):
    d = x-1
    if d < 0:
        return False
    
    while d > 1:
        if x % d == 0:
            return False
        d -= 1
 
    return True

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(is_prost, a)                 # фильтрация только простых чисел
b2 = filter(lambda x: x % 2 != 0, b)    # фильтрация только нечетных
c = tuple(b2)
print(c)
