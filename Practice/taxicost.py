def isnumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def ishigherzero(inputtext,strict=True):
    number=input(inputtext)
    if strict:
        while (isnumber(number) and (float(number)>0))==False:
            print("Invalid input")
            number=input(inputtext)
    else:
        while (isnumber(number) and (float(number)>=0))==False:
            print("Invalid input")
            number=input(inputtext)
    return float(number)
def taxicost(km,pricekm,startprice):
    return km*pricekm+startprice
km=ishigherzero("KM:")
pricekm=ishigherzero("Price of KM:")
startprice=ishigherzero("Start price:",False)
print("Price:",taxicost(km,pricekm,startprice))