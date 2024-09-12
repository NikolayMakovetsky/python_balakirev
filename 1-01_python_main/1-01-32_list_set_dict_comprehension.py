print("                                 COMPREHENSION                               ")
print("""comprehension is better then loop:
1. it's faster
2. it's more clear for reading by programmer
Most of all it's possible to use nested list/set/dict comprehensions in different combinations
""")
a = [x**2 for x in range(1, 5)]
print(f"a = {a}                type(a) = {type(a)}")
b = {x**2 for x in range(1, 5)}
print(f"b = {b}                type(b) = {type(b)}")
c = {x:x**2 for x in range(1, 5)}
print(f"c = {c}    type(c) = {type(c)}")

print("\n------------------------LET'S CREATE SET FROM LIST----------------------------")
lstKeys = [1, 2, '1', '2', -4, 3, 4]
print(f"lst = {lstKeys}")
st = {int(x) for x in lstKeys}
print(f"st = {st}              // by using comprehension we change data type string to integer")

print("\n-------------LET'S CREATE SET FROM LIST - version 2 with using FOR LOOP-------------")
lstKeys = [1, 2, '1', '2', -4, 3, 4]
print(f"lst = {lstKeys}")
for x in lstKeys:
    st.add(int(x))
print(f"st = {st}")

print("\n------------LET'S REWRITE KEYS WITH CAPITAL LETTERS AND VALUES WITH INTEGER DATA TYPE-------------")
dct = {'bad': 2, 'ok': 3, 'norm': '4', 'super': '5'}
lstKeys = list(dct)
dct2 = {}
for x in lstKeys:
    dct2[x.upper()] = int(dct[x])
print(dct)
print(dct2)

print("\n------------VARIANT 2-------------")
dct = {'bad': 2, 'ok': 3, 'norm': '4', 'super': '5'}
dct2 = {k.upper(): int(v) for k, v in dct.items()}
print(dct)
print(dct2)

print("\n                             CONDITIONS IN COMPREHENSIONS")
print("\n--------------LET'S MAKE SET FROM LIST, BUT USING ONLY ELEMENTS > 0-------------")
lst = [1, 2, '1', '9', -4, 3, 4]
st = {int(x) for x in lst if int(x) > 0}
print(lst)
print(st)

print("\n-----------------------LET'S REPLACE KEYS AND VALUES IN DICT--------------------------")
dct = {'bad': 2, 'ok': 3, 'norm': '4', 'super': '5'}
dct2 = {v: k for k, v in dct.items()}
print(dct)
print(f"{dct2}        //  keys are float and integer")

print("\n----------LET'S REPLACE KEYS AND VALUES IN DICT with condition that 3 <= marks <= 5 -----------------")
dct = {'bad': 2, 'ok': 3, 'norm': '4', 'super': '5'}
dct2 = {int(v): k for k, v in dct.items() if 3 <= int(v) <=5}
print(dct)
print(f"{dct2}                     //  keys are integer")
