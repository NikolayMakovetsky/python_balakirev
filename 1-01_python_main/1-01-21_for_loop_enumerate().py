print("                   FOR LOOP EXAMPLES")
print("---------FACTORIAL-----input N: ----N! = ?------------------")
n = -1
nFact = 1
while n < 0 or n > 50:
    n = int(input("input 0 <= n <= 50: "))
if n > 0:
    for x in range(1, n+1):
        nFact *= x
print(f"{n}! = {nFact}")

print("\n---------HAPPY NEW YEAR FIR TREE-----------------")
for x in range(1, 6):
    print("*" * x)

print("\n---------LETS PASTE EVERY WORD IN LIST TO A NEW STRING----------------")
words = ['python', 'is', 'the', 'best', 'of', 'the', 'best']
strWords = ""
for x in range(len(words)):
    strWords += words[x] + " "
strWordsEdit = strWords.strip().replace(" ", "_")
print(f"words = {words}\nstrWordsEdit = {strWordsEdit}")

print("\n--------.JOIN() IS THE BEST WAY TO MAKE STRING FROM LIST !!!----------------")
strWords = "-".join(words)
print(f"words = {words}\nstrWords = \"-\".join(words) -> {strWords}")

print("\n--------LETS REPLACE ALL TWO-DIGIT NUMBERS IN LIST TO 0----------------")
num = [4, 3, 100, -53, 34, 8]
print(num)
for x in range(len(num)):
    if len(str(num[x]).replace("-", "")) == 2:
        num[x] = 0
print(num)

print("\n--------LETS DO IT ONE MORE TIME USING ABS()----------------")
num = [4, 3, 100, -53, 34, 8]
print(num)
for x in range(len(num)):
    if 9 < abs(num[x]) < 100:
        num[x] = 0
print(num)

print("\n--------------------ENUMERATE()----------------")
print("IN CONTRAST OF RANGE() ENUMERATE() takes from iterable object both: INDEX AND IT'S VALUE")
print("LETS DO OUR EXAMPLE WITH REPLACEMENT USING ENUMERATE()")
num = [4, 3, 100, -53, 34, 8]
print(num)
for i, d in enumerate(num):
    if 9 < abs(d) < 100:
        num[i] = 0
print(num, "                   // the shortest code simple for reading")

print("\n-------HOW TO REPLACE ANY CYRILLIC ALPHABET STRING TO LATIN ALPHABET STRING USING ENUMERATE()-------------")
cyrAlphabet = ['а', 'б', 'в']
latAlphabet = ['a', 'b', 'v']
cyrStr = "аабв"
print(f"cyrStr = {cyrStr}")
latStr = ""
for i, d in enumerate(cyrStr):
    for j in range(len(cyrAlphabet)):
        if d == cyrAlphabet[j]:
            latStr += latAlphabet[j]
print(f"latStr = {latStr}")