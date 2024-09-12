print("""---------------------------------------------
STRING IS AN UNCHANGEBLE ITERABLE DATA TYPE !!!!
METHOD is a built-in object function in Python
syntax: Object.method(arguments)""")

msg = "abrakadabra"
print(f"""\n-------------.COUNT(sub, start, end)-----------------")
msg = {msg}
msg.count("ra", 1 , 11) = {msg.count("ra", 1 , 11)}   // returns number of repeats substring 'sub' in string""")

print(f"""\n-------------.REPLACE(old symbol, new symbol, count)-------------")
// count = 1 maximum one replacement // count = -1 no limit replacements
msg = {msg}
msg.replace('a', 'o', -1) = {msg.replace('a', 'o', -1)}
msg.replace('a', 'o', 2) = {msg.replace('a', 'o', 2)}""")

digs = "1, 2,  3,4,5   6,"
digsList = digs.replace(" ", "").split(",")
print(f"""\n--------------.SPLIT(sep="", maxsplit = -1)-----------------")
// return collection of substrings, maked from basic string
// maxsplit = -1 no limit of separations
"Ivanov Ivan Ivanovich".split(" ", 1)  ->  {"Ivanov Ivan Ivanovich".split(" ", 1)})
digs = {digs}  |  type(digs) = {type(digs)}
digsList = digs.replace(" ", "").split(",")  -> {digsList}""")

digsJoined = " ".join(digsList)
print(f"""\n--------------.JOIN()-----------------
// return one joined string
digsList = {digsList}
digsJoined = " ".join(digsList)  ->  {digsJoined}
type(digsJoined) = {type(digsJoined)}""")

print(f"""\n-----------.UPPER() ------.LOWER()-----------------
// change letters register
msg = {msg}
msg.upper() = {msg.upper()}
type(msg.upper)  = {type(msg.upper)} 
msg.lower() = {msg.lower()}
type(msg.lower)   = {type(msg.lower)}""")

print(f"""\n------.FIND(sub, start, end)------.RFIND(sub, start, end)------.INDEX(sub, start, end)----------------
FIND(sub, start, end) finds first sub-element in string and returns it's ID // else returns -1 // it goes from left to right
msg = {msg}
msg.find("bra", 2, 12) = {msg.find("bra", 2, 12)}   //  abrakadaBRA
msg.find("bro")  = {msg.find("bro")}        // no finded

RFIND(sub, start, end) works the same like .FIND but do it from RIGHT TO THE LEFT !!!
msg.find("bra") = {msg.find("bra")}     // aBRAkadabra
msg.rfind("bra") = {msg.rfind("bra")}    // abrakadaBRA

# .INDEX(sub, start, end) works the same like .FIND but RETURNS ERROR IF THERE IS NO SUBSTRINGS !!!
msg.index("bra")  = {msg.index("bra")} 
msg.index("bb")  = ??? // ValueError: substring not found""")

print(f"""\n----------.ISALPHA()---------.ISDIGIT()-------------")
// returns True or False
\"HELLow\".isalpha()"   = {"HELLow".isalpha()} 
\"HELLow!\".isalpha()"  =  {"HELLow!)".isalpha()} 
\"234\".isdigit()"     = {"234".isdigit()}  
\"2.34\".isdigit()"    = {"2.34".isdigit()}""")

bankNumber = "34562"
print(f"""\n----------.RJUST()--------------.LJUST()------------
// .RJUST(width, fillchar = "0") returns new string with added letters to the LEFT SIDE
// .LJUST(width, fillchar = "0") returns new string with added letters to the RIGHT SIDE
bankNumber = "34562"
bankNumber.rjust(10, "0") -> {bankNumber.rjust(10, "0")} 
bankNumber.ljust(10, "0")  ->  {bankNumber.ljust(10, "0")} 
bankNumber.rjust(4, " ")  -> {bankNumber.rjust(4, " ")} // because len(bankNumber) = 5, but 4 < 5""")


test1 = "    a b c    "
test2 = "abc a b c abc"
test3 = "abc a b c abc"
test4 = "abc ab bc cb bbbbbbbb FAQ a b c aa bb cc abc"
print(f"""\n----------.STRIP()------.LSTRIP()-------.RSTRIP()---------
// lstrip, rstrip and strip remove characters from the left, right and both ends of a string respectively.
//  By default they remove whitespace characters (space, tabs, linebreaks, etc)
test1 = {test1}
test1.replace(" ", "_") = {test1.replace(" ", "_")}
test1.strip().replace(" ", "_")  = {test1.strip().replace(" ", "_")}
test1.lstrip().replace(" ", "_")  = {test1.lstrip().replace(" ", "_")}
test1.rstrip().replace(" ", "_") = {test1.rstrip().replace(" ", "_")} 

test2 = {test2}
test2.replace(" ", "_") = {test2.replace(" ", "_")}
test2.strip("cab").replace(" ", "_") = {test2.strip("cab").replace(" ", "_")}
test2.lstrip("cab").replace(" ", "_") = {test2.lstrip("cab").replace(" ", "_")} 
test2.rstrip("cab").replace(" ", "_")  = {test2.rstrip("cab").replace(" ", "_")}

test3 = {test3}
test3.replace(" ", "_") = {test3.replace(" ", "_")}
test3.strip("c ab").replace(" ", "_")  = {test3.strip("c ab").replace(" ", "_")} // empty string
test3.lstrip("c ab").replace(" ", "_")  = {test3.lstrip("c ab").replace(" ", "_")}  // empty string
test3.rstrip("c ab").replace(" ", "_")  = {test3.rstrip("c ab").replace(" ", "_")}  // empty string

test4 = {test4}
test4.replace(" ", "_") = {test4.replace(" ", "_")}
test4.strip("c ab").replace(" ", "_") = {test4.strip("c ab").replace(" ", "_")}
test4.lstrip("c ab").replace(" ", "_") = {test4.lstrip("c ab").replace(" ", "_")}
test4.rstrip("c ab").replace(" ", "_") = {test4.rstrip("c ab").replace(" ", "_")}""")