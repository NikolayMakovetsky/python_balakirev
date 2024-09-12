print("\n-----------------------RECURSIVE FUNCTION-------------------------")
print("recursive function is a function that calls itself")
print("996 - maximum recursion depth")
print("997 - end of CALL STACK")


def recoursive(val):
    print(val)
    recoursive(val + 1)


# recoursive(1) -> printed values: 1...996
# RecursionError: maximum recursion depth exceeded while calling a Python object

print("\n----INFO")
print("when function called it placed to the CALL STACK")
print("in call stack python saved call order of different functions")
print("for python important to know what func from what func in what order was called")
print("operation number 997 is the end of call stack")

print("\n---------------------HOW TO LIMIT RECURSION DEPTH?---USE COUNTER------------------")


def recoursive(val):
    print(val)
    if val < 3:
        recoursive(val + 1)
    print(val)


print("unusual print by using recoursive function:     // recoursive(1)")
recoursive(1)


print("\n-------HOW TO FIND FACTORIAL BY USING RECOURSIVE FUNCTION?-------------")
print("but you should know that for this task loops are more effective!")


def fact(val):
    if val <= 0:
        return 1
    else:
        return val * fact(val - 1)


N = 4
print(f"{N}! = {fact(N)}")


print("\n-------HOW TO BYPASS HIERARCHICAL DATA USING RECOURSIVE FUNCTION?---------")
F = {
    'C:': {
        'Program Files': {
            'Java': ['test.txt', 'j_script.js'],
            0 : 'bak37.dll',
            'Python': {
                "Py_01": ['les_01-1.py', 'les_01-2.py'],
                "Py_02": ['les_02-98.py', 'les_02-99.py']
            }
        },
        0 : "sysfile.dll",
        'Windows': {
            'System32': ['dit.dll', 'zipfile.dll'],
            0 : 'msado.tlb'
        }
    }
}


def get_files(path, depth=0, COUNTER=0): # COUNTER used for beautiful printing
    if depth > 0:
        for f in path:
            if f:
                print("-" * (COUNTER + 1), "/", f, sep="")
                if type(path[f]) == dict:
                    get_files(path[f], depth-1, COUNTER+1)
                else:
                    for x in path[f]:
                        print(" " * (COUNTER + 3), x, sep="")
            else:
                print("-" * (COUNTER + 1), path[f], sep="")


nest_level = int(input("input nesting level 1...4: "))
print(f"DATA STRUCTURE with nesting level = {nest_level}:")
get_files(F, nest_level)
