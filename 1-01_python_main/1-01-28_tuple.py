print("------------------------------TUPLE-----------------------------")
print("tuple is an ordered immutable collection of different data")
print("\n------------------------------FOR EXAMPLE-----------------------------")
a = (-5, 'hello', True, [1, 2])
print(a)
print("""---------
    0       1        2        3
   -5    'hello'   True     [1, 2]
   -4       -3       -2       -1
---------""")

print("\n-------------USE FLOATING COMMA TO CREATE TUPLE WITH ONLY 1 ELEMENT-------------------")
b = 1,
c = (2,)
print(b, c)

print("\n-----------HOW TO UNPACK TUPLE TO SEPARATE VARIABLES------------------")
tup = (1, 2)
print(f"tup = {tup}")
x, y = (1, 2)
print(f"x = {x}, y = {y}    // WE UNPACK IT BY USING MULTIPLE ASSIGNMENT")
str = "LA"
print(f"str = {str}")
x1, y1 = str
print(f"x1 = {x1}, y1 = {y1}    // multiple assignment. how it works with string")
lst = [4.5, 8.8]
print(f"lst = {lst}")
x2, y2 = lst
print(f"x2 = {x2}, y2 = {y2}    // multiple assignment. how it works with list...")

print("\n--------------------------LEN()-----------------------")
print("return amount of elements in tuple")
a = (1, 2, 3)
print(f"a = {a}, len(a) = {len(a)}")

print("\n-------------------------ACCESS TO AN ELEMENT OF TUPLE-----------------------")
a = (1, 2, 3)
print(f"a = {a}, a[0] = {a[0]}")

print("\n--------------------------INDEXING AND SLICES------------------------------")
print("it works the same like LIST indexes and slices")
print("the only difference is that it impossible to create new tuple using [:], even [:] could create new list")
b = (1, 2, 3, 4, 5)
print(f"b = {b}")
print(f"b[1:2] = {b[1:2]}")
print(f"b[::2] = {b[::2]}")
c = b[:]
print(f"c = b[:] -> {c}")
print(f"id(b) = {id(b)}, id(c) = {id(c)}  // b and c linked to the same object!!!")
