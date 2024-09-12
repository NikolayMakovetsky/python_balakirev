# __iter__(self) – получение итератора для перебора объекта
# __next__(self) – переход к следующему значению и его считывание


print("\n---Послед вещ чисел арифм прогрессии")

class FRange:
    """Выдача последовательности вещественных чисел арифметической прогрессии"""
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    # метод необходим для перебора значений итератора в цикле
    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        """мы увеличиваем значение value на шаг step
         и возвращаем до тех пор,
         пока не достигли значения stop (не включая его)"""
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

# цикл for именно так и перебирает итерируемые объекты,
# сначала неявно вызывает функцию iter(),
# а затем, на каждой итерации – функцию next(),
# пока не возникнет исключение StopIteration
fr = FRange(0, 2, 0.5)
for x in fr:
    print(x, end=" ")

print("\n---")
fr = FRange(5, 8, 0.7)
it = iter(fr)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) # StopIteration


print("\n---Формирование таблиц значений")

class FRange2D:
    """Формирование таблиц значений"""
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.fr = FRange(start, stop, step)
        self.rows = rows


    def __iter__(self):
        self.value_row = 0
        return self


    def __next__(self):
        if self.value_row < self.rows:
            self.value_row += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr = FRange2D(0, 2, 0.5, 4)

for row in fr:
    for x in row:
        print(x, end=" ")
    print()



