print("                           RETURN OPERATOR")
print("Backslash just tells the Python interpreter that the statement continues on the next line!")
print("""
   (object with value 49)
             ^
             |
def get_sqrt(x):                          new object created by function
    res = None\                                     _________              // vars x, res alive only in function body
          if x < 0\                                 |       |              // it's possible to use 
          else x ** 0.5-----------value record-------->7.0  |              // only 1 return in function!
    return res------------------link to object----->|       |              // but if you write 2 or more returns
                                                    ---------              // only first will working""")


def get_sqrt(x):
    res = None\
          if x < 0\
          else x ** 0.5
    return res


print(f"get_sqrt(49) = {get_sqrt(49)}")

print("\n-------------------------USE TUPLE TO RETURN 2 VARIABLES------------------------")


def get_SumAndDiff(v1, v2):
    tpl = (v1 + v2, v1 - v2)
    return tpl


print(f"get_SumAndDiff(9, 3) = {get_SumAndDiff(9, 3)}")

print("\n-------------------------GET MAX OF 3 NUMBERS-------------------------")


def getMax(a, b, c):
    res = max([a, b, c])
    return res


a, b, c = map(int, input("3 numbers: ").split())
print(f"getMax({a}, {b}, {c}) = {getMax(a, b, c)}")

print("\n                            NESTED FUNCTIONS")

print("\n-------------------------GET MAX OF 2 and 3 NUMBERS-------------------------")


def getMax2(a, b):
    return a if a > b else b


print("return a if a > b else b")
a, b = map(int, input("2 numbers: ").split())
print(f"getMax2({a}, {b}) = {getMax2(a, b)}")


def getMax3(a, b, c):
    return getMax2(a, getMax2(b, c))


print("\nClassic functional programming: return getMax2(a, getMax2(b, c))")
a, b, c = map(int, input("3 numbers: ").split())
print(f"getMax3({a}, {b}, {c}) = {getMax3(a, b, c)}")

print("\n-------------------------FUNCTION ANNOUNCEMENT WITH VARIABLE BODIES-------------------------")
mode = int(input("func mode = 1 (perimeter) OR 0 (square): "))

if mode == 1:
    def get_rect(a, b):
        return 2 * (a + b)
else:
    def get_rect(a, b):
        return a * b

a, b = map(int, input("2 sides of rectangle: ").split())
print(f"mode = {mode} get_rect({a}, {b}) = {get_rect(a, b)}")

print("\n-----------------LET'S DEFINE 2 FUNCTIONS WITH THE SAME NAME-------------------------")
print("first defined function will be deleted by garbage cleaner")


def get_rect(a, b):
    return 2 * (a + b)


def get_rect(a, b):
    return a * b


print(f"get_rect(2, 4) = {get_rect(2, 4)}  // return {a} * {b}  // first declared function deleted by garbage cleaner")

print("\n------------------USE FUNCTION WHERE YOU NEED IT (in for loop for example)------------------------")


def even(x):
    return x % 2 == 0


lst = [1, 3, 2, 2, 8]
print(f"lst = {lst}")
for i, d in enumerate(lst):
    if even(d):
        lst[i] = 0
print(f"lst = {lst}")
