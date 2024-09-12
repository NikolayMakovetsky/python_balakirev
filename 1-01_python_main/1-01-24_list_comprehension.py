print("---------------------------LIST COMPREHENSION---------------------")
print("list comprehension works faster then loops and code with this construction is more clear")
print("1: [$-formula FOR $ IN iterable object]")
print("2: [$-formula FOR $ IN iterable object IF conditions]")
print("3: [$-formula with ternary conditions operator FOR $ IN iterable object IF conditions]")
print("variable $ can be used only inside of the brackets [] !!!")

print("\n-------------LETS CREATE LIST OF SQUARED ELEMENTS, AND MAKE IT FAST !!!---------------")
N = 6
lstSquared = [x**2 for x in range(N)]  # [0, 1, 4, 9, 16, 25]
print(lstSquared)

print("\n-------------LETS INITIALIZE LIST WITH VALUES 1, AND MAKE IT FAST !!!---------------")
lst1 = [1 for x in range(0, 5)]  # [1, 1, 1, 1, 1]
print(lst1)

print("\n-------------LETS TRY LIST ELEMENTS IF IT'S EVEN / UNEVEN---------------")
print(lstSquared)
lst2 = [x % 2 == 0 for x in lstSquared]
print(lst2)

print("\n-------------LETS CREATE X VALUES OF LINEAR FUNCTION--------------")
lst3 = [(x * 0.5) + 3 for x in range(0, 5)]
print(lst3)

print("\n---------LETS CREATE LIST USING VALUES INPUT FROM KEYBOARD IN ONE LINE--------------")
lst4 = [int(x) for x in input("input numbers using space: ").split()]
print(lst4)

print("\n---------------LETS CREATE LIST FROM STRING \"python\"-----------------")
lst5 = [x for x in "python"]
print(lst5)

print("\n---------LETS CREATE LIST OF ASCII-table numbers of STRING \"python\"------------")
lst6 = [ord(x) for x in "python"]
print(lst6)

print("\n                  CONDITIONAL OPERATORS IN LIST COMPREHENSION")
print("\n-------------LETS CREATE LIST WITH POSITIVE NUMBERS if x % 2 == 0 AND x % 3 == 0----------------")
lst7 = [x for x in range(30) if x % 2 == 0 and x % 3 == 0]
print(lst7)

print("\n-------------LETS CREATE NEW LIST WITH LEN(ELEMENTS) < 7---------------------------------")
lst8 = [x for x in ["Moscow", "Porto", "Volgograd"] if len(x) < 7]
print(lst8)

print("\n-----------LETS CREATE NEW LIST with EVEN/UNEVEN WORDS USING TERNARY CONDITIONS OPERATOR---------------")
lst9 = ["even" if x % 2 == 0 else "uneven"
        for x in [5, 2, 2, -7, 4, -9]
        if x > 0
        ]
print(lst9)
print("Advice: to make code more readable use 3 lines in this construction")
