import datetime
year=int(datetime.datetime.today().year)
BASE_PRICE=20000
MILEAGE_DIVIDER=10000
brandlist=("rolls-royce","mercedes","bmw","lexus","lamborghini","land rover","maserati","porsche","jaguar","jeep","bentley","ferrari","cadillac","aston martin","alfa romeo")
pricelist=[]
carno=0
cars_amount=int(input("Количество автомобилей :"))
for x in range(cars_amount):
    car_brand=input("Марка автомобиля :")
    car_brand=car_brand.lower()
    coefbrand=2 if car_brand in brandlist else 1
    car_year=int(input("Год выпуска :"))
    coefyear=0.99**(year-car_year)
    car_mileage=int(input("Пробег километров :"))
    coefmileage=0.99**(car_mileage/MILEAGE_DIVIDER)
    car_status=input("Cостояние(новый/бу) :")
    while car_status not in ("новый","бу"):
        print("Invalid input")
        car_status=input("Cостояние(новый/бу) :")
    coefstatus=0.75 if car_status=="бу" else 1
    price=BASE_PRICE*coefbrand*coefyear*coefmileage*coefstatus
    pricelist.append(price)
for car_price in pricelist:
    carno+=1
    print(f"Стоимость автомобиля №{carno}:",format(car_price,'.0f'))
input()
