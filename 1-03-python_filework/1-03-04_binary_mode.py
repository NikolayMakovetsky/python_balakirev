# Что такое бинарный режим доступа?
# Это когда данные из файла считываются один в один без какой-либо обработки.
# Обычно он используется для сохранения и считывания объектов целиком.

import pickle # модуль для работы с бинарными файлами

book1 = ["Евгений Онегин", "Пушкин А.С.", 200]
book2 = ["Муму", "Тургенев И.С.", 250]
book3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
book4 = ["Мертвые души", "Гоголь Н.В.", 190]
 
try:
    with open("files//docs//out.bin", "wb") as file:
        pickle.dump(book1, file)
        pickle.dump(book2, file)
        pickle.dump(book3, file)
        pickle.dump(book4, file)
except:
    print("Ошибка при работе с файлом")


try:
    with open("files//docs//out.bin", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)
except:
    print("Ошибка при работе с файлом")
 
print(b1, type(b1)) #  <class 'list'>, а не строка !!!
print(b2, type(b2))
print(b3, type(b3))
print(b4, type(b4))