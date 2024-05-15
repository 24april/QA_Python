def isnumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def validnumber(str,inputtext):
    str=input(inputtext)
    while isnumber(str)==False:
        print("Invalid input")
        str=input(inputtext)
    return float(str)
def createlist(listelement,elementtext="Element of list:"):
    element=0
    continued="y"
    while continued=="y":
        element=validnumber(element,elementtext)
        listelement.append(element)
        continued=input("Continue(y)?")
    return listelement
def sumlist(list):
    return sum(list)
def sumlistdivided(sumoflist):
    divider=0
    divider=validnumber(divider,"Divider:")
    try:
        result=sumoflist/divider
        return result
    except ZeroDivisionError:
        result="Zero Division Error"
        return result
numberlist=[]
createlist(numberlist,"Number:")
print(numberlist)
b=sumlistdivided(sumlist(numberlist))
print(b)