
print("--------classic sorted()--------")
# По умолчанию сортировка коллекции выполняется по значениям ее элементов
a = [4, 3, -10, 1, 7, 12]
b = sorted(a)
print(b)

print("-----------sorted() with key(x % 2)----------")
# Но мы можем вместо этих значений указать другие, используя key
a = [4, 3, -10, 1, 7, 12]

def is_odd(x):
    return x % 2

b = sorted(a, key=is_odd)
print(b)

# b = sorted(a, key=lambda x: x % 2)  # короткий вариант записи
# a.sort(key=lambda x: x % 2)       # короткий вариант записи

print("-----------sorted() with complex key----------")
# Теперь у нас выполняется не только разделение на четные и нечетные значения,
# но и их сортировка внутри групп.
a = [4, 3, -10, 1, 7, 12]

def key_sort(x):
    return x if x % 2 == 0 else 100 + x

b = sorted(a, key=key_sort)
print(b)

print("-----------ex with towns----------")
lst = ["Москва", "Тверь", "Смоленск", "Псков", "Рязань"]
print( sorted(lst, key=len) )
print( sorted(lst, key=lambda x: x[-1]) )
print( sorted(lst, key=lambda x: x[0]) )

print("---------ex with books in library--------")
books = (
    ("Евгений Онегин", "Пушкин А.С.", 200),
    ("Муму", "Тургенев И.С.", 250),
    ("Мастер и Маргарита", "Булгаков М.А.", 500),
    ("Мертвые души", "Гоголь Н.В.", 190)
)

print( sorted(books, key=lambda x: x[2]) )
