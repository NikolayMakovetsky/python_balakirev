print("\n--------------------- LOGIC TYPE BOOL ----------------".upper())
print("          Bool type variable can be: TRUE or FALSE    ")

print("""\nAdvice: be careful with bool variable,
because it's possible unnoticed to change type 'bool' to 'int' or 'float'""")

a, b = 2, 4
res = a > b
print(f"""a, b = 2, 4
res = a > b = {res}
type(res) = {type(res)}
res + 2.4 = {res + 2.4}
type(res + 2.4) = {type(res + 2.4)}""")

print("\n-------------- COMPARISON OPERATORS >, <, <=, >=, ==, != ---------".upper())

# EX: let's test if numeric division on 2
x = 8
print(f"x = {x}, x % 2 == 0 = {x % 2 == 0}")

print("""\n--------------OPERATORS OR, AND, NOT-------------
             PRIORITY LEVEL: OR (1), AND (2), NOT (3)
That means 'NOT' has highest priority and it will be executed first of all\n""")

y = 4.55
print(f"y = {y}    y > 2 and y < 5: {y > 2 and y < 5}         //   test if numeric is in or out of gap")

# EX: inverting of compose conditional operator
# REPEAT: Operator NOT has highest priority level
z = 19
print(f"z = {z}    z % 2 == 0 or z % 3 == 0: {z % 2 == 0 or z % 3 == 0}   //  test if we can division numeric on 2 or 3 without remainder")

print(f"""\n--------------BOOL()----------------
inverting different data type argument to bool type
bool(3) = {bool(3)} 
bool(7.5) = {bool(7.5)}
bool('fish') = {bool('fish')}
bool('') = {bool('')}
bool(" ") = {bool(" ")}
bool(0) = {bool(0)}""")
