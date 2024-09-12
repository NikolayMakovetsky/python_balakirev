print("-------FOR LOOP IS USEFUL FOR DOING SMTH WITH ITERABLE OBJECTS: STRINGS, LISTS AND SO ON...")
print("           Bad news is that by using FOR we can't changing an items of iterable objects")

print("\n---------------LETS IMPLEMENT COMPOSITION OF THE LIST ELEMENTS-----------------")
d = [1, 2, 3, 4, 5]
dComposition = 1
for x in d:
    dComposition *= x
print(f"d = {d}  ->  dComposition = {dComposition}")

print("\n-----------LIFE HACK: HOW TO CHANGE LIST ELEMENTS USING FOR LOOP???-----------------")
d = [1, 2, 3, 4, 5]
print(f"               d = {d}")
dIndexes = []
i = 0
while i < len(d):
    dIndexes += [i]
    i += 1
print(f"        dIndexes = {dIndexes}")
for x in dIndexes:
    d[x] *= 2
print(f"After FOR loop d = {d}")

print("\n-----------------------------RANGE()---------------------------")
print("""Return an object that produces a SEQUENCE OF INTEGERS!
from start (inclusive) to stop (exclusive)""")
x, y, z = range(2, 5)
print(f"x, y, z = range(2, 5)\n{x = }, {y = }, {z = }")

print("\n---------RANGE() HELPS TO CHANGE LIST ELEMENTS USING FOR LOOP-----------------")
print("                 range() generates arithmetic sequence")
print(f"""                  range(start:stop:step)
list(range(0, 5, 1))       {list(range(0, 5, 1))}
list(range(0, 5))          {list(range(0, 5))}
list(range(5))             {list(range(5))}
list(range(-5))            {list(range(-5))}
list(range(-10, -5))       {list(range(-10, -5))}
list(range(-20, -12, 2))   {list(range(-20, -12, 2))}
list(range(-5, 5, 2))      {list(range(-5, 5, 2))}
list(range(5, -5, -2))     {list(range(5, -5, -2))}""")

print("\n---------LET'S TRY RANGE() IN THE EX WITH LIST ELEMENTS * 2-------------")
d = [1, 2, 3, 4, 5]
print(f"                            d = {d}")
for x in range(len(d)):
    d[x] *= 2
print(f"After FOR with range()      d = {d}   // and the code is short and good readable")