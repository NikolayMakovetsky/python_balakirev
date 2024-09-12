# LIST - CHANGEABLE ordered data collection
print("----------LIST EXAMPLES-----------")
lTowns = ["Moscow", "Paris", "London", "Tokyo"]
lMarks = [4, 3, 3, 2, 5, 5]
lBool = [True, False, False, True]
print(lTowns)
print(lMarks)
print(lBool)

# LIST How it works?
#     0        1         2        3
#["Moscow", "Paris", "London", "Tokyo"]
#    -4        -3       -2        -1

print("\n----------list is a changeable type-----------".upper())
lTowns[0] = 'Lipetsk'
print(lTowns, "// [0] element changed")

print("\n----------list can includes different data types-----------".upper())
lDifTypes = [True, 0, 5, 6.48, "Chicago", [3.4, 5.5]]
print(lDifTypes)

print("\n----------create empty list-----------".upper())
lEmpty1, lEmpty2 = [], list()
print(f"Empty list 1: {lEmpty1}, Empty list 2: {lEmpty2}")

print("\n--------functions: len() sum() max() min() sorted()-----------".upper())
print(f"marks: {lMarks}, summ: {sum(lMarks)}, count of marks: {len(lMarks)}, average mark: {sum(lMarks)/len(lMarks)}")
print(f"minimal mark: {min(lMarks)}, maximum mark: {max(lMarks)}")
print(f"sorted list of marks: {sorted(lMarks)}")
print(f"sorted list of marks: {sorted(lMarks, reverse = True)}, reverse = True")

print("\n--------list() creates list using any iterable object-----------".upper())
lListTest = list(lTowns[0])
print(lListTest)

print("\n--------list operators + * in del-----------".upper())
del(lListTest[0])
print((['P']+lListTest) * 2)
print(r"'i' in lListTest = ", 'i' in lListTest)

print("\n--------list concatenation // .append -----------".upper())
lListTest += [555]
print(f"lListTest += [555]", lListTest)
lListTest.append(777)
print(f"lListTest.append(777)", lListTest)

print("""\n_____________________
big list problem is that you can't add new element in the middle of actual list
without creating new list in memory""".upper())

print("---------------------------.EXTEND--------------------------")
print("""The "extend" function works by taking an iterable object
and adding its elements to the end of the original list.
The iterable object can be a list, tuple, string, set, or any other iterable object.
When the "extend" function is called,
it first checks if the argument passed to it is an iterable object.
If it is not, then the function raises a "TypeError" exception.\n""")

a = [1, 2, 3]
b = [5, 6]
print(f"{a = }\n{b = }")

a.append(b)
print(f"\na.append(b)  ->  {a = }")
a.extend(b)
print(f"a.extend(b)  ->  {a = }\n")