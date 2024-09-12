
print("------------map returns iterator----------")
b = map(int, ['1', '3', '7'])

for x in b:
    print(x, type(x), end="\n")

print("--equivalent generator")
a = (int(x) for x in ['1', '3', '7'])   # эквивалентный классический генератор
print(list(a))                          # (а не выражение-генератор: list, set, dict)

print("-----------sum, max, min-----")
b = map(int, ['1', '3', '7'])
print(sum(b))
b = map(int, ['1', '3', '7'])
print(max(b))
b = map(int, ['1', '3', '7'])
print(min(b))

print("-----------cities ex------------")
cities = ["Москва", "Астрахань", "Самара", "Уфа", "Смоленск", "Тверь"]
print(list(map(len, cities)))

print("-----------map with my own func------------")
cities = ["Москва", "Астрахань", "Самара", "Уфа", "Смоленск", "Тверь"]

def symbols(s):
    return s.lower()

b = map(symbols, cities)
print(list(b))

print("-----------map with lambda func------------")
cities = ["Москва", "Астрахань", "Самара", "Уфа", "Смоленск", "Тверь"]
b = map(lambda s: s[::-1], cities)
print(list(b))

print("-----------map with INPUT func------------")
s = map(int, input("input number: ").split())
print(list(s))