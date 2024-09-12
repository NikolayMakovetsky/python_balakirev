print("               DICTIONARY METHODS")
print("\n-----------------------.FROMKEYS()----------------------------")
print("creates dict using list with keys and one universal default value for all keys")
lst = ["+1", "+2", "+3"]
print(f"lst = {lst}")
a = dict.fromkeys(lst)
print(f"{a}                    // variant with no args")
b = dict.fromkeys(lst, "Celsius")
print(f"{b}     // variant with argument \"Celsius\"")

print("\n-----------------------.CLEAR()----------------------------")
print("used to clear the dictionary")
print(f"Before: b = {b}")
b.clear()
print(f"After:  b = {b}")

print("\n-----------------------.COPY()----------------------------")
print("creates copy of the dictionary")
print(f"a = {a}")
d1 = a
print(f"d1 = {d1}         //  it's not a copy, it's just second link to the same dict")
print(f"id(a), id(d1) = {id(a), id(d1)}    //  id of this objects is the same!")
d2 = a.copy()
print(f"d2 = {d2}\nid(d2) = {id(d2)}                            //  d2 is the real copy of dict 'a' ")

print("\n-----------------------.GET()----------------------------")
print("returns value by the key")
d3 = {'num1': 1.1, 'num2': 2.2, 'num3': 3.3}
print(f"{d3}")
print(f"d3.get('num2') = {d3.get('num2')}")
print(f"d3['num2']             //  return ERROR if 'num2' is not in dict!")
print(f"d3.get('num4') = {d3.get('nsum4')}  //  .get() return NONE in this case and it's much better")
print(f"d3.get('num4', 'Empty') = {d3.get('num4', 'Empty')}    // 2-d arg contain answer if 'num4' is not in dict")

print("\n-----------------------.SETDEFAULT()----------------------------")
print("return value by the key, but if there is no such key - it creates this key with our value or no defined value")
print(f"d3 = {d3}")
print(f"d3.setdefault('num2', 9.8) = {d3.setdefault('num2', 9.8)}")
print(f"d3.setdefault('num4', 4.4) = {d3.setdefault('num4', 4.4)}")
print(f"d3.setdefault('num5') = {d3.setdefault('num5')}")
print(f"d3 = {d3}")

print("\n-----------------------.POP()----------------------------")
print("delete key and return it's value")
print(f"d3 = {d3}")
print(f"d3.pop('num1') = {d3.pop('num1')}                     // if 'num1' is not in dict this code returns ERROR")
print(f"d3 = {d3}")
print(f"d3.pop('num6', False) = {d3.pop('num6', False)}           // it's more safety variant")

print("\n-----------------------.POPITEM()----------------------------")
print("delete last added key and return it's value")
print(f"d3 = {d3}")
print(f"d3.popitem() = {d3.popitem()}")
print(f"d3 = {d3}")
print(f"d3.popitem() = {d3.popitem()}")
print(f"d3 = {d3}")
print(f"d3.popitem() = {d3.popitem()}")
print(f"d3 = {d3}")
print(f"d3.popitem() = {d3.popitem()}")
print(f"d3 = {d3}")
print(f"d3.popitem() -> KeyError: dictionary is empty")

print("\n-----------------------.KEYS()----------------------------")
print("return list of dict keys")
g = {True: 1, False: 5, "horse": "Pegasus", (1, 3): 1.3333}
print(f"g = {g}")
print(f"g.keys() = {g.keys()}")
print("lets print dict keys using for loop:".upper())
for x in g:
    print(x, end="->")
print("\n----------Info: by default FOR LOOP iterate KEYs of dict!------------")

print("\n-----------------------.VALUES()----------------------------")
print("return list of dict values")
print(f"{g}")
print(f"g.values() = {g.values()}")
print("lets print dict values using for loop:".upper())
for x in g.values():
    print(x, end="->")

print("\n\n-----------------------.ITEMS()----------------------------")
print("return list of tuples in format: (key, value)")
print("INFO: TUPLE IS AN IMMUTABLE DATA TYPE")
print(f"g = {g}")
print(f"g.items() = {g.items()}")
print("lets print dict items using for loop:".upper())
for x in g.items():
    print(x, end="->")
print("\nlets print dict items using for loop and method of tuple initialization x, y = (1, 2):".upper())
for x, y in g.items():
    print(x, y)

print("\n-----------------------.UPDATE() - MERGE 2 DICTS------------------")
print("merge two dicts using first list as basic")
g1 = {'three': 3, 'four': 4}
g2 = {5: 'super', 'four': 'good'}
print(f"g1 = {g1}\ng2 = {g2}")
g1.update(g2)
print(f"updated g1 = {g1}")

print("\n----------------------HOW TO MERGE 2 DICTS USING OPERATORS?---------------------")
print("we'll use operator '**' or '|' (both works the same), but what is it exactly we'll talk later in other lesson")
k1 = {'three': 3, 'four': 4}
k2 = {5: 'super', 'four': 'good'}
print(f"            k1 = {k1}")
print(f"            k2 = {k2}")
k3 = {**k1, **k2}
k4 = k2 | k1
print(f"k3 = k1 | k2 -> {k3}")
print(f"k4 = k2 | k1 -> {k4}")
