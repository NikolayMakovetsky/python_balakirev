print("\n-------------------------DECORATORS IN PYTHON--------------------------------")
print("To understand what decorators is first learn about inner funcs and closures (see below)")
print("In fact decorator is a closure that as a saved variable has a reference to function that we want to decorate")
print("Decorator expands opportunities of function we already have\n")


def func_decorator(func):
    def wrapper():
        print("did before func")
        func()
        print("did after func")
    return wrapper


def some_func():
    print("some_func called")


f = func_decorator(some_func)  # we fix in memory environment "func_decorator" that has a ref to some_func
f()  # until reference f is alive we have in memory independent local environment "func_decorator"

print("\n-------------------------DECORATOR FOR SPECIAL CASE--------------------------------")


def func_decorator(func):
    def wrapper(title):
        print("did before func")
        func(title)
        print("did after func")
    return wrapper


def some_func(title):
    print(f"title = {title}")
    

some_func = func_decorator(some_func) # some_func = wrapper
some_func("Python forever!") # we lost original reference to some_func...but it is a common practice


print("\n-------------------------UNIVERSAL DECORATOR--------------------------------")
print("If some_func will changed than our decorator will not work")
print("Now we want to create the universal decorator that will be able to work with absolutely diff funcs\n")


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("did before func")
        res = func(*args, **kwargs)
        print("did after func")
        return res
    return wrapper


def some_func(title, tag):
    print(f"title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"

some_func = func_decorator(some_func)  # now some_func refer to wrapper in func_decorator
res = some_func("Python!", "h1")  # res = wrapper("Python!", "h1")
print(res)


print("\n-------------------------SPEED TEST DECORATOR--------------------------------")
print("look 3-01-35_test_function.py")
import time


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Working time: {dt} sec.")
        return res
    return wrapper


print("\n--------get_gcd(a, b) / greatest common divisor")
def get_gcd(a, b): 
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

get_gcd = test_time(get_gcd)
res = get_gcd(2, 1_000_000)
print(f"greatest common divisor = {res}")

print("\n--------get_fast_gcd(a, b) / greatest common divisor ")
# @test_time before def get_fast_gcd(a, b)
# means that we decorate get_fast_gcd by test_time
# so, now we don't need to write: get_fast_gcd = test_time(get_fast_gcd)
@test_time
def get_fast_gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


res = get_fast_gcd(2, 1_000_000)
print(f"greatest common divisor = {res}")

