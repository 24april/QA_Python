def isnumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def ishigherzero(number,inputtext,strict=True):
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
km,startprice,pricekm=0,0,0
km=ishigherzero(km,"KM:")
pricekm=ishigherzero(pricekm,"Price of KM:")
startprice=ishigherzero(startprice,"Start price:",False)
print("Price:",taxicost(km,pricekm,startprice))