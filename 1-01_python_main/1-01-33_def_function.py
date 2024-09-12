print("---------------------------------FUNCTIONS IN PYTHON-------------------------------------")
print("""why do we like functions?
1. it makes modular code
2. it makes non-duplicated code and leads us to DRY principle - \"Don't Repeat Yourself\"
3. it makes programing simpler - we can call a function repeatedly anywhere and anytime""")

print("\n---------------------------------FUNCTION SYNTAX-------------------------------------")
print("""def <func name>([args]):      // func name mostly includes some verb: get, set, go, show etc.
    operator 1                // sometimes function have no args !!
    operator 2
    ...
    operator N""")

print("""\n---------------------------------EXAMPLE-----------------------------------------
print()
print - FUNCTION NAME - this is A LINK to an object-function
() - FUNCTION CALL OPERATOR 
""")

print("\n---------------LET'S CREATE ANOTHER LINK TO FUNCTION PRINT()---------------------")
prt = print
prt("Hi!   // function print called by created link prt")

print("\n----------------IF PRINT IS A LINK - WE CAN REDIRECT IT--------------------------")
print = "few lines before it was a link to function print, but now it's just a link to this string"
prt(print)

prt("\n-------------------FUNCTION EMULATING E-MAIL SENDING----------------------")


# PEP8 standard - 2 empty lines before function
# PEP8 standard - 2 empty lines before function
def send_email():  # symbol "_" used for good readable code
    text = "Dear, XYZ!"  # variable names should be understandable
    prt(text)


# PEP8 standard - 2 empty lines after function
# PEP8 standard - 2 empty lines after function
send_email()

prt("\n-------------------FUNCTION SEND_MAIL(with 1 parameter)----------------------")
prt("""TERMS important for understanding:
def send_mail(by_name):    //  by_name is a function PARAMETER
send_mail("Ken")           //  Ken is a function ARGUMENT\n""")


def send_mail(by_name):
    prt(f"Hi, {by_name}!")


send_mail("Ken")
prt("send_mail()    // ERROR! because for function with parameter we necessary should send an argument")
prt("In call of function with 1 argument PARAMETER links to string that we specify as an ARGUMENT")


prt("\n-------------------FUNCTION SEND_MAIL2(with 2 parameters)----------------------")


def send_mail2(name, age):
    prt(f"Hi, {name}! You are {age}!")


send_mail2("Barbie", 18)
