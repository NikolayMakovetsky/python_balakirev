print("----------CONDITIONAL OPERATOR IF----------------")
print("0 = False, \"\" = False")
print("1 = True, -1 = True, 5.78 = True, \"a\" = True\n--------------------------------------------------------")

print("Insert 2 numbers. if a > b: Changing! a = b, b = a")
a = float(input("a: "))
b = float(input("b: "))
if a > b:
    a, b = b, a
    print(f"Changing! a = {a}, b = {b}")
else:
    print(f"a = {a}, b = {b}")

print("------------------Compound condition------------------")
c = float(input("c: "))
if -5 <= c <= 5 and c != 0:
    print(c, " is in conditions =)")
else:
    print("\"c\" is out of conditions =/")

print("--------------Using conditional operator if in testing list ------------------")
marks = [2, 5, 4, 3, 3]

if 5 in marks:
    print(f"marks = [2, 5, 4, 3, 3] includes item = 5")
