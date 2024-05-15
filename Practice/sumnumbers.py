n=int(input("Number:"))
numbers=1
sumnumbers=0
while numbers<=n:
    sumnumbers+=numbers
    numbers+=1
print(f"Sum of numbers from 1 to {n}:",sumnumbers)