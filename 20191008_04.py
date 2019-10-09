#

# s = 'Привіт це я \'звертаюся\' довас.'
s = input("Type some text >>")

print(s)
print(len(s))  # len - lenght

for i in range(len(s)):
    print(s[i], end="")
print()

print(s[0:4])
