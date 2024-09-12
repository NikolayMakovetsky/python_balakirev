print("\n----------------------CLOSURES IN PYTHON--------------------------")
print("word CLOSURE comes from word CLOSE that means NOT FAR FROM")
print("The idea is to save in memory separate independent local environment with some variable:")
print("We save variable as argument of outer (external) function")
print("Then we use this variable into the inner function")
print("Then we create reference to the inner function and use it in our programm")
print("We know that in python all objects with references to it will not be deleted until references is exists")
print("So, we create a ref to the local env and this reference makes it alive until we want have it alive")


print("\n---------Function construction we are going to modify--------------------------")


def say_name(name):
    def say_gbye():
        print("Hey, " + name + "!")
    say_gbye()


say_name("Nik")


print("\n---------HELLO FUNC / Inner function takes 0 args, returns 0 values--------------")
# global environment
def say_name(name): # outer (external) environment
    def say_gbye(): # local environment
        print("Hey, " + name + "!")
    return say_gbye # no () here, we just return referense to the func say_gbye()

f = say_name("Nik")
f()
f2 = say_name("Maria")
f2()


print("\n-------COUNTER FUNC / Inner function takes 0 args, returns 1 value--------------")


def counter(start = 0):
    def step():
        nonlocal start
        start += 1
        return start
    return step # we return reference to inner func


c1 = counter() # in c1 we have ref to inner func "step"
c2 = counter(10)
print(c1(), c2()) # c1 with call operator () calls inner func "step"
print(c1(), c2())
print(c1(), c2())


print("\n-------STRIPPER FUNC / Inner function takes 1 arg, returns 1 value--------------")


def strip_string(strip_chars = " "):
    def do_strip(string):
        return string.strip(strip_chars)
    return do_strip


strip1 = strip_string()
strip2 = strip_string(" !?,.:;")
hello_python = " hello python!..: "
print(len(hello_python), hello_python)
print(len(strip1(hello_python)), strip1(hello_python))
print(len(strip2(hello_python)), strip2(hello_python))


print("\n-------DEL VALUES FUNC / Inner function takes 1 arg, returns 1 value----------")


def del_list_values(tpl = (0,)):
    def del_values(lst):
        if len(lst):
            for val in tpl:
                while val in lst:
                    lst.remove(val)
    return del_values


lst1 = [0, 1, 2, 0, 0, 5, 0, 4, 5]
del1 = del_list_values()
del2 = del_list_values((4, 5))

print(f"Before: {lst1 = }")
del1(lst1)
print(f"After del1: {lst1 = }")
del2(lst1)
print(f"After del2: {lst1 = }")
