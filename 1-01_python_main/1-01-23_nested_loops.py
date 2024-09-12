print("                 NESTED LOOPS:FOR-FOR, FOR-WHILE, WHILE-FOR, WHILE-WHILE")
print("-----------------LET'S ENUMERATE ELEMENTS IN NESTED LIST--------------------")
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"lst = {lst}\nlst:")
for row in lst:
    for elem in row:
        print(elem, end=" ")
    print("\n")

print("-----------------LET'S SUMM TO NESTED LISTS--------------------")
lst1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
lst2 = [[0, 0, 0], [3, 3, 3], [6, 6, 6]]
print(f"lst1 = {lst1}")
print(f"lst2 = {lst2}")
lstRes = []
for i, v1 in enumerate(lst1):
    row = []
    for j, v2 in enumerate(v1):
        row.append(v2 + lst2[i][j])
    lstRes.append(row)
    print(f"row = {row}")
print(f"lstRes = {lstRes}")
print("if we will use operator \"+\" instead of .append() the result will be: lstRes = [1, 2, 3, 4, 5, 6, 7, 8, 9]")

print("\n-----------------LET'S REPLACE \"  \" TO \" \" IN COLLECTION OF STRINGS--------------------")
strColl = ["a        aaa", "bb        b      bbbb", "         cc                  c"]
print(f"strColl = {strColl}")

for i, s in enumerate(strColl):
    while s.count("  "):
        s = s.replace("  ", " ", -1)
    strColl[i] = s.strip()
print(f"strColl = {strColl}")

print("\n--------------LET'S CREATE NESTED LIST USING SIZE VALUES INPUT FROM KEYBOARD--------------------")
a, b = map(int, (input("rows, columns:").split()))
c = int(input("digit for initialization:"))
lst = []
for x in range(a):
    row = []
    for y in range(b):
        row.append(c)
    lst.append(row)

for x in lst:
    print(x)
print(f"lst = {lst}")

print("\n--------------LET'S CHANGE ROWS AND COLUMNS IN LIST--------------------")
print("Advice: if you want to change values in two variables use construction: A, B = B, A")
lstCurr = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]

print("Before:")
for x in lstCurr:
    print(x)

N = 4
for x in range(N):
    for y in range(x+1):
        lstCurr[x][y], lstCurr[y][x] = lstCurr[y][x], lstCurr[x][y]

print("\nAfter:")
for x in lstCurr:
    print(x)

print("------------------------------PASCAL TRIANGLE----------------------------------")
print("""                 example:
                    1
                 1  +  1
              1  +  2  +  1
           1  +  3  +  3  +  1
        1  +  4  +  6  +  4  +  1
              and so on...""")

# initializing all pascal triangle with 0
pascTriangle = []
N = 5
for i in range(N):
    row = []
    for j in range(i+1):
        row.append(0)
    pascTriangle.append(row)

# changing 0 to 1 on the right and left side of triangle
for i in range(len(pascTriangle)):
    pascTriangle[i][0] = 1
    pascTriangle[i][-1] = 1

# changing 0 to actual values
for x in range(len(pascTriangle)):
    for y in range(x+1):
        if pascTriangle[x][y] == 0:
            pascTriangle[x][y] = pascTriangle[x-1][y-1] + pascTriangle[x-1][y]

print('result:')
for x in pascTriangle:
    print(x)

print("-----------------PASCAL TRIANGLE: OPTIMAL REALIZATION---------------------------")
print("Advice: use equality (==) between item of nested list and mount of elements in it")
N = 5
P = []
for i in range(N):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]
    P.append(row)
for x in P:
    print(x)

