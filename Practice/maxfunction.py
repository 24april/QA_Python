def maxfromlist(list):
    if not list:
        return None
    return max(list)
listelement=[]
continued="n"
continued=input("Start a list of numbers(y)?")
while continued=="y":
    element=int(input("Number:"))
    listelement.append(element)
    continued=input("Continue(y)?")
print('Max number:',maxfromlist(listelement))