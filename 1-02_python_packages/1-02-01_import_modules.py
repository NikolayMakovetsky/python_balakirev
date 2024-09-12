print("\n----------------------------IMPORT STANDART MODULES----------------------------------")
print("Module is a text file")
print("In PyCharm of VScode use CTRL + left button mouse click to open info about module")
print("docs.python.org/3/library - standart modules list and description")

print("\n----------------------------FULL IMPORT----------------------------------")

import math
import time
import pprint

pprint.pprint(locals()) # func locals() return all local variables of this python file
print("\nfor example <module 'math' (built-in)> - is the reference to namespace 'math'")
print("import operator create namespace with name 'math', so we can use vars and funcs from this module")

print("\n------------------------------SELECTIVE IMPORT----------------------------")
from math import ceil, pi
print(f"{pi = }")  # when we use selective import the objects import directly to the file


print("\n------------------SELECTIVE IMPORT OF ALL LIBRARY--------------------------")
from math import * # it is the worst way of import, because name conflict can happen
print(f"{pi = }")

print("\n---------------USE NICKNAMES IN BOTH TYPES OF IMPORT-------------------------")
print("1. Sometimes 2 different modules have vars or funcs with the same names")
print("2. It's useful when module name is very long\n")
from math import pi as pi_3_14
print(f"{pi_3_14 = }")
