class Point:
    "Класс для представления координат точек на плоскости"
    color = 'red'
    circle = 2

a = Point()
b = Point()

print(f"{type(a) = }")                  # <class '__main__.Point'>
print(f"{isinstance(a, Point) = }")     # True

print("---")
print(f"{Point.__dict__ = }") # 2
Point.circle = 1
print(f"{Point.__dict__ = }") # 1

print("---")
b.color = 'green'
b.circle = 5
print(f"{b.__dict__ = }")       # {'color': 'green', 'circle': 5}

print(hasattr(b, 'color'))      # True
print(getattr(b, 'circle'))     # 5
setattr(b, 'categ', 'mypoint')
delattr(b, 'color')

print(f"{b.__dict__ = }")       # {'circle': 5, 'categ': 'mypoint'}
