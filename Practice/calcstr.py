def isnumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def validnumber(inputtext="Number:"):
    str=input(inputtext)
    while isnumber(str)==False:
        print("Invalid input.")
        str=input(inputtext)
    return float(str)
def calc():
    try:
        a=validnumber("First number:")
        action=input("+ - * / :")
        while action not in ("+","-","*","/"):
            print("Invalid input.")
            action=input("+ - * / :")
        b=validnumber('Second number:')
        if action=="+":
            result=a+b
        elif action=="-":
            result=a-b
        elif action=="*":
            result=a*b
        else:
            result=a/b
        print(a,action,b,"=",result)
    except ZeroDivisionError:
        print("Division by zero.")
continued=input("Start calculator(y)?")
while continued.lower()=="y":
    calc()
    continued=input("Continue(y)?")