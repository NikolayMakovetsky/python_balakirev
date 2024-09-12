print("\n----------------------TRUTHY / FALSY VALUE---------------------------")

print('''\nhttps://docs.python.org -> Built-in Types -> Truth Value Testing
Any object can be tested for truth value, for use in:
    1. IF condition
    2. WHILE condition
    3. or as operand of the Boolean operations below (AND, OR, NOT)

By default, an object is considered TRUE unless its class defines either a __bool__() method that returns False
or a __len__() method that returns zero, when called with the object.
Python looks for __bool__ first, then __len__. If neither is defined, all instances are considered "true". 

Here are most of the built-in objects considered false:
* constants defined to be false: None and False.
* zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
* empty sequences and collections: '', (), [], {}, set(), range(0)

Boolean Operations — and, or, not
These are the Boolean operations, ordered by ascending priority:
Operation              Result                   Notes
x or y      if x is true, then x, else y        (1)
x and y     if x is false, then x, else y       (2)
not x   if x is false, then True, else False    (3)''')

print("\n----------------------1. IF condition---------------------------")
my_list = [1]
if my_list: # if len(my_list) != 0:
    print(f"{my_list = }")
    print(f"{bool(my_list) = }")
    print("Not empty!")

print("\n----------------------2. WHILE condition---------------------------")

n = 1
while n: # while n != 0
    print("while loop iteration")
    n -= 1

print("\n----------------------3.1 AND------------------------------------")
print("x AND y  ->  if x is false, then x, else y\n")
print(f"""{'' and [1, 2] = }
{6 and [1, 2] = }
{'' and {} = }
{6 and True and 0 and 1.4 and '' and [1, 2] = }    // We go from left to right!
{6 and True and 5 and 1.4 and '' and [1, 2] = }
{6 and True and 5 and 1.4 and 'hi' and [1, 2] = }""")


print("\n----------------------3.2 OR------------------------------------")
print("x OR y   ->  if x is true, then x, else y\n")
print(f"""{'' or [1, 2] = }
{6 or [1, 2] = }
{'' or {} = }
{'' or False or 0 or 1.4 or 'hi' or [1, 2] or '' or {} = }    // We go from left to right!
{'' or False or 0 or 0.0 or 'hi' or [1, 2] or '' or {} = }
{'' or False or 0 or 0.0 or '' or [1, 2] or '' or {} = }""")

s = ""
print(f"\n{s = }")
print(f"{s or 'Default value' = }")

s = "John"
print(f"\n{s = }")
print(f"{s or 'Default value' = }")


print("\n--------------------------------3.3 NOT------------------------------------")
print(f"{not 5 = }")
print(f"{not [] = }")

print("\n----------------------AND OR NOT EXAMPLE------------------------------------")
print("priority level: not(3), and(2), or(1)\n")
print(f"""{(not '') = }
{(5 and False) = }
{(not '') or (5 and False) = }
{not '' or 5 and False = }""")

print("\n---------------------CONDITION WITHOUT IF OPERATOR------------------------------")
x = -5
print(f"Before: {x = }")  # -5
x *= x > 0 # x = x * (x > 0)   1. x = x * 0  2. x = x * 1
print(f"After: {x = }")  # 0
