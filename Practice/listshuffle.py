import random
listelement=[]
continued="y"
while continued=="y":
    element=input("Element of list:")
    listelement.append(element)
    continued=input("Continue(y)?")
print(listelement)
random.shuffle(listelement)
print(listelement)