print("----------------------TERNARY CONDITIONS OPERATOR------------------")
print("TCO automatically returns result, so basically we should use variable to save it")
print("            res = a if a > b else b".upper())
print("  instead of A and B we can use also some simple Python constructions")
print("------------------------EXAMPLES--------------------------------")
a = 12
b = -7
res = a if a > b else b
print(f"a = {a}\nb = {b}\nres = a if a > b else b                        res =", res)
res = a + 2 if a > b else b - 5
print("res = a + 2 if a > b else b - 5                res =", res)
res = abs(a) if a < b else abs(b)
print("res = abs(a) if a < b else abs(b)              res =", res)
res = [1, 2, a if a > b else b, 4, 5]
print("res = [1, 2, a if a > b else b, 4, 5]          res =", res)
print("----------------------------------------------------------")
str = "PYthon"
mod = "up"
res = str.upper() if mod == "up" else str
print(f"str = {str}\nmod = {mod}\nres = str.upper() if mod == \"up\" else str      res =", res)
print("-------------------EVEN OR UNEVEN NUMBER-------------------------------")
d = int(input("number: ").strip())
print(f"{d} is " + ("even" if d % 2 == 0 else "uneven") + " number")
print("-----------------BAD IDEA TO USE ONE TCO INTO ANOTHER TCO---------------------")
print("        lets find max of 3 numbers using ternary conditions operator")
a, b, c = map(float, input("3 numbers:").split())
print(f"a = {a}, b = {b}, c = {c}")
maxNum = (a if a > c else c) if a > b else (b if b > c else c)
print("maxNum = (a if a > c else c) if a > b else (b if b > c else c)      maxNum =", maxNum)
