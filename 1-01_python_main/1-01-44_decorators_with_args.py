import math

print("\n----------DECORATOR TO CALCULATE MATH FUNCTION DIREVATIVE--------")
print('''Math function derivative illustrates how fast function changes in the point
x - is the point we want to calculate derivative for
dx - is a parameter with small value''')


def derivative(func):
    def wrapper(x, *args, **kwargs):
        dx = 0.0001  # fixed value of variable
        res = (func(x+dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
        return res
    return wrapper


@derivative
def sin_df(x):
    return math.sin(x)


df = sin_df(math.pi/3)
print(df)

print("\n-----------------------DECORATOR WITH ARGUMENTS------------------------")

def val_derivative(dx = 0.01):  #  in this case we can change dx if we want
    def derivative(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x+dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        return wrapper # we return REFERENCE to wrapper func!
    return derivative # we return REFERENCE to derivative func!


# @val_derivative(dx=0.1)  # easier way of using decorator
def sin_df(x):
    """sin_df(x) description"""
    return math.sin(x)


sin_df = val_derivative(dx=0.1)(sin_df) # alternative variant of using decorator
df = sin_df(math.pi/3)
print(df)


print("\n------------HOW TO SAVE NAME AND DESCRIPTION OF FUNC THAT WE DECORATE?----------------")
print(sin_df.__name__)  # wrapper // so, we lost the name sin_df by using decorator for this function =(
print(sin_df.__doc__) # None  // so, we also lost the decscription of sin_df =(


def val_derivative(dx = 0.01):
    def derivative(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x+dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        wrapper.__name__ = func.__name__  # we save __name__ of our func in decorator
        wrapper.__doc__ = func.__doc__  # we save __doc__ of our func in decorator
        return wrapper
    return derivative


@val_derivative(dx=0.1)
def sin_df(x):
    """sin_df(x) description"""
    return math.sin(x)

df = sin_df(math.pi/3)
print(df)

print(sin_df.__name__)  # sin_df 
print(sin_df.__doc__) # sin_df(x) description 


print("\n----------THE MOST SIMPLE WAY TO SAVE NAME AND DESCRIPTION OF FUNC THAT WE DECORATE---------------")
print("If you don't want to write in decorators 2 lines for saving __name__ and __doc__ all the time")
print("you can import special decorator, called wraps")
print("than, you should decorate wrapper func by the decorator wraps\n")

from functools import wraps

def val_derivative(dx = 0.01):
    def derivative(func):
        @wraps(func) # we decorate wrapper by wraps
        def wrapper(x, *args, **kwargs):
            res = (func(x+dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res # float
        return wrapper # func
    return derivative # func


@val_derivative(dx=0.1)
def sin_df(x):
    """sin_df(x) description"""
    return math.sin(x)

df = sin_df(math.pi/3)
print(df)

print(sin_df.__name__)  # sin_df 
print(sin_df.__doc__) # sin_df(x) description 

