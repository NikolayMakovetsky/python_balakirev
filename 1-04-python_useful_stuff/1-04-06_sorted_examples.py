print("-----------Сортируем символы в строке-----------")

s = "Сортируем номера, соответствующие Символам Алфавита, по возрастАнию"

print(ord('f'))

#Функция для сортировки строки
def char_sort(ch):
    if ch == ch.lower():
        return ord(ch)
    return ord(ch.lower()) - 0.1

#Вар.1
ssort = sorted(s, reverse=False)
print("".join(ssort))

#Вар.2
ssort = sorted(s, key=lambda x: x.lower())
print("".join(ssort))

#Вар.3
ssort = sorted(s, key=lambda x: char_sort(x))
print("".join(ssort))

print("-----------сортировка по возрастанию------------")

# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))

# string
py_string = 'Python'
print(sorted(py_string))

# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))

print("-----------сортировка по убыванию------------")

# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))

# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse=True))

# frozen set
frozen_set = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(frozen_set, reverse=True))

print("-----------Сортировка списка с ключевой функцией------------")
# take the second element for sort
def take_second(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(random, key=take_second)

# print list
print('Random list:', random)
print('Sorted list:', sorted_list)


print("-----------Сортировка с использованием нескольких ключей------------")
# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100, Age)

participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

# Отсортировать список нужно таким образом,
# чтобы ученик с самыми высокими оценками был в начале.
# Если ученики имеют одинаковые оценки, их необходимо отсортировать так, чтобы младший участник был первым.
# Мы можем добиться этого типа сортировки с несколькими ключами, возвращая кортеж вместо числа.
# Два кортежа можно сравнить, вместе с их элементами, начиная с первого.
# Если есть связь (элементы равны), сравнивается второй элемент и так далее.
# >>> (1,3) > (1, 4)
# False
# >>> (1, 4) < (2,2)
# True
# >>> (1, 4, 1) < (2, 1)
# True

def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)


sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)

print("-----------Сортировка с использованием нескольких ключей (ПРИМЕНЯЕМ ЛЯМБДА-ФУНКЦИЮ )  ------------")

sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
print(sorted_list)

