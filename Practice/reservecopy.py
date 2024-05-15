copyamount=0
maxcopyamount=10
while copyamount < maxcopyamount:
    print("Создание новой копии:",copyamount+1)
    copyamount+=1
    print("Новая копия ",copyamount,"успешно создана.")
if copyamount==maxcopyamount:
    print(f"Количество созданных копий соответствует ожидаемому количеству({maxcopyamount})")
else:
    print(f"Количество созданных копий не соответствует ожидаемому количеству({maxcopyamount})")