
print("------------function-generator-------------")
def get_list():
    for x in [1, 2, 3, 4]:
        yield x

d = get_list()
for i in d:
    print(i, end=" ")   # распечатываем генератор поэлементно
                        # (в моменте формурием новое значение и распечатываем его)
                        

# yield превращает обычную функцию в генератор
# и при каждом вызове функции next() активизируется функция-генератор,
# возвращает очередное значение и «замораживает» свое состояние
# вместе с локальными переменными до следующего вызова функции next()

print("\n------------ex 2-------------")
def avg_gen(N):
    for i in range(1, N):
        a = range(i, N+1)
        print(f"{a = }, {sum(a) = }, {len(a) = }") # демонстрация работы функции
        yield sum(a) / len(a)

b = avg_gen(5)
print(list(b)) # генератор через список сразу весь распечатываем

# В выражении генератора мы можем записать лишь один оператор для формирования значения,
# а в функции-генераторе – произвольный фрагмент программы,
# реализующий нужную нам логику формирования очередного значения.

print("\n---------------search in file----------------")
# хотим найти все начальные индексы слова «ГЕНЕРАТОР» в текстовом файле yield.txt

print("find func example")
msg = "abrakadabra"
# возвращает индекс первого найденного вхождения подстроки sub в строке String
print(msg.find("br"))
print(msg.find("brr")) # возвращает -1 при ненахождении подстроки в строке
print("------------")

def find_word(f, word):
    g_indx = 0
    for line in f:
        indx = 0
        while(indx != -1):
            indx = line.find(word, indx)
            if indx > -1:
                yield g_indx + indx
                indx += 1
        g_indx += len(line)

try:
    with open("files//yield.txt", encoding="utf-8") as file:
        a = find_word(file, "ГЕНЕРАТОР")
        print(list(a))
except FileNotFoundError:
    print("Файл не найден!")
except:
    print("Ошибка обработки файла!")

