# year , leap year

years = []
for year in range(1990, 2018):
    years.append(year)
print(years)

leap_years = []
for year in years:
    if not year%4:
        leap_years.append(year)

print(leap_years)

print("check 2000 and 2002 are leap years?")
chk_key = True
while chk_key:
    print('to finish typing  - "0" ')
    y_year = int(input("enter the year you want to check if it is 'leap' : "))
    if leap_years.count(y_year) > 0:
        print(f"So the {y_year} is 'leap' !")
    elif y_year == 0:
        print('goodbye ! ')
        chk_key = False
    else:
        print(f"{y_year} is not a 'leap' !")