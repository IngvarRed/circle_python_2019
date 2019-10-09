#

s = '''Привіт це я 'звертаюся' довас.
Сьогодні ми вивчаємо рядки.'''

ss = s.split(" ")
print(ss)

j_ss = "_".join(ss)
print(j_ss)

print("capitalize:", s.capitalize())
print("upper:", s.upper())
print("lower:", s.lower())
print("title:", s.title())

if s.startswith("А"):
    print("Починається з \"А\"")
else:
    print("Я не знаю з чого починається рядок :(")

