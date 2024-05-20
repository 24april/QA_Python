def createlist(elementtext="Element of list:"):
    listelement=[]
    continued="y"
    while continued=="y":
        element=input(elementtext)
        listelement.append(element)
        continued=input("Continue(y)?")
    return listelement
nlist=createlist()
print(nlist)