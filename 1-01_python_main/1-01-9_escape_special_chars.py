print(r"""-------------SPECIAL CHARS IN PYTHON---------------
# \n  \\  \'  \"  \a  \b  \f  \r  \t  \v  \0  \xhh  \ooo  \N{id}  \uhhhh  \Uhhhhhhhh  and else
# \n - line break
# \t - gorizontal tabulation
# \v - vertical tabulation
# \f - change format
# \b - backspace emulation and so on...""")

test = "cat\n"
print("\n", rf"""------------"\n" 2 SYMBOLS BUT 1 CHAR !!!-------------------
test = "cat\n"
len(test) = {len(test)} because "\n" is 1 char even it includes 2 symbols""")

# HOW TO ESCAPE SPECIAL CHARACTERS WHEN WE USE IT IN STRINGS?
print("\n---------------------BACKSLASH PROTECTION---------------------")
print("1. panda\needs fruits")  # panda
                                # eeds fruits
print("2. panda\\needs fruits") # panda\needs fruits

print("\n-----------RAW STRING PROTECTION r\"\"----------")
# EX: Path to a file
path = r"D:\\Python\north\test.py"
print(path)  # D:\\Python\north\test.py

print("\n-----------BAD STYLE PROTECTION FOR QUOTATION MARKS----------")
print("Wine 'Summer fruits'")
print("// In this case we used mix of single and double quotation marks")