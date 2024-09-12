print("------------------------------------DICTIONARY--------------------------------------")
print("IN PYTHON 3.7+ DICT IS AN ORDERED COLLECTION instead of earlier Python versions where it was unordered")
print("dictionary is useful when we want to have word-keys instead of numeric-keys")
print("{key1:var1, key2:var2, key3:var3}")
print("important to know that 1 VARIABLE RESPONDS ONLY 1 KEY")
print("DICT KEY SHOULD BE UNCHANGEABLE(immutable) DATA TYPE")
print("DICT VALUE COULD BE CHANGEABLE(mutable) OR UNCHANGEABLE(immutable) DATA TYPE")

print("\n------------------------------LETS CREATE TEST DICT FOR EXAMPLE----------------------")
dct = {"car": "a453gh", "house": 76, "tel": 3328456}
print(dct)

print("\n-----------------------LETS CREATE DICT USING FUNCTION DICT()-------------------------")
print("in DICT() KEYS ARE ALWAYS STRINGS")
dct1 = dict(name='James', surname='Bond', agentNum=700)
print(dct1)
print("""\n---------------INFO !!!
for KEY names like for variable names ALLOWED:
First symbol: a...z \ A...Z and '_'
Second to last symbols: a...z \ A...Z 0...9 and '_'
KEY names NOT ALLOWED: Python Console -> help() -> keywords""")

print("\n--------------------LETS CREATE DICT USING LIST AND FUNCTION DICT()-------------------------")
print("function dict() is very useful if you have some list and want to create dictionary")
lst = [[2, "bad"], [3, "norm"], [4, 'good'], [5, 'super']]
print(f"             lst = {lst}")
dct2 = dict(lst)
print(f"dct2 = dict(lst) -> {dct2}")

s = 'я'
e = s.encode('utf8')
s = e.decode('utf8')
print(f"""\n------------------IMMUTABLE DATA TYPES THAT CAN BE USED AS A KEY IN DICT------------------------
True/False - boolean
\"land\" - string
4 - integer
36.4 - float
3+5j - complex number
(3, 2.5) - tuple
{e} - bytes type
frozenset type""")

print("\n---------------------LETS CREATE EMPTY DICT AND ADD TO IT diff ELEMENTS-------------------------")
print("when we create new key with new value -> it's info automatically added to dict")
print("if we save new value to an old key -> info automatically refreshed")
d = {}
d[True] = "truth"
d[False] = "lie"
d["land"] = {"russ": "land"}  # dict var = dict, dict is immutable data type !!!
d[4] = "four"
d[36.4] = [3, 6, 4]  # dict var = list, and list is a mutable data type !!!
d[6+2j] = "complex"
d[(3, 2.5)] = "x,y"
d[b'\xd1\x8f'] = "i_am"
print(d)

print("\n-----------------------LETS CHANGE VALUE BY THE KEY: True-------------------------")
d[True] = 1
print(f"d[True] = 1\nd = {d}")

print("\n--------------------MAIN OPERATORS AND FUNCTIONS TO WORK WITH DICT--------------------------------")
print(f"len(d) = {len(d)}                   // returns amount of couples in dictionary")
del d[True]
print(f"del d[True]              // deletes couple by the key // ERROR IF YOU TRY TO DEL ANY KEY THAT IS NOT IN DICT")
test = "abc" in d
print(f"test = \"abc\" in d -> {test}              // operator IN helps to understand if KEY is in dict")
test2 = "abc" not in d
print(f"test2 = \"abc\" not in d -> {test2}       // operator NOT IN helps to understand if KEY is not in dict")
