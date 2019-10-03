""" DEPOSIT CALCULATION

    РОЗРАХУНОК ДЕПОЗИТУ
    Ввести Суму
    Ввести % ставку річну
    Розрахувати помісячно і надрукувати

"""
deposit_summ = float(input('Enter the deposit amount : '))
deposit_intr = float(input('Enter interest rate on deposit : ' ))
deposit_mont = deposit_intr / 12
print('The calculation of the deposit amount on a monthly basis')
i = 1
while i <= 12:
        deposit_summ = deposit_summ * (100 + deposit_mont) / 100
        print('mounth ', i, ' = ', round(deposit_summ, 2))
        i += 1


