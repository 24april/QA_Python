def isnumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def validnumber(str,inputtext="Number:"):
    str=input(inputtext)
    while isnumber(str)==False:
        print("Invalid input")
        str=input(inputtext)
    return float(str)
def ishigherzero(number,inputtext="Number:",strict=True):
    number=input(inputtext)
    if strict:
        while (isnumber(number) and (float(number)>0))==False:
            print("Invalid input")
            number=input(inputtext)
    else:
        while (isnumber(number) and (float(number)>=0))==False:
            print("Invalid input")
            number=input(inputtext)
    return float(number)
a,b=0,0
a=validnumber(a,"First number:")
b=validnumber(b,"Second number:")
try:
    result=a/b
    print(f"{a} / {b} =",result)
except ZeroDivisionError:
    print("Division by zero.")