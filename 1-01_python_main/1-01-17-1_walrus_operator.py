print("\n--------------------------WALRUS := OPERATOR-------------------------------")
print(":= is a way to assign to variables within(inside) an expression using the notation NAME := expr.")
print("PEP 572 – Assignment Expressions: https://peps.python.org/pep-0572/\n")

print("\n-------VARIABLE ASSIGNMENT")
# x := 33 # INVALID
(x := 33) # Valid alternative
print(f"{x = }")

print("\n-------CASCADING ASSIGNMENT")
x = (y := 6.75) # x = y = 6.75
print(f"{x = }")
print(f"{y = }")
print(f"{x is y = }")

print("\n-------INSIDE LIST")
lst = [y:=1, 2, 3]
print(f"{lst = }")
print(f"{y = }")

print("\n-------INSIDE F-STRING")
print(f"{(x:=5)}")
print(f"{x:=3} walrus operator := without () passes 3 symbols")
print(f"{x = }")

print("\n-------INSIDE IF OPERATOR")
if num := 4.7:
    print(f"{num = }")

print("\n-------INSIDE FUNCTION")

def my_func(var, cat='point'):
    var += 1
    print(f"{var = }; {cat = }")
    return None


my_func(x := 3, cat='vector')
print(f"{x = }")


print("\n-------INSIDE LIST COMPREHENSION")
res = [(y := x + 5, x % y) for x in range(5)]
print(f"{res = }")