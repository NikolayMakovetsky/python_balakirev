import time
print("---------------------------Euclid's algorithm---------------------------".upper())
print("used to find the greatest common divisor (GCD), for numbers 18 and 24 GCD = 6")


def get_GCD_slow(a, b):
    """ 
    get the greatest common divisor (GCD) by using Euclid's algorithm
    :param a: first natural numeric
    :param b: second natural numeric
    :return: GCD numeric
    """  # DESCRIPTION
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print("\n----------------------function description-----------------------".upper())
print(f"get_GCD_slow(18, 24) = {get_GCD_slow(18, 24)}")
print("\nhelp(get_GCD_slow):                                       //  easy way to find function description")
help(get_GCD_slow)

print("----------------------------test function------------------------------".upper())


def test_speed(func, a, b):
    st = time.time()
    func(a, b)
    et = time.time()
    wt = et - st
    return wt


def get_GCD_fast(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


print(f"slow func for numbers 5000000 and 2: {test_speed(get_GCD_slow, 5000000, 2)} sec.")
print(f"fast func for numbers 5000000 and 2: {test_speed(get_GCD_fast, 5000000, 2)} sec.")

print("\n--------------------------COMPARE SLOW AND FAST VERSIONS-----------------------------")
print("""      Slow              Fast
a = 32, b = 3       a = 32, b = 3
a = 29, b = 3       a = 3, b = 2
a = 26, b = 3       a = 2, b = 1
a = 23, b = 3       a = 1, b = 1
a = 20, b = 3       a = 1, b = 0
a = 17, b = 3       
a = 14, b = 3       
a = 11, b = 3       
a = 8, b = 3       
a = 5, b = 3       
a = 2, b = 3       
a = 2, b = 1       
a = 1, b = 1""")
