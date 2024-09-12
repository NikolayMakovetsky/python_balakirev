print(f"""\n---------- PRINT() OUTPUT DATA TO CONSOLE -----------
parameter SEP -> set type of element that will separate parts of output data
parameter END -> set end element of output data""")
print("EXAMPLE:", "hello", "world", sep=" ! ", end=" ")
print("|| sep=\" ! \", end=\" \"")
print("IN EXAMPLE default end element =\"\\n\" changed to element \" \"")

print("\n---------- F-LINES format output -----------".upper())
x = 5.76
y = -8
print(f"Actual coordinates of point | x: {x}, y: {y}")  # x: 5.76, y: -8

print("\n---------- INPUT() take string information from users keyboard -----------".upper())
print("Input integer numeric:", end=" ")
a = int(input())  # We retype string information to integer and save link to it in variable 'a'
print(f"Your choice: {a}, {type(a)}")

print("\n---------- map() how to insert 2 parameters in 1 line? -----------".upper())
print("Insert 2 sides of rectangle with space separation:", end=" ")
a, b = map(float, input().split())
print(a, type(a), b, type(b), f"Square = {a * b}")

print("\n--------------------------- map() basic info -----------------------------".upper())
print("GENERAL SYNTAX: map(function, iterable, [iterable1, iterable2, ...])")
print("applies a function to each item in an iterable, returns iterable")
lNums = [1, 2, 3, 4, 5]

def Cube(num):
    return num**3

print(f"lNums = {lNums}, list(map(Cube, lNums)) = {list(map(Cube, lNums))}")

