def isnumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
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
    a=input("First number:")
    while isnumber(a)==False:
        print("Invalid input")
        a=input("First number:")
    a=float(a)
    action=input("+ - * / :")
    while action not in ("+","-","*","/"):
        print("Invalid input")
        action=input("+ - * / :")
    b=input('Second number:')
    while isnumber(b)==False:
        print("Invalid input")
        b=input("Second number:")
    b=float(b)
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