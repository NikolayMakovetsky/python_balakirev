# В Python можно описывать свои собственные метаклассы,
# которые, конечно же, явно или неявно наследуются от основного метакласса type.


print("\n---Функция-метакласс")
# предположим, что мы бы хотели создавать классы для точек,
# в которых бы автоматически появлялись атрибуты MAX_COORD и MIN_COORD

# name – имя создаваемого класса
# base – кортеж из базовых классов
# attrs – словарь с атрибутами класса

# Сейчас в этой функции мы в словарь attrs
# добавляем два атрибута MAX_COORD и MIN_COORD,
# а затем, явным вызовом метакласса type
# формируем новый класс и возвращаем его

def create_class_point(name, base, attrs):
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
    return type(name, base, attrs)


# Теперь, чтобы эта функция использовалась в качестве метакласса,
# при объявлении класса нужно прописать специальный параметр metaclass
# и передать ссылку на эту функцию
class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)

pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())


print("\n---Создание собственного метакласса как класса")

class Meta(type): # имя Meta выбрано для примера
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.MAX_COORD = 100
        cls.MIN_COORD = 0


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)
 
pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())


print("\n---Тонкая настройка (переопределяем __new__ вместо __init__)")
# Однако, инициализатор __init__() в классе Meta вызывается
# когда класс Point полностью создан.
# Для более тонкой работы лучше переопределить
# магический метод __new__,
# который вызывается непосредственно перед созданием класса

class Meta(type):

    def __new__(cls, name_class, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name_class, base, attrs)

# cls – ссылка на текущий класс Meta
# name_class – имя создаваемого класса
# base – кортеж из базовых классов
# attrs – словарь атрибутов создаваемого класса

# Так как метод __new__ вызывается до создания нового класса,
# то мы добавляем новые атрибуты MAX_COORD и MIN_COORD
# непосредственно в словарь attrs.
# А, затем, вызываем аналогичный метод __new__ у объекта-метакласса type.
# Обратите внимание, метод __new__ должен вернуть ссылку на созданный класс,
# то есть, обязательно следует прописать оператор return.


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)
 
pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())

