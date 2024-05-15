def isnumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def ishigherzero(number,inputtext,strict=True):
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