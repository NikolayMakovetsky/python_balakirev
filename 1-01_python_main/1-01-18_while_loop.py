print("----------------------WHILE LOOP-----------------------")
print("loop includes: header with condition, body with operators")
print("1 loop iteration = 1 working cycle of loop body")
print("while the condition is True the loop body will working")
print("Advice: strict conditions is the FASTEST !")

print("\n---------------Summ of numbers 1...N---------------")
N = int(input("1 <= N <= 1000: "))
summ = 0
i = 1
while i < N+1:
    summ += i
    i += 1
print(f"Summ of numbers 1...{N} =", summ)

print("\n---------------RIGHT / WRONG PASSWORD---------------")
passWord = "loop33"
passTry = ""
while passWord != passTry:
    passTry = input("password: ")
    print(f"you have entered: {passTry}\nright password: loop33\n")
print("Hello, dear guest! Enjoy our application and thank you for your choice!")

print("\n-------------------SUMM OF UNEVEN NUMBERS 1...N----------------------- WHILE + IF----------")
N = int(input("1 <= N <= 1000: "))
print("Uneven numbers is : ", end="")
summ = 0
i = 1
summPrint = ""
while i < N+1:
    if i % 2 != 0:
        summ += i
        summPrint += str(i) + ", "
    i += 1
print(summPrint)
print(f"Summ of uneven numbers 1...{N} = {summ}")
