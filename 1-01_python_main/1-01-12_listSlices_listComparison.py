lst = ["Moscow", "Paris", "London", "Tokyo"]
print(f"""----------------LIST SLICES [start:stop]-------------------
     0        1         2        3
["Moscow", "Paris", "London", "Tokyo"]
    -4        -3       -2        -1
------------------------------------------------------------
lst[1:3] -> {lst[1:3]}
lst[2:] -> {lst[2:]}
lst[:3] -> {lst[:3]}
lst[:] -> {lst[:]}
list(lst) -> {list(lst)}
lst[-1] -> {lst[-1]}
SLICE RESULT IS A NEW LIST WITH CHOOSEN ITEMS""")

print(f"""\n--------------CHANGING GROUP OF ELEMENTS--------------""")
marks = [2, 3, 4, 3, 5, 2]
print(marks)
marks[2:4] = ["good", "normal"]
print(marks, "      //  marks[2:4] = [\"good\", \"normal\"]")
marks[:5:2] = [0, 0, 0]
print(marks, "           //marks[:5:2] = [0, 0, 0]")
marks[2:4] = 10, 20
print(marks, "             //   marks[2:4] = 10, 20")
marks += [3]
print(marks, "           // marks += [3]")
print(f"""-----------------------------------------------""")
marks = [2, 3, 4, 3, 5, 2]
print(marks)
print(marks[2:-1], "     // marks[2:-1]")
print(marks[-3:-1], "        //  marks[-3:-1]")

marks = [2, 3, 4, 3, 5, 2]
print(f"""\n--------------SLICES WITH STEP [start:stop:step]--------------
marks = {marks}
marks[1:5:2] = {marks[1:5:2]}
marks[:5:2] = {marks[:5:2]}
marks[1::2] = {marks[1::2]}
marks[::2] = {marks[::2]}
IF YOU WANT ITERATE FROM RIGHT TO LEFT UST STEP < 0
THIS IS THE WAY TO REVERSE LIST
marks[::-1] = {marks[::-1]}
marks[::-2] = {marks[::-2]}""")

print(f"""\n--------------LIST COMPARISON--------------
[1, 2, 3] == [1, 2, 3] -> {[1, 2, 3] == [1, 2, 3]}
[10, 2, 3] > [1, 2, 3] -> {[10, 2, 3] > [1, 2, 3]}
LIST COMPARISON WORKS THE SAME LIKE STRINGS
1. 10 > 1? Bingo! return result True
2. next items don't tests
[1, 2, 3, 4] > [1, 2, 3] -> {[1, 2, 3, 4] > [1, 2, 3]}
[1, 2, "abc"] > [1, 2, "abc"] -> {[1, 2, "abc"] > [1, 2, "abc"]}
[1, 2, 3] > [1, 2, "abc"] -> TypeError: '>' not supported between instances of 'int' and 'str'
""")