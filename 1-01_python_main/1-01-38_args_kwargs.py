print("\n---------------FUNCTIONS WITH ARBITRARY NUMBER OF ARGUMENTS------------------")
m = max(1, -4, 9)
print(f"m = max(1, -4, 9)   ->   {m = }  // max(var1...varN) accept arbitrary number of args")

print("\n                  ARGUMENT PACKING OPERATOR *; (*args)")
print("\n---------------FUNCTION THAT PRINT ARBITRARY NUMBER OF ARGUMENTS---------------")


def print_all(*args):
    for i, d in enumerate(args):
        print(f"{i}. {d} {type(d)}")


print_all(*[1, 2], *"hi", *(7.6732,), *{"color": "red"})


print("\n--------------------FUNCTION THAT PRINT PATH TO THE FILE----------------")


def print_path(*args):
    path = "\\".join(args)
    print(path)


way_to_file = ("F:", "_3_", "python")
print_path(*way_to_file)

print("\n                 KEYWORD ARGUMENT PACKING OPERATOR **; (**kwargs)")
print("**kwargs allows you to accept keyword arguments packed to a dictionary")
print("\n------------FUNCTION PRINT_STR WITH DIFFERENT MODES------------------")


def print_str(str, **kwargs):
    if "trim" in kwargs and kwargs["trim"]:
        str = str.strip()
    if "reverse" in kwargs and kwargs["reverse"]:
        str = str[::-1]
    if "upper" in kwargs and kwargs["upper"]:
        if "lower" not in kwargs or not kwargs["lower"]:
            str = str.upper()
    if "lower" in kwargs and kwargs["lower"]:
        if "upper" not in kwargs or not kwargs["upper"]:
            str = str.lower()
    print(str)


print("\nEXAMPLE 1:")
str1 = "      HELLO, Python     "
print(f"{str1 = }")
print_mode = {
    "trim" : True,
    "reverse" : True,
    "upper" : False,
    "lower" : False
}
print(f"{print_mode = }")
print("RESULT: ", end="")
print_str(str1, **print_mode)


print("\nEXAMPLE 2:")
str1 = "      HELLO, Python     "
print(f"{str1 = }")
print_mode = {
    "trim" : True,
    "reverse" : False,
    "upper" : True,
    "lower" : False
}
print(f"{print_mode = }")
print("RESULT: ", end="")
print_str(str1, **print_mode)


print("\nEXAMPLE 3:  Conflict between upper and lower mode -> func don't use any of them")
str1 = "      HELLO, Python     "
print(f"{str1 = }")
print_mode = {
    "trim" : True,
    "reverse" : False,
    "upper" : True, #True!
    "lower" : True  # True! Conflict between upper and lower mode
}
print(f"{print_mode = }")
print("RESULT: ", end="")
print_str(str1, **print_mode)


print("\nEXAMPLE 4:  We deleted 'reverse' and 'upper' from the print_mode")
str1 = "      HELLO, Python     "
print(f"{str1 = }")
print_mode = {
    "trim" : True,
    "lower" : True
}
print(f"{print_mode = }")
print("RESULT: ", end="")
print_str(str1, **print_mode)

print("\n                   ARGUMENTS ORDER INSIDE OF FUNCTION")
print("(normal args, *args, keyword args, **kwargs)")

print("\n-----------------FUNCTION OS_PATH(ARGS, *ARGS, KWARGS, **KWARGS)-------------------")


def os_path(disk, *args, sep='\\', **kwargs):
    args = (disk,) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [x.strip() for x in args]
    path = sep.join(args)
    return path


p = os_path("F:  ", "  _3_", "   python  ", sep='/', trim=True)
print(f"PATH: {p}\n")
