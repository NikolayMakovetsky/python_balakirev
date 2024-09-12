import math # bad style
# from math import pi  # good style

NAME = 'mymodule'

def get_sum_of_pi(count = 2) -> float:
    res = math.pi * count
    print(f"sum of {count} pi = {res}")
    return res

if __name__ == "__main__":  # Condition is True only if we run this file directly
    print(f"{NAME = }")     # Otherwise __name__ = "__3-01-46_mymodule__"

# INFO: if we'll make cross import between 2 python files everything will be OK

