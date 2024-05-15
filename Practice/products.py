summ=0
contin="д"
products = ['яблоки','груши','веники','угли','мясо']
prices = [100,200,300,400,500]
while contin=="д":
    product=input("Продукт: ")
    while product not in products:
            print("Invalid input")
            product=input("Продукт: ")
    summ+=prices[products.index(product)]
    contin=input("Продолжить(д)?")
if summ>=200:
    print("Скидка 10%. Сумма:",0.9*summ)
else:
    print("Сумма:",summ)