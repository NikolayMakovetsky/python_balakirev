# __getitem__(self, item)         – получение значения по ключу item
# __setitem__(self, key, value)   – запись значения value по ключу key
# __delitem__(self, key)          – удаление элемента по ключу key


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __str__(self):
        return f"{self.name}: {self.marks}"

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом")
 
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")


    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        
        # Если индекс превышает размер списка,
        # то мы расширяем список значениями None до нужной длины
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
            # Сергей: [5, 5, 4, 2, 5, None, None, None]
        
        self.marks[key] = value
        # Сергей: [5, 5, 4, 2, 5, None, None, 99]


    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")
 
        del self.marks[key]


s1 = Student('Сергей', [5, 5, 3, 2, 5])
print(s1.marks[2])  # 3
print(s1[2])        # 3
s1[2] = 4
print(s1[2])        # 4
# print(s1[20])     # IndexError: Неверный индекс
# print(s1['abc'])  # TypeError: Индекс должен быть целым числом
s1[7] = 99
print(s1)
del s1[0]
del s1[0]
del s1[-1]
print(s1)

