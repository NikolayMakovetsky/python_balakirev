

# zip(iter1 [, iter2 [, iter3] ...])
# формирует наборы значений из всех переданных объектов

print("------zip 2 lists-------")

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]

z = zip(a, b)
for x in z:
    print(x, type(x)) # <class 'tuple'>

print("------zip with string-------")
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = "python"

# Иногда удобно кортеж сразу распаковать в отдельные переменные
# и использовать внутри цикла for
z = zip(a, b, c)
for v1, v2, v3 in z:
    print(v1, v2, v3)

print("------zip с оператором распаковки (*)-------")
z1, z2, z3, z4 = zip(a, b, c)
print(z1, z2, z3, z4, sep="\n")
print("----")
z1, *z2 = zip(a, b, c)
print(z1, z2, sep="\n")


print("-----как используя zip получить набор кортежей с обрезанными исх данными-----")
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = "python"
print(a, b, c, sep="\n")

print("-----")

z = zip(a, b, c) # (1, 5, 'p') (2, 6, 'y') (3, 7, 't') (4, 8, 'h')
res = zip(*z)    # (1, 2, 3, 4) (5, 6, 7, 8) ('p', 'y', 't', 'h')
print(*res)
