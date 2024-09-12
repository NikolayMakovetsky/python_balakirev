print("""
-------------------------------------------------------
3 basic numeric types in python: int, float, complex
IN FLOAT TYPE WE MUST USE '.'""".upper())

a = 2 + 2  # =4 addition                 (priority 2)
b = 3 - 1  # =2 deduction                (priority 2)
c = 4 * 2  # =8 multiplication           (priority 3)
d = 9 / 2  # =4.5 division               (priority 3)
e = 9 // 2  # =4 division with rounding  (priority 3)
f = 9 % 2  # =1 division remainder       (priority 3)
g = 2 ** 3  # =8 exponentiation          (priority 4)
# OPERATIONS IN PARENTHESES !!!          (priority 5)

print(f"""
-------------------------------------------------------
operation name             |  example        | priority
-------------------------------------------------------
addition                   |  2 + 2 = {a}         2
deduction                  |  3 - 1 = {b}         2
multiplication             |  4 * 2 = {c}         3
division                   |  9 / 2 = {d}       3
rounding division          |  9 // 2 = {e}        3
division remainder         |  9 % 2 = {f}         3
exponentiation             |  2 ** 3 = {g}        4
operations in parentheses  |  (          )      5
-------------------------------------------------------""")

print("\nservice variable '_' stores in Python console last calculated value".upper())

print("\n----------HOW IT WORKS? ARITHMETIC OPERATION-----------".upper())
var = 4 + 5
print(f"var = 4 + 5 = {var}")
print("""here python creates first object with data '4' and second object with data '5'
then creates third object for the result of operation '9' and after this objects '4' and '5' deletes
because there is no actual links to this objects
RESULT: variable 'var' links to the object with data '9', so we can work with it""")


print("\n---------- int + float = float -----------".upper())
intPlusFloat = 2 + 3.0
print("intPlusFloat = 2 + 3.0 = ", intPlusFloat)  # 5.0

print("\n----------Division always gives FLOAT result -----------".upper())
print("type(6 / 2) =", type(6 / 2), " // even '6' and '2' are integer numerics")

# Division with rounding to the least integer
print(f"""\n----------Division with rounding to the least integer -----------
7 / 3 = {7 / 3}    ->    7 // 3 = {7 // 3}
-7 / 3 = {-7 / 3}  ->   -7 // 3 = {-7 // 3}
""".upper())

print(f"""----------Division remainder -----------
9 % 5       = 9-5     = {9 % 5}
-9 % -5     = -9+5    = {-9 % -5}
9 % -5      = 9-5-5   = {9 % -5}
-9 % 5      = -9+5+5  = {-9 % 5}
To understand how it works move from first value to NULL
with step writes in second value
""".upper())

print(f"""----------Exponentiation priority FROM RIGHT TO LEFT -----------
3^8     = 6561    = {3 ** 8}
3^(2^3) = 6561    = {3 ** 2 ** 3}
9^3     = 729     = {(3 ** 2) ** 3}
""".upper())

print(f"""----------Advice: Use correct arithmetic operations priority -----------
                        27 / 3  = 9.0 = {27 ** 1 / 3}
     27^0.333333333333333333  +-= 3.0 = {27 ** (1 / 3)}
2+3*3**2+64 = 2+3*9+64 = 2+27+64 = 93 = {2 + 3 * 3 ** 2 + (4 ** (2 + 1))}
""".upper())

i = 10
print(f"""--------ARITHMETIC OPERATORS += -= *= /= //= %= **=---------
                SAVE RESULT IN CURRENT VARIABLE""".upper())
print(f"i = {i}")
i += 1
print(f"i += 1 = {i}")
i -= 2
print(f"i -= 2 = {i}")
i *= 5
print(f"i *= 5 = {i}")
i /= 2
print(f"i /= 2 = {i}, division always gives FLOAT result")
i //= 3
print(f"i //= 3 = {i}")
i %= 4
print(f"i %= 4 = {i}")
i **= 3
print(f"i **= 3 = {i}")
print(f"RESULT: i = {i}")


