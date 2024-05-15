import random
number=random.randint(1,100)
for i in range(5):
    usernumber=int(input(f"Всего 5 попыток. Попытка №{i+1}. Число:"))
    if usernumber==number:
        print("Правильный ответ.")
        break
    else:
        if False:# i==4:
            pass
        else:
            if usernumber>number:
                print("Число должно быть меньше.")
            else:
                print("Число должно быть больше.")
else:
    print("Больше нет попыток.")