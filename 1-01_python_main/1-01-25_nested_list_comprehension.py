print("-------------------------------NESTED LIST COMPREHENSION------------------------------------")
print("nested list comprehension creates advanced list elements instead of simple list comprehension")
print("""
RES = [formula with AAA, BBB, CCC
       FOR AAA IN iterable object IF conditions    // main loop
       FOR BBB IN iterable object IF conditions         // nested loop
       FOR CCC IN iterable object IF conditions             // nested loop
      ]""")

print("\n---------LETS CREATE NESTED LIST WITH 2 ELEMENTS IN ITEM---------")
lst = [[i, j]
       for i in range(4)
       for j in range(4) if j % 2 == 0
       ]
print(lst)

print("\n-------------------MULTIPLICATION TABLE---------------------")
lst1 = [f"{i}*{j} = {i*j}"
        for i in range(3)
        for j in range(4)
        ]
print(lst1)

print("\n---------LETS TRANSFORM 2-DIMENSIONAL LIST TO 1-DIMENSIONAL----------------")
matrix = [[1, 2, 3], [4, 5]]
print(matrix)
lst2 = [elem
        for row in matrix
        for elem in row
        ]
print(lst2)

print("\n       USING NESTED LIST COMPREHENSION IN PLACE OF \"formula with AAA, BBB, CCC\"        ")
print("\n-----------------------LETS CREATE MATRIX AND INITIALIZE IT------------------------------")
M, N = 3, 4
lst3 = [[x for x in range(M)]   # 2-d level of list (nested level)
        for y in range(N)       # 1-st level of list
        ]
print(lst3)

print("\n-----------------------LETS SQUARING ELEMENTS OF NESTED LIST------------------------------")
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(A)
lst4 = [elem**2
        for row in A
        for elem in row
        ]
print(lst4)
lst5 = [[elem**2 for elem in row]
        for row in A
        ]
print(lst5)

print("\n-----------------------MATRIX TRANSPOSITION------------------------------")
print("transposition means that we should change rows and columns")
B = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
print(B)
lst6 = [[B[i][j] for i in range(len(B))]
        for j in range(len(B[0]))
        ]
print(lst6)

print("\n--------------------MATRIX TRANSPOSITION: best variant-----------------------")
print("transposition means that we should change rows and columns")
B = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
print(B)
lst7 = [[row[i] for row in B]
        for i in range(len(B[0]))
        ]
print(lst7)

print("\n       USING NESTED LIST COMPREHENSION IN PLACE OF \"iterable object\"        ")
print("\n--------------LETS CREATE LIST WITH SQUARED OBJECTS----------------------------")
sqr = [s**2 for s in [x for x in range(5)]]
print(sqr)
