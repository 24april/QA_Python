def createlist(listelement,elementtext="Element of list:"):
    continued="y"
    while continued=="y":
        element=input(elementtext)
        listelement.append(element)
        continued=input("Continue(y)?")
    return listelement
nlist=[]
createlist(nlist)
print(nlist)