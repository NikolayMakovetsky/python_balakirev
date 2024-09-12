print("----------------------------------ARGUMENTS AND PARAMETERS-------------------------")
print("""Parameter is an variable that specified in function announcement
Argument is a value that passed to function when it called""")


print("\n---------------------NORMAL,KEYWORDS (NAMED), MIXED ARGUMENTS IN FUNCTION----------------------")
print("""Normal arguments get passed into a function in the order they specified in function announcement
Keyword (named) arguments get passed into a function in mixed order using the syntax \'parameter=value\'""")


def get_v(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")
    return a * b * c


v = get_v(1, 2, 3)
print(f"v = get_V(1, 2, 3)   ->   {v}           // normal arguments ARGS")
print("--------------------------------")
v = get_v(b=1, a=2, c=3)
print(f"v = get_V(b=1, a=2, c=3)   ->   {v}     // keywords arguments KWARGS")
print("--------------------------------")
v = get_v(1, c=2, b=3)
print(f"v = get_v(1, c=2, b=3)   ->   {v}       // mixed arguments")
print("--------------------------------")
print(f"v = get_v(a=1, 2, 3)   ->    Error!  // in mixed args normal args should stand first")

print("\n-----------------------ACTUAL AND FORMAL PARAMETERS IN FUNCTIONS-----------------------------")
print("""Actual Parameters are the variables that get values when the function is called 
Formal Parameters are the variables that have by default values when the function is called
Formal Parameters defines function mode that often used, but it's good that if you want you can change this mode""")
print("""INFO:
* Optional you can specify formal parameters when function called, but also you can missed them !!!
""")


def get_v(a, b, c, mode=True):  # a, b, c (Actual Parameters); mode (Formal Parameter)
    if mode:
        print(f"a = {a}, b = {b}, c = {c}      // You see a,b,c output because FORMAL PARAMETER mode = True")
    return a * b * c


print(f"V = {get_v(1, 2, 3, mode=False)}          // You don't see a,b,c output because FORMAL PARAMETER mode = False")
print("----------------")
print(f"V = {get_v(1, 2, 3)}")

print("\n-------------------------LET'S COMPARE 2 STRINGS IN FUNCTION-------------------------------")
print("1. strip mode = True / False FORMAL PARAMETER TRIM\n2. register mode = False / True FORMAL PARAMETER REG\n")


def str_compare(str1, str2, trim=True, reg=False):
    if trim:
        str1 = str1.strip()
        str2 = str2.strip()
    if reg is False:
        str1 = str1.lower()
        str2 = str2.lower()
    str1_weight = 0
    str2_weight = 0
    for x in str1:
        str1_weight += ord(x)
    for y in str2:
        str2_weight += ord(y)

    return (str1_weight, str2_weight)


print("input 2 strings using upper/lower register, start/end space symbols")
strg1 = input("string 1:")
strg2 = input("string 2:")
print("                   ENJOY THE RESULT:                // str1, str2 - actual parameters")
print("                                                    // trim, reg - formal parameters")
print(f"str_compare(strg1, strg2) = {str_compare(strg1, strg2)}              // <--- normal arguments")
print(f"str_compare(str2=strg1, str1=strg2) = {str_compare(str2=strg1, str1=strg2)}    // <--- keyword arguments")
print(f"str_compare(strg1, strg2, trim=True, reg=False) = {str_compare(strg1, strg2, trim=True, reg=False)}")
print(f"str_compare(strg1, strg2, trim=False, reg=True) = {str_compare(strg1, strg2, trim=False, reg=True)}")
print(f"str_compare(strg1, strg2, trim=True, reg=True) = {str_compare(strg1, strg2, trim=True, reg=True)}")
print(f"str_compare(strg1, strg2, trim=False, reg=False) = {str_compare(strg1, strg2, trim=False, reg=False)}")
print("------------")
print(f"str_compare(strg1, strg2, reg=False) = {str_compare(strg1, strg2, reg=False)}")
print(f"str_compare(strg1, strg2, reg=True, trim=False) = {str_compare(strg1, strg2, reg=True, trim=False)}")

print("\n---------------FUNCTION WITH MUTABLE TYPE FORMAL PARAMETER can make some problems! HOW IT WORKS?----------")
print("---def add_value(val, lst=[]):")


def add_value(val, lst=[]):
    lst.append(val)
    return lst


print("result 1:", end=" ")
l = add_value(1)
l = add_value(2)
print(l, "formal parameter lst=[] always linked to the same list. Result: BY DEFAULT WE ADD VALUES TO THE SAME LIST !")
print("result 2:", end=" ")
l1 = add_value(3, [])  # this list is deleted by garbage cleaner, because on the next line we have another l1
l1 = add_value(4, [])
print(l1)
print("result 3:", end=" ")
l2 = add_value(5, lst=[])  # this list is deleted by garbage cleaner, because on the next line we have another l2
l2 = add_value(6, lst=[])
print(l2)
print("---def add_value2(val, lst=None): -> if lst is None: -> lst = []")


def add_value2(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst


print("result 4:", end=" ")
l3 = add_value2(7)  # this list is deleted by garbage cleaner, because on the next line we have another l3
l3 = add_value2(8)
print(l3)

print("result 5:", end=" ")
lstTest = []
add_value(9, lstTest)
add_value(10, lstTest)
add_value(11, lstTest)
print(lstTest)
