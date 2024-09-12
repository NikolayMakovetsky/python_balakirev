print("                          TUPLES AND IT'S METHODS")

print("\n------------------WHAT'S THE REASONS TO USE TUPLES INSTEAD OF LISTS?------------------------")
print("""1. tuples is immutable data type - by using it we protect data from programmer actions
2. tuples is immutable data type - so, we can use tuple as a key in dict
3. tuples used less memory then lists""")
lst = [1, 2, 3]
tpl = (1, 2, 3)
print(f"lst = {lst} size (bytes): {lst.__sizeof__()}")
print(f"tpl = {tpl} size (bytes): {tpl.__sizeof__()}")

print("\n----------------HOW TO CREATE EMPTY TUPLE?---------------------")
a = ()
b = tuple()
print(a, b, "- 2 variants")
print("IN PRACTICE empty tuple used as basic tuple to merge it with fresh-created tuples in loop")

print("\n-----------------------------HOW TO MERGE TUPLES? OPERATOR + -------------------------")
a = ()
print(f"a = {a}, id = {id(a)}")
a = a + (1,)
print("a = a + (1,)")
print(f"a = {a}, id = {id(a)}      // we merge empty tuple with tuple (1,) and get the result: NEW TUPLE !!!")

print("\n-----------------------------HOW TO CREATE TUPLE USING OPERATOR * -------------------------")
a = (0,) * 5
print(f"a = (0,) * 5  ->  {a}")
b = ("za", "no") * 3
print(f"b = (\"za\", \"no\") * 3  ->  {b}")

print("\n-----------------------------HOW TO DELETE ELEMENT FROM TUPLE?-------------------------")
print("it's impossible because tuple is an immutable data type - we can't change it")

print("\n-------------------------FUNCTION TUPLE() HOW IT WORKS?------------------------------")
print("tuple() can take as an argument any iterable object")
a = tuple([1, 2, 3])
print(f"a = tuple([1, 2, 3])  ->  {a}")
b = tuple("python")
print(f"b = tuple(\"python\")  ->  {b}")

print("\n-------------------------FUNCTION LIST() MAKES LIST FROM TUPLE------------------------------")
tpl = (1, 2, 3)
print(f"tpl = {tpl}\nlist(tpl) = {list(tpl)}")

print("\n-------------------TUPLE VALUES COULD BE DIFFERENT DATA TYPES------------------------------")
a = (True, 5.67, 3, [43, 8], "weight", {"car": "g76ds"}, ('L', 'A'))
print(f"a = {a}")

print("\n-----------MUTABLE (CHANGEABLE) DATA TYPES SAVE THEIR PROPERTIES IN IMMUTABLE TUPLE-------------")
print(f"a = {a}")
a[3].append(134)
print("a[3].append(134)")
print(f"a = {a}")
a[5]["flat"] = 32
print("a[5][\"flat\"] = 32")
print(f"a = {a}")

print("\n---------------------------.COUNT(x)------------------------------")
print("return number of found elements with value x")
a = (True, 3, 3, [43, 8], "weight")
print(f"a = {a}")
print(f"a.count(99) = {a.count(99)}\na.count(3) = {a.count(3)}")

print("\n---------------------------.INDEX(x [,start [,stop]])------------------------------")
print("return index of first found element with value x")
print("you can use start and stop parameters if you want to search element in a part of tuple")
a = (True, 3, 3, [43, 8], "weight", 3)
print(f"a = {a}")
print(f"a.index(3) = {a.index(3)}")
print(f"a.index(3, 3) = {a.index(3, 3)}")
print(f"a.index(3, 2, 4) = {a.index(3, 2, 4)}")
print(f"a.index(9) = ValueError: tuple.index(x): x not in tuple")

print("\n-----------------OPERATOR IN - TEST IF VALUE IS IN TUPLE----------------------")
a = (True, 3, 3, [43, 8], "weight", 3)
print(f"a = {a}")
print(f"\'weight\' in a = {'weight' in a}")
print(f"9 in a = {9 in a}")
