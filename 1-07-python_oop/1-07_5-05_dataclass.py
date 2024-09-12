from dataclasses import dataclass, field


print("\n---Вычисляемое свойство. Метод __post_init__()")

@dataclass
class V3D:
    x: int
    y: int
    z: int
 
    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v) # V3D(x=1, y=2, z=3)...length нету в выводе!

print(v.__dict__)
# магический метод __repr__() выводит только те атрибуты,
# которые были указаны при объявлении класса.
# Все остальные, что создаются в процессе формирования объекта,
# не учитываются в методе __repr__()


print("\n---Добавление вычисляемого атрибута length в  __repr__()")

@dataclass
class V3D:
    x: int
    y: int
    z: int
    length: float = field(init=False)
    # Мы здесь воспользовались уже знакомой нам функцией field() и отметили,
    # что атрибут length не следует использовать
    # в качестве параметра инициализатора
 
    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v) # V3D(x=1, y=2, z=3, length=3.7416573867739413) # length ИМЕЕТСЯ

print("\n---Функция field()")
# Мы увидели, как работают два ее параметра: init и default_factory.
# Довольно часто можно встретить использование еще трех:

# repr      – булевое значение True/False указывает использовать ли атрибут в магическом методе __repr__() (по умолчанию True)
# compare   – булевое значение True/False указывает использовать ли атрибут при сравнении объектов (по умолчанию True)
# default   – значение по умолчанию (начальное значение)

@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    length: float = field(init=False, compare=False)
 
    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

v = V3D(1, 2, 3)
v2 = V3D(1, 2, 5)
print(v)        # V3D(y=2, z=3, length=3.7416573867739413)
print(v2)       # V3D(y=2, z=5, length=5.477225575051661)
print(v == v2)  # True (z,length мы не использовали при сравнении объектов)


