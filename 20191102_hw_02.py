# dict name and year

name_dct = {}
name_lst = ['Vova', 'Valja', 'Petro', 'Ivan']
year_lst = [1990, 2000, 1995, 2002]

for nm, yr in zip(name_lst, year_lst):
    name_dct[nm] = yr

print("We make dictionary :", name_dct)

print("\nDictionary sorted by Name")
for i in sorted(name_dct):
    print(i, ":", name_dct[i])

print("\nDictionary sorted by Year")
for vls in sorted(name_dct.values()):
    for ks in name_dct:
        if name_dct[ks] == vls:
            print(ks, ":", name_dct[ks])


