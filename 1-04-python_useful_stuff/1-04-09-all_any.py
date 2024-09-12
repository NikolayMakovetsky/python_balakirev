

print("----------all ex 1---------")
a = [True, True, True]
print(a)
print(all(a))

a = [True, False, True]
print(a)
print(all(a))

a = [False, False, False]
print(a)
print(all(a))

print("----------all ex 2---------")
# Мы ранее говорили, что любое значение можно привести к типу Bool
a = [0, 1, 2.5, "", "python", [], [1, 2], {}] # 0, "", [], {} is False
print(a)
print(all(a))

all_res = []
for x in a:
    all_res.append(bool(x))
 
print(all_res)

print("----------any ex 1---------")
a = [True, True, True]
print(a)
print(any(a))

a = [True, False, True]
print(a)
print(any(a))

a = [False, False, False]
print(a)
print(any(a))

print("-----------игра «Крестики-нолики»----------")
P = ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
# x x o 
# o x o
# x x x 

def true_x(a):
    return a == 'x'

row_1 = all(map(true_x, P[:3]))
row_2 = all(map(true_x, P[3:6]))
row_3 = all(map(true_x, P[6:]))
print("rows:", row_1, row_2, row_3, sep=" ")

diag_1 = all(map(true_x, [P[0], P[4], P[8]]))
diag_2 = all(map(true_x, [P[2], P[4], P[6]]))
print("diags:", diag_1, diag_2, sep=" ")

print("-------------- игра «Сапер»-----------------")