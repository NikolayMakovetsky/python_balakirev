print('''----------------
Assign Operator '=' creates a link between variable and data storage
If in program we have no links to storage object,
it will be deleted by garbage cleaner
--------------------'''.upper())
a = 7
b = 8
print(f"2 objects created: a = {a}, b = {b}")
a = b
print(f"""after line \"a = b\": a = {a}, b = {b}
storage object with number = 7 deleted
now we nave one object with number = 8 and two links to it: 'a'->8<-'b'""")

print("\n----------how to create variable-----------".upper())
var_a = "PANDA"
print(f"Variable \"{var_a}\" creates when we assign it's first value")

print("\n----------Cascading assignment-----------".upper())
c = d = f = 0
print(f"c = d = f = 0 result:", c, d, f, "// We creates 1 object and 3 links to it")

print("\n----------MULTIPLE assignment-----------".upper())
j, k, l = 3, 4, 5
print(f"j, k, l = 3, 4, 5 -> {j, k, l}")
j, k, l = ["car", "tree", "link"]
print(f"j, k, l = [\"car\", \"tree\", \"link\"] -> {j, k, l}")
j, k, l = 'rap'
print(f"j, k, l = 'rap' -> {j, k, l}")

print("\n----------id()------type()---------".upper())
#id() function returns variable linked object identificator

print(f"var_a = {var_a}, {type(var_a)}")
print(f"id(var_a) = {id(var_a)}, {type(id(var_a))}")
print(f"id('PANDA') = {id('PANDA')} - Python didn't create new object 'PANDA' but found it in a memory")
print(f"type(id) - {type(id)}")
print("""As long as you've maintained a reference to the object you can find it by id()""".upper())


print("""----------------
Variable names ALLOWED:
First symbol: a...z \ A...Z and '_'
Second to last symbols: a...z \ A...Z 0...9 and '_'
Variable names NOT ALLOWD: Python Console -> help() -> keywords
-----------------""")