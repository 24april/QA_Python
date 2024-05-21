def isnumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def validnumber(inputtext):
    str=input(inputtext)
    while isnumber(str)==False:
        print("Invalid input.")
        str=input(inputtext)
    return float(str)
def createlist(elementtext="Element of list:"):
    listelement=[]
    continued="y"
    while continued=="y":
        element=validnumber(elementtext)
        listelement.append(element)
        continued=input("Continue(y)?")
    return listelement
def listnumbersdividedthree(numbers):
    try:
        dividedthree=[]
        for number in numbers:
            if number%3==0:
                dividedthree.append(number)
        return dividedthree
    except TypeError:
        return "Incorrect data type."
numberlist=createlist("Number:")
print("Divided by three:",listnumbersdividedthree(numberlist))