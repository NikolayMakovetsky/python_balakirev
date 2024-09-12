# Вычисление хеша для объектов классов

# функция hash формирует по определенному алгоритму
# целочисленные значения для неизменяемых объектов

print("\n---функция hash()")
print(hash(123))
print(hash("Python"))
print(hash((1, 2, 3)))
# hash([1, 2, 3]) # TypeError: unhashable type: 'list'
# # хэши можно вычислять только для неизменяемых объектов

print("\n---свойства хеша")
# Если объекты a == b (равны), то равен и их хэш.
# Если равны хеши: hash(a) == hash(b), то объекты могут быть равны,
# но могут быть и не равны.
# Если хеши не равны: hash(a) != hash(b), то объекты точно не равны.

print("\n---Словарь в питоне использует хеш")
# под капотом ключи в словаре хранятся в виде: (хэш ключа, ключ)
# высокая скорость поиска достигается за счет поиска
# сначала по хэшу ключа, а затем по ключу
d = {}
d[5] = 5
d["python"] = "python"
d[(1, 2, 3)] = [1, 2, 3]
print(d)

print("\n---Рассмотрим класс")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # мы подменили вычисление хэша объекта класса Point
    # на вычисление хэша от координат точки
    # чтобы экземпляры класса стали хэшируемыми объектами
    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(hash(p1), hash(p2), sep='\n')
# Функция hash() ориентируется на дандер-метод __eq__
# Если оператор сравнения __eq__ дает True, то объекты равны, иначе – не равны,
# Однако если мы переоприделим метод __eq__, то объекты станут нехэшируемыми.
# Как же быть? Переопределить метод __hash__

d = {}
d[p1] = 1
d[p2] = 2
print(d) # p1 и p2 воспринимаются как один и тот же ключ