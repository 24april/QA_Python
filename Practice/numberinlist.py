listnumbers=[1,3,5,7,9,10,10]
n=int(input("Number:"))
for x in listnumbers:
    if n==x:
        print("Number exists in list")
        break
else:
    print("Number does not exist in list")