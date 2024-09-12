# Начнем со знакомства с функцией:

# open(file [, mode=’r’, encoding=None, …])

# которая открывает указанный файл на чтение или запись данных
# (по умолчанию – на чтение). Основные ее параметры, следующие:

# file – путь к файлу (вместе с его именем);
# mode – режим доступа к файлу (чтение/запись);
# encoding – кодировка файла.

print("--------------windows-1251--------------")
file = open("files//docs//myfile.txt", mode='r', encoding="windows-1251")
print( file.read() )
file.close()

print("--------------utf-8--------------")
file = open("files//docs//myfile.txt", mode='r', encoding="utf-8")
print( file.read() )
file.close()

print("--------------utf-8--------------")
file = open("files//docs//myfile.txt", mode='r', encoding="utf-8")
print( file.read(4) )  # read first 4 symbols, first is system-start invisible symbol
file.close()

print("-------------seek and tell-------------")
file = open("files//docs//myfile.txt", mode='r', encoding="utf-8")

print( file.read(3) )  # read first 3 symbols
pos = file.tell() # return number of position
print( pos )

file.seek(0) # stand cursor to position with number 0
print( file.read(10) )
pos = file.tell()
print( pos )

file.close()

print("-------------readline-------------")
file = open("files//docs//myfile.txt", mode='r', encoding="utf-8")

print( file.readline(), end="" )
print( file.readline(), end="" )

file.close()

print("-------------for loop-------------")
file = open("files//docs//myfile.txt", mode='r', encoding="utf-8")

for line in file:
    print( line, end="" )

file.close()

print("\n-------------take all lines as list-------------")
file = open("files//docs//myfile.txt", mode='r', encoding="utf-8")

s = file.readlines()
print( s )

file.close()    