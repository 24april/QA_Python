def isnumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def validnumber(inputtext="Number:"):
    str=input(inputtext)
    while isnumber(str)==False:
        print("Invalid input")
        str=input(inputtext)
    return float(str)
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiplicate(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return("Division by zero")
    return a/b
def calc():
    a=validnumber("First number:")
    action=input("+ - * / :")
    while action not in ("+","-","*","/"):
        print("Invalid input")
        action=input("+ - * / :")
    b=validnumber('Second number:')
    if action=="+":
        print(plus(a,b))
    elif action=="-":
        print(minus(a,b))
    elif action=="*":
        print(multiplicate(a,b))
    else:
        print(divide(a,b))
continued=input("Start calculator(y)?")
while continued=="y":
    calc()
    continued=input("Continue(y)?")