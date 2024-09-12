print("\n          UNPACKING OPERATOR * TO PACK / UNPACK ITERABLE COLLECTIONS")
print("Unpacking operator * take iterable of values and return tuple (or list) of variables")

print("\n------------------------SINGLE UNPACKING---------------------------")
print("            All 4 variants:")
a = 'juju'
b = [*a]
print(f"{a = }                -> {b = }   // str->list")

a = "emma"
b = (*a,)
print(f"{a = }                -> {b = }   // str->tuple")

a = [4.2, 5.5, 6.1]
b = (*a,)
print(f"{a = }       -> {b = }        // list->tuple")

a = 1, 2, 3
b = [*a]
print(f"{a = }             -> {b = }              // tuple->list")

print("\n--------------------SIMPLE MULTIPLE UNPACKING-----------------------")
a = 1, 2, 3
x, y, z = a
print("a = 1, 2, 3  /  a = (1, 2, 3)  / a = [1, 2, 3]        // it works the same")
print("x, y, z = a  /  x, y, z = (*a,)  /  x, y, z = [*a,]   // it works the same")
print(f"{x = }, {y = }, {z = }                                   // result")


print("\n--------------------COMPLICATED MULTIPLE UNPACKING-----------------------")
print("used when you don't know the sequence length")

print("\nCOMPLICATED MULTIPLE UNPACKING TO LIST:")
x, *y = (1, 2, 3, 4)
print(f"x, *y = (1, 2, 3, 4)            -> {x = }, {y = }")
x, *y = 1, 2, 3, 4
print(f"x, *y = 1, 2, 3, 4   tuple!     -> {x = }, {y = }")
*x, y = (1, 2, 3, 4)
print(f"*x, y = (1, 2, 3, 4)            -> {x = }, {y = }")
x, *y = [1, 'a', True, 4.9]
print(f"x, *y = [1, 'a', True, 4.9]     -> {x = }, {y = }")
*x, y, z = "Hello!"
print(f"*x, y, z = \"Hello!\"             -> {x = }, {y = }, {z = }")

print("\nCOMPLICATED MULTIPLE UNPACKING TO TUPLE:")
print("Is it imposible?")

print("\n--------------HOW TO USE TUPLE AS AN ARGUMENT OF RANGE() FUNCTION?------------")
d = 2, 5
print(f"{d = }                        // d is a tuple")
print(f"{range(*d) = }           // 2 and 5 here is already an integer")
print(f"{list(range(*d)) = }")
print(f"{[*range(*d)] = }")
a = [1, 2, 3]

print("\n-----------------------HOW TO MERGE LIST AND TUPLE?--------------------------------")
print(f"{a = }")
print(f"{[*(True, False), *a] = }    // return list")
print(f"{(*(True, False), *a) = }    // return tuple")

print("\n-----------------OPERATOR * TO WORK WITH DICTIONATIES-------------------")
d = {0: "nochance", 1: "terrible", 2: "bad", 3: "normal", 4: "good", 5: "perfect"}
print(f"{d = }")
print(f"{[*d] = }")
print(f"{[*d.keys()] = }")
print(f"{[*d.values()] = }")
print(f"{[*d.items()] = }")

print("\n--------------------OPERATOR ** TO UNPACK DICTIONATIES-------------------")
print("in practice operator ** is often used to merge a dictionaries")
print("d1.update(d2) almost accordance to: d3 = {**d2, **d1}")
print("instead of in line: d3 = {**d2, **d1} we create a new dictionary")
d1 = {3: "normal", 4: "good", 5: "perfect"}
d2 = {4: "OK!", 5: "SUPER!", 6: "vip", 7: "elite", 9: "God"}
print(f"\n{d1 = }")
print(f"{d2 = }")
d3 = {**d1, **d2}
print("\nd3 = {**d1, **d2}")
print(f"{d3 = }")
d4 = {**d2, **d1}
print("\nd4 = {**d2, **d1}")
print(f"{d4 = }")

print("\n-------------------OPERATOR ** TO PACK FUNCTION ARGUMENTS----------------")
print("look **kwargs")