print("----NESTED CONDITIONS even/uneven digit/number status----------------")
x = int(input("number: "))
if x % 2 == 0:
    if 0 <= x <= 9:
        print(f"{x} is an even digit")
    else:
        print(f"{x} is an even number")
else:
    if 0 <= x <= 9:
        print(f"{x} is an uneven digit")
    else:
        print(f"{x} is an uneven number")

print("----------- HOW TO FIND MAX OF 3 NUMBERS ? ----------------")
print("        if it's important not to use new memory cell to store comparison number")
a, b, c = map(float, input("3 numbers:").split())
print(f"a = {a}, b = {b}, c = {c}")

print("maxNum = ", end="")
if a >= b:
    if a >= c:
        print(f"{a}")
    else:
        print(f"{c}")
else:
    if b >= c:
        print(f"{b}")
    else:
        print(f"{c}")
print("Advice: don't use more than 3 layers of comparisons")

print("--------MULTIPLE CHOICE: IF -> ELSE IF -> ELSE IF -> ELSE CONSTRUCTION-------------------")
lang = int(input("Choose language: 1=Python 2=Java 3=C# : "))
if lang == 1:
    print("Python")
else:
    if lang == 2:
        print("Java")
    else:
        if lang == 3:
            print("C#")
        else:
            print("Unknown language")

print("--------MULTIPLE CHOICE: IF -> ELIF -> ELSE CONSTRUCTION-------------------")
print("   if one of elif-blocks triggered next elif-blocks will be ignored")
print("   elif-blocks are very useful when we needs to choose single value of multiple available")
d = int(input("input any positive integer number: "))
if d < 1:
    print("it's negative number")
elif 0 < d < 10:
    print("it's digit")
elif 9 < d < 100:
    print("it's two-valued number")
elif 99 < d < 1000:
    print("it's three-valued number")
elif 999 < d < 100000:
    print("it's multi-valued number")
else:
    print("it's monster-valued number")

print("Advice: Use strict conditions if it's possible, IT'S FASTER then not strict conditions")
print("Advice: Use INT TYPE instead of FLOAT TYPE if it's possible, TO ECONOMY MEMORY")
