# Метод класса – это тоже его атрибут и когда создаются экземпляры класса,
# то метод становится общим для всех объектов и не копируется в них.
# Фактически, только благодаря параметру self мы «знаем» какой объект
# вызвал данный метод и можем организовать с ним обратную связь.


class Point:
    color = 'red'
    circle = 2
 
    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print("вызов метода set_coords " + str(self))

 
    def get_coords(self):
        return (self.x, self.y)


pt = Point()

pt.set_coords(1, 2)
Point.set_coords(pt, 1, 2)

print(f"{pt.get_coords() = }")
print(f"{Point.get_coords(pt) = }")

res = getattr(pt, 'get_coords')
print(res()) # требуется вызов, т.к. get_coords это функция