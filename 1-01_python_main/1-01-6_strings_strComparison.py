
print("\n-------------- STRING is unchangeble !!! iterable !!! data type  ---------".upper())
s1 = "CungFU"
s2 = 'Panda'
print(s1, s2, type(s1), "SHORT STRING")
sLong1 = '''\n-----------MULTIPLE LINE STRING IN \'\'\'----------
In addition to the standard library,
there is an active collection of hundreds of thousands of components'''
print(sLong1, type(sLong1), "\n", sep='    ')

sLong2 = """--------------MULTIPLE LINE STRING IN \"\"\"-------------
(from individual programs and modules to packages and entire application development frameworks),
available from the Python Package Index.   """
print(sLong2, type(sLong2))

print("\n-------------- STRING CONCATENATION (+)  ---------".upper())
sIlike = 'I like'
sPython = 'Python'
print(sIlike + "..." + sPython + "...it's concatenation")

print("\n-------------- STRING FUNCTIONS AND OPERATOR '*' ---------".upper())

print("\n-------------- STR() ---------".upper())
print(f"type(str(5.6)) = {type(str(5.6))}  //  modified accept argument and returns string")

print("\n-------------- OPERATOR '*' ---------".upper())
strMultiple = "txt" * 5
print(f"strMultiple = \"txt\" * 5 = {strMultiple}   //  makes str by multiplicating substring")

print("\n-------------- LEN() ---------".upper())
print("strMultiple length = ", len(strMultiple), "  //  returns length of string")  # 20

print("\n-------------- ORD() ---------".upper())
print(f"ord('K') = {ord('K')} // accept symbol, returns ASCII code")

print("\n-------------- CHR() ---------".upper())
print(f"chr(75) = {chr(75)}  // accept ASCII code, returns symbol")


print("\n-------------- PYTHON STRING COMPARISON ---------".upper())

print("\n-------------- OPERATOR 'IN' ---------".upper())
# OPERATOR 'IN' returns True if substring is in string
print("\'ab\' in \'abdfd\' -> ", 'ab' in 'abdfd')  #  True

print("\n-------------- OPERATORS '==', '!=' ---------".upper())
strHello = "Hello"
print(strHello, "== Hello ->", strHello == "Hello")  # Hello == Hello True

print("\n-------------- OPERATORS '>', '<', '>=', '<=' ---------".upper())
print('\"cat\" > \"cit\"? ->', "cat" > "cit")  # False
print("""WHY FALSE?
Operator compares symbols in two strings from first to last one by one using ASCII-code table
1. 'c' = 'c' go on!
2. 'a' > 'i' False bingo! -> operator returns False
3. next symbols ignored""")
