def uniqlist(list):
    return sorted(list)==sorted(set(list))
def createlist(listelement,elementtext="Element of list:"):
    element=0
    continued="y"
    while continued=="y":
        element=input(elementtext)
        listelement.append(element)
        continued=input("Continue(y)?")
    return listelement
nlist=[]
createlist(nlist)
print(nlist)
print(f"Uniqlist :",uniqlist(nlist))