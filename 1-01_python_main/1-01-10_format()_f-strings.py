print("\n----------ADDITION (+) METHOD TO MAKE FORMAT STRING-----------")
age = 3
name = "Nikolay"
print("My name is " + name + " I am " + str(age)*2)  # My name is Nikolay I am 33

print("\n----------.FORMAT()-----------")
print("My name is {0} I am {1} // .format".format(name, age*11))
print("My name is {0} I am {0} My age is {1} // .format".format(name, age*11))

print("\n----------.FORMAT() WITH KEYS-----------")
# If you use keys you can simple use it in different sequence
print("My name is {fio} I am {old} // .format with keywords".format(fio=name, old=age*11))
print("My name is {fio} I am {old} // here I change sequence of keywords".format(old=age*11, fio=name))

print("\n---------- F-STRINGS PYTHON 3.6+ WATCH PEP498 FOR MORE INFO -----------")
print(f"My nickname is {name}{len(name)+ord('R')} I am {age*11}")

print("\n------- FORMAT STRING USING OPERATOR MODULO (actual for Python2)-------")
name = "smith"
year = 1994
print("My name is %s and I born in year %d." % (name, year))
# %s	    string
# %d or %i	integer
# %f	    float
