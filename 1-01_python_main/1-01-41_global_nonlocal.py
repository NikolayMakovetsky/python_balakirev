print("\n-------------------------NAMESPACE IN PYTHON-------------------------")
print("when we create myprog.py - python automatically create a new namespace 'myprog'")
print("GLOBAL VARIABLES exist in program body include function bodies")
print("LOCAL VARIABLES exist in local area (in function body) for example 'myfunc'")

print("\n----------VARIABLES WITH THE SAME NAME IN DIFFERENT NAMESPACES----------")
print("If we access to var N in local namespace, first python  tries to find it in local namespace")
print("and if python doesn't find it, it tries to find it in global namespace\n")
N = 100


def my_func(a):
    N = 20
    print(f"inside function {N = }")


print(f"outside function {N = }")
my_func(3)

print("\n------------------HOW TO USE GLOBAL VAR INSIDE FUNCTION BODY?-----------------")


def my_func(a):
    global N
    print(f"inside function {N = }")


print(f"outside function {N = }")
my_func(3)

print("\n------------------HOW !!! TO CREATE !!! GLOBAL VAR INSIDE FUNCTION BODY?---------------")


def my_func(a):
    global R
    R = 20
    print(f"inside function {R = }")


my_func(3)
print(f"outside function {R = }")


print("\n-------------------------FUNCTION INSIDE FUNCTION-----------------------")
x = 0


def outer():
    x = 1


    def inner():
        x = 2
        print("inner:", x)
    

    inner()
    print("outer:", x)


outer()
print("global:", x)


print("\n------------HOW TO WORK IN NESTED FUNC WITH FUNC VAR? use keyword: nonlocal--------------")
x = 0


def outer():
    x = 1


    def inner():
        nonlocal x # here is your attention
        x = 2
        print("inner:", x)
    

    inner()
    print("outer:", x)


outer()
print("global:", x)

print("\n--------------------NONLOCAL VAR CAN'T LINK TO GLOBAL VAR-----------------")
x = 0


def outer():
    #global x - that will give us SyntaxError
    x = 1


    def inner():
        nonlocal x # 1. here is your attention
        x = 2
        print("inner:", x)
    

    inner()
    print("outer:", x)


outer()
print("global:", x)
