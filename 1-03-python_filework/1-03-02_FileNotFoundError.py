# Для обработки подобных ошибок (или, как говорят, исключений)
# существует специальная группа операторов:
# try / except / finally

print("--------------вар 1----------------")
try:
    file = open("files//docs//myfile.txt", encoding='utf-8')
    s = file.readlines()
    print(s)
    file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")

print("--------------вар 2----------------")
try:
    file = open("myfile.txt", encoding='utf-8')
 
    try:
        s = file.readline()
        print(s)
    finally:
        file.close()
        
except FileNotFoundError:
     print("Невозможно открыть файл")
except: 
    print("Ошибка при работе с файлом")

print("--------------вар 3----------------")
try:
    with open("myfile.txt", encoding='utf-8') as file:
        s = file.readlines()
        print( s )
 
except FileNotFoundError:
     print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")

print("--------------вар 4----------------")
try:
    # with - аналог конструкции try / finally
    with open("myfile.txt", encoding='utf-8') as file:
        s = file.readlines()
        print( s )
 
except FileNotFoundError: # обработка исключения
     print("Невозможно открыть файл")
except: # обработка исключения
    print("Ошибка при работе с файлом")
finally: # блок операторов, которые всегда и обязательно будут исполнены
    print(file.closed)
