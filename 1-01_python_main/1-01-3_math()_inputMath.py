print("\n----------PYTHON FUNCTIONS -----------".upper())
print("\n----------ABS() -----------".upper())
print(f"|-5.6| = {abs(-5.6)}")  # = 5.6

# MIN() accept different numbers, return minimal
print(f"min(1, 0, -5, 6.7, -8.34) = {min(1, 0, -5, 6.7, -8.34)}")  # =-8.34
var1, var2 = 78, 12
print(f"var1, var2 = 78, 12  ->  min(var1, var2) = {min(var1, var2)}")  # =12

print("\n---------- POW() -----------".upper())
# POW() accept 2 parameters: numeric and degree, return: result of exponentiation
print(f"2^3=8 -> pow(2, 3) = {pow(2, 3)}")  # 2^3=8

print(f"""\n---------- ROUND() -----------
round(5.43) = {round(5.43)}
round(3.12) = {round(3.12)}
round(7.499) = {round(7.499)}
round(7.5) = {round(7.5)} // but sometimes result could be 7! 
type(round(6.5)) = {type(round(6.5))}
round(7.3411, 2) = {round(7.3411, 2)}
round(7.3411, -1) = {round(7.3411, -1)}
""")

print("---------- how to call one function from another? -----------".upper())
print(f"max(1, 2, abs(-5)) = {max(1, 2, abs(-5))}")  # = 5

# ADDITIONAL (OPTIONAL) MODULE MATH
import math
print(f"""\n------- MATH MODULE FUNCTIONS-----------
math.ceil(5.21) = {math.ceil(5.21)}                    // round number to bigger integer
math.floor(7.88) = {math.floor(7.88)}                  // round number to smaller integer
math.factorial(4) = {math.factorial(4)}               // 1*2*3*4 = 24 
math.trunc(4.3344) = {math.trunc(4.3344)}             // delete float numeric part after '.' and return integer numeric
type(math.trunc(4.3344))  = {type(math.trunc(4.3344))}    // it's true =)
math.log2(8) = {math.log2(8)}                       // logarithm with base 2
math.log10(100)  = {math.log10(100)}               // logarithm with base 10
math.sqrt(16)  = {math.sqrt(16)}                 //square root
math.pi = {math.pi}                 // pi number
math.e  = {math.e}                 // e number
math.log(2.7)  = {math.log(2.7)}             //  natural logarithm with base 'e'
math.log(2.7, 3)  = {math.log(2.7, 3)}          // logarithm with base 3
""")
