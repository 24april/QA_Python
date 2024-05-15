month_p=int(input("Ежемесячный доход :"))
credit_rating=int(input("Кредитный рейтинг :"))
if credit_rating>10 or credit_rating<1 or month_p<=0:
    print("Invalid input")
else:
    if month_p>=5000:
        if credit_rating>=7:
            print("Кредит одобрен.")
        else:
            print("Кредитный рейтинг ниже 7. Кредит не одобрен.")
    else:
        print("Доход ниже 5000.Кредит не одобрен.")