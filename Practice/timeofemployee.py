timeofemployee={}
continued="y"
while continued=="y":
    employee=input("Name of employee:")
    time=float(input("Time of work:"))
    timeofemployee[employee]=time
    continued=input("Continue(y)?")
print(timeofemployee)