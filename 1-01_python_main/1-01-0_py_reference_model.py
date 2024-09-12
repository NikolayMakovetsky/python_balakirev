print("\n--------IMPORTANT EXAMPLES TO UNDERSTAND PYTHON REFERENCE MODEL WORKING-------")
print("When we RUN Code - Python interpret it AS ONE LINE - so we can't see a details inside")
print("But when we use REPL - we can look under the hood")

print("\n----------------")
a = 5
b = 5
print(f'{a = }, {b = }')
print('value is the same') if a == b else print('values are different')
print('id is the same') if a is b else print('ids are different')
print('''IN TERMINAL - REPL "Read Evaluate Print Loop"
>>> a = 5  // new line in Terminal is a new evaluation of Parser program that interpret the code
>>> b = 5  // new line in Terminal is a new evaluation of Parser program that interpret the code
>>> a == b  // new line in Terminal is a new evaluation of Parser program that interpret the code
True
>>> a is b  // new line in Terminal is a new evaluation of Parser program that interpret the code
True
We've got True, because 5 is in range -5...256,
Python has nums from this range automatically created all the time (it needs for himself work)
So, in 2 lines we created 2 references to num 5 that already exist''')

print("\n----------------")
c = 300
d = 300
print(f'{c = }, {d = }')
print('value is the same') if c == d else print('values are different')
print('id is the same') if c is d else print('ids are different')
print('''IN TERMINAL - REPL "Read Evaluate Print Loop"
>>> c = 300
>>> d = 300
>>> c == d
True
>>> c is d
False
We've got False, because 300 is out of range -5...256,
So, Python needed to create new variable
It created 2 vars, because we used 2 lines, that means two evaluations of Parser program
YOU NEED TO REMEMBER that even int is unchangeble type / c is d -> FALSE''')

print("\n----------------")
e = -10; f = -10
print(f'{e = }, {f = }')
print('value is the same') if e == f else print('values are different')
print('id is the same') if e is f else print('ids are different')
print('''IN TERMINAL - REPL "Read Evaluate Print Loop"
>>> e = -10; f = -10
>>> e == f
True
>>> e is f
True
We've got True, because even -10 is out of range -5...256,
and Python needed to create new variable
But!!! we created 2 vars in 1 line, that means ONLY ONE evaluation of Parser program''')

print("\n----------------")
s1 = 'password'
s2 = 'password'
print(f'{s1 = }, {s2 = }')
print('value is the same') if s1 == s2 else print('values are different')
print('id is the same') if s1 is s2 else print('ids are different')
print('''IN TERMINAL - REPL "Read Evaluate Print Loop"
>>> s1 = 'password'
>>> s2 = 'password'
>>> s1 == s2
True
>>> s1 is s2
True
We've got True, even we used 2 evaluations of Parser program
Why?
YOU NEED TO REMEMBER that even str is unchangeble type / s1 is s2 -> TRUE''')



print("\n----------------")
s3 = 'pass word'
s4 = 'pass word'
print(f'{s3 = }, {s4 = }')
print('value is the same') if s3 == s4 else print('values are different')
print('id is the same') if s3 is s4 else print('ids are different')
print('''IN TERMINAL - REPL "Read Evaluate Print Loop"
>>> s3 = 'pass word'
>>> s4 = 'pass word'
>>> s3 == s4
True
>>> s3 is s4
False
We've got False, even we used 2 evaluations of Parser program,
and we already know that STR is unmutable data type!
So, Why FALSE??
Because our strings includes SPECIAL SYMPOL (SPACE)''')


print("\n----------------")
s5 = 's#%'; s6 = 's#%'
print(f'{s5 = }, {s6 = }')
print('value is the same') if s5 == s6 else print('values are different')
print('id is the same') if s5 is s6 else print('ids are different')
print('''IN TERMINAL - REPL "Read Evaluate Print Loop"
>>> s5 = 's#%'; s6 = 's#%'
>>> s5 == s6
True
>>> s5 is s6
True
We've got True, because even out strings includes SPECIAL SYMPOLS (#%),
But we used 1 evaluation of Parser program''')

print("\n----------------")
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(f'{lst1 = }, {lst2 = }')
print('value is the same') if lst1 == lst2 else print('values are different')
print('id is the same') if lst1 is lst2 else print('ids are different')
print('''IN TERMINAL - REPL "Read Evaluate Print Loop"
>>> lst1 = [1, 2, 3]
>>> lst2 = [1, 2, 3]
>>> lst1 == lst2
True
>>> lst1 is lst2
False''')

print("\n----------------")
lst3 = [1, 2, 3]; lst4 = [1, 2, 3]
print(f'{lst3 = }, {lst4 = }')
print('value is the same') if lst3 == lst4 else print('values are different')
print('id is the same') if lst3 is lst4 else print('ids are different')
print('''IN TERMINAL - REPL "Read Evaluate Print Loop"
>>> lst3 = [1, 2, 3]; lst4 = [1, 2, 3]
>>> lst3 == lst4
True
>>> lst3 is lst4
False
''')