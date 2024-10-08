# __init__(self) –  инициализатор объекта класса (вызывается сразу после создания экземпляра)
# __del__(self) – финализатор класса (вызывается перед удалением экземпляра)

# Вначале происходит создание объекта в памяти устройства.
# (Перед его созданием вызывается магический метод __new__ 
# Затем, после успешного создания объекта, вызывается магический метод __init__


class Point:
    color = 'red'
    circle = 2
 
    def __init__(self, a, b):
        print("вызов __init__")
        self.x = a
        self.y = b

    def __del__(self):
        print("Удаление экземпляра: "+ str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y
 
    def get_coords(self):
        return (self.x, self.y)

pt = Point(4, 7)
print(pt.__dict__)

# Интерпретатор языка Python имеет, так называемый, сборщик мусора.
# Это алгоритм, который отслеживает объекты
# и как только они становятся ненужными, удаляет их.