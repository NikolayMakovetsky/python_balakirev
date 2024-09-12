# открывая файл на запись, его прежнее содержимое автоматически удаляется!!!

print("--------------вар 1----------------")
file = open("files//docs//log.txt", "w")

file.write("Hello World!")
file.close()

print("--------------вар 2----------------")
try:
    with open("files//docs//log.txt", "w") as file:
        file.write("try-2 Hello World!")
except:
    print("Ошибка при работе с файлом")

print("--------------вар 3----------------")
try:
    with open("files//docs//log.txt", "w") as file:
        file.write("try-3\n")
        file.write("Hello\n")
        file.write("Hello\n")
        file.write("Hello\n")
except:
    print("Ошибка при работе с файлом")

print("--------------append to file----------------")
try:
    with open("files//docs//log.txt", "a") as file:
        file.write("try-4\n")
        file.write("World!!!!!!\n")
        file.write("World!!!!!!\n")
        file.write("World!!!!!!\n")
except:
    print("Ошибка при работе с файлом")


print("--------------append and read----------------")
try:
    with open("files//docs//log.txt", "a+") as file:
        file.write("try-5\n")
        file.write("good by\n")
        file.seek(0)
        print( file.read(10) )
except:
    print("Ошибка при работе с файлом")

# Запись данных всегда осуществляется в конец файла,
# так как для записи используется другая файловая позиция
# и она указывает на конец файла.

print("--------------writelines----------------")
try:
    with open("files//docs//log.txt", "a+") as file:
        file.writelines(["____try-6\n", "TEXT1\n", "TEXT2\n"])
        file.seek(30)
        print( file.read(10) )
except:
    print("Ошибка при работе с файлом")