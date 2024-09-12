print("\n--------------------LAMBDA ANONYMOUS FUNCTION-------------------")
print("a function that includes only one python construction and returns one value")
print("lambda can be written only in one line")
print("lambda has automatical return operator inside itself")
print("in lambda we can't use operator '=': lambda a : a = 1 -> ERROR!")
print("inside lambda we can create an object by using incoming parameters and Global variables")
print("""\n-----------------------SYNTAX--------------------------
keyword           if we need it               
   ---     --------------------------          ---
lambda parameter1, parameter2...parameterN : command
""")

print("\n--------------USE VARIABLE TO SAVE LAMBDA FUNCTION IN MEMORY----------------")
s = lambda a, b : a + b
print(f"s = lambda a, b : a + b  ->  {s = }")
print(f"s = lambda a, b : a + b  ->  {s(1, 2) = }")

print("\n------------USE LAMBDA IN DIFFERENT PYTHON CONSTRUCRIONS-----------")
a = [1, lambda a : a ** 2, 3]
print(f"a = [1, lambda a : a ** 2, 3]   ->   {a = }")
print(f"a = [1, lambda a : a ** 2, 3]   ->   {a[1] = }")
print(f"a = [1, lambda a : a ** 2, 3]   ->   {a[1](3) = }  // () - calling operator")

print("\n-------------HOW TO MODIFY VARS IN LIST IN DIFF WAYS BY USING ONE FUNCTION?-----------")


def get_modify(a, fctn = None):
    if fctn:
        for x, y in enumerate(a):
            a[x] = fctn(y)


lst = [1, 2, 3, 4, 5]
print(f"{lst = }\n")
get_modify(lst, lambda x : x * 0 if x > 2 else x)
print(f"{lst = }      // get_modify(lst, lambda x : x * 0 if x > 2 else x)")
get_modify(lst, lambda x : x + 3)
print(f"{lst = }      // get_modify(lst, lambda x : x + 3)")
get_modify(lst, lambda x : True if x == 5 else x)
print(f"{lst = }   // get_modify(lst, lambda x : True if x == 5 else x)")
get_modify(lst, lambda x : 5)
print(f"{lst = }      // get_modify(lst, lambda x : 5)")


print("\n----------------------LAMBDA AS KEY IN SORT() AND SORTED()----------------------")
list_of_tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]


def new_order(x):  # Own sort func for itarable objects
    return x[1]


print(f"""{list_of_tuples = }\n
{sorted(list_of_tuples) = }
{sorted(list_of_tuples, key=lambda x: x[1]) = }
{sorted(list_of_tuples, key=new_order) = }    // new_order() - our own sort func""")

print("-" * 30)

print(f"""\n{range(-5, 6) = }
{sorted(range(-5, 6), key=lambda x: x * x) = }
                             HOW DOES IT WORK?
                 range(-5, 6) = -5 -4 -3 -2 -1 0 1 2 3 4 5
                          key = 25 16 9 4 1 0 1 4 9 16 25 (key=lambda x: x * x)
                   sorted key = 0 1 1 4 4 9 9 16 16 25 25
sorted(range(-5, 6), key=...) = 0 -1 1 -2 2 -3 3 -4 4 -5 5

{"-" * 30}

{sorted(range(5, -6, -1), key=lambda x: x * x) = }
                             HOW DOES IT WORK?
                    range(5, -6, -1) = 5 4 3  1 0 -1 -2 -3 -4 -5
                                 key = 25 16 9 4 1 0 1 4 9 16 25 (key=lambda x: x * x)
                          sorted key = 0 1 1 4 4 9 9 16 16 25 25
   sorted(range(5, -6, -1), key=...) = 0 1 -1 2 -2 3 -3 4 -4 5 -5
   """)

print("-" * 30)

print(f"\n{sorted('hello', key=lambda x: ord(x))}   // 'hello' sorted by key=lambda x: ord(x)")

enter = 'hel545 py5n st495 hel55 hel54 py5n'
print(f"\n{enter = }")
result = set(map(lambda x: x.replace('5', '*').replace('4', '*'), enter.split()))
print(f"{result = }    // replacing by lambda func")
