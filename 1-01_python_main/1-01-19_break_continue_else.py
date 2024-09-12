print("-------------LOOP OPERATORS: BREAK, CONTINUE, ELSE--------------")
print("  break automatically finals loop body work")
print("  continue makes 1 loop body iteration missed")
print("  else is a block that works if loop body correctly finished ")

print('\n---------IS THERE IN LIST AT LEAST ONE EVEN NUMBER?-----------------')
d = [1, 5, 3, 7, 0, -4]
print(f"We have the list: {d}")
evenNum = False
i = 0
while i < len(d):
    if d[i] % 2 == 0 and d[i] != 0:
        evenNum = True
        print(f"first found even number: {d[i]}\nevenNum = {evenNum}")
        break
    i += 1

print('\n-------SUMM OF UNEVEN NUMBERS UNTIL WE DON\'T INPUT \"0\"---------------')
print("0 - to finish")
numEnt = ""
unEvenNums = ""
unEvenSumm = 0
while True:
    numEnt = int(input("input number: ").strip())
    if numEnt == 0:
        break
    else:
        if numEnt % 2 == 0:
            continue
        else:
            unEvenNums += str(numEnt) + " "
            unEvenSumm += numEnt
print(f"unEvenNums = {unEvenNums}\nunEvenSumm = {unEvenSumm}")
print("""                          BLOCK DIAGRAM      
                            while True
                         input number: $
                           (N)  $ == 0? (Y)
                           /             \\
                 (N)  $ % 2 == 0? (Y)    break
                 /                 \\
            Summ += 5            continue
""")

print('\n---------------SUMM OF EVEN NUMBERS UNTIL USER DON\'T ENTER 0 or uneven number!-------------')
print("0 - correct finish; uneven number - dirty finish")
numEnt = 1
evenSumm = 0
evenNums = ""
while numEnt != 0:
    numEnt = int(input("even number: ").strip())
    if numEnt % 2 != 0:
        print("dirty finish")
        break
    elif numEnt == 0:
        continue
    evenNums += str(numEnt) + " "
    evenSumm += numEnt
    continue
else:
    print("correct finish")
print(f"evenNums = {evenNums}\nevenSumm = {evenSumm}")

