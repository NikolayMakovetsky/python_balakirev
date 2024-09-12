print("-----------------------------------------ITERATOR-----------------------------------------------")
print("using iterator we can enumerate all elements of the collection from start to finish, BUT ONLY ONCE")
print("when iterator is already on the finish we can't return it to the start -> we should create new iterator")
print("using iterator is a safety way to iterate elements of iterable objects: STRINGS, LISTS, RANGE()...")
print("iter() - creates new iterator\nnext() - changes iterator position to the next element of iterable object")

print("\n-------------------LETS PRINT STRING ELEMENTS USING ITER() AND NEXT()------------------------")
s = "cake"
print(f"s = {s}")
it = iter(s)
for x in range(len(s)):
    print(next(it), end="->")

print("\n-------------------LETS PRINT RANGE() ELEMENTS USING ITER() AND NEXT()------------------------")
r = range(5)
print(f"r = {r}")
it = iter(r)
for x in [0, 0, 0, 0, 0]:
    print(next(it), end="->")
print(f"""\n
it->it->it->it->it->it
|   |   |   |   |   |
v   v   v   v   v   v
0 - 1 - 2 - 3 - 4 - StopIteration""")

print("\nInfo: FOR loop inside of himself calling next() function until it doesn't return \"StopIteration\" ")