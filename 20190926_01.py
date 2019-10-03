""" GREETING

    ВІТАННЯ
    Запитує вік
    в залежності від віку
    <16 - Привіт
    16-30 - Вітання
    >30 - Добрий день

"""
age = float(input('How old are you ? '))
if age < 16 :
    print('Привіт!')
elif 16 <= age <= 30 :
    print('Вітання')
else:
    print('Добрий день!')

