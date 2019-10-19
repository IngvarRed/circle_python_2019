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

print("перевірити чи 2000 та 2002 роки є високосними")
while True:
    y_year = int(input("введіть рік котрий хочете перевірити чи він є 'високосним' : "))
    if leap_years.count(y_year) > 0:
        print(f"Так {y_year} є 'високосним'")
    else:
        print(f"{y_year} не 'високосний'")