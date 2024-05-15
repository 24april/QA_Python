expensesincomes={'Monday':{'expenses':0,'incomes':0},'Tuesday':{'expenses':0,'incomes':0},'Wednesday':{'expenses':0,'incomes':0},'Thursday':{'expenses':0,'incomes':0},'Friday':{'expenses':0,'incomes':0},'Saturday':{'expenses':0,'incomes':0},'Sunday':{'expenses':0,'incomes':0}}
for day in expensesincomes:
    expenses=int(input(f"Expenses {day}:"))
    incomes=int(input(f"Incomes {day}:"))
    expensesincomes[day]['expenses']=expenses
    expensesincomes[day]['incomes']=incomes
totalexpenses=sum(x['expenses'] for x in expensesincomes.values())
totalincomes=sum(x['incomes'] for x in expensesincomes.values())
balance=totalincomes-totalexpenses
print("Balance:",balance)