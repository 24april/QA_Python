month = input("Name of month: ")
month = month.lower()
if month =="december" or month=="january" or month=="february":
    print("Winter")
elif month =="march" or month=="april" or month=="may":
    print("Spring")
elif month =="june" or month=="july" or month=="august":
    print("Summer")
elif month =="september" or month=="october" or month=="november":
    print("Autumn")
else:
    print("Invalid input")