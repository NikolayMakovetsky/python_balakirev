print("-----------------STRING IS UNCHANGEBLE ITERABLE DATA TYPE !!-------------------")
# STRING is a symbol collection, each element has own number
# STRING is a massive/list of symbols
str = "Hello Python"
print(str, type(str))
print("""STRING is a massive/list of symbols
each element has own positive and negative number 
-12 -11  -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
 H   e    l   l   o   _   P   y   t   h   o   n
 0   1    2   3   4   5   6   7   8   9   10  11""")

print("\n--------------HOW TO FIND SYMBOL IN STRING?------------")
print(f"""str = {str}
str[-4] = {str[-4]}              
str[len(str) - 1] = {str[len(str) - 1]}    
"panda"[3] = {"panda"[3]}""")

print("\n-----------STRING SLICE [start:stop] // ARRAY SLICING METHOD------------")
print(f"""str = {str}
str[1:5] = {str[1:5]} 
str[8:]  = {str[8:]}    
str[:3] = {str[:3]}     
str[:]  = {str[:]}    // (full slice) result object has the same id
str[2:2] = {str[2:2]}    // empty slice
str[-2:2] = {str[-2:2]}   // empty slice
str[2:-2] = {str[2:-2]}    // slices works only from left to the right""")

print(f"""\n---------STRING SLICES WITH 'STEP' [start:stop:step] BY DEFAULT: step = 1---------")
str = {str}
str[2:10:2] = {str[2:10:2]}  // l(2)o(4)P(8)t(10)
str[::-1]  = {str[::-1]}   // IDEA how to REVERSE STRING // if step < 0 slice starts from last element!!!""")

print(f"""\n---------STRING IS UNCHANGEABLE DATA TYPE---------")
str[0] = 'Y'  # TypeError: 'str' object does not support item assignment""")

str2 = "Y" + str[1:]
print(f"""\n---------BUT HOW TO CHANGE STRING? BINGO! CREATE NEW ONE!---------")
str = {str}
str2 = "Y" + str[1:] -> {str2}""")

# SLICE(start, stop, step) function
strSlice = slice(0, 5, 1)
print(str2[strSlice])  # Yello

strSlice = slice(0, 5, 1)
print(f"""\n--------- SLICE(start, stop, step) function ---------")
strSlice = slice(0, 5, 1)
str2 = {str2}
str2[strSlice] = {str2[strSlice]}""")

