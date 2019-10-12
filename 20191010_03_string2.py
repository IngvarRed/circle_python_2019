import string

lower_case = string.ascii_lowercase

s = " "
# is _s_ IN the Lower_case-string
rez = s in lower_case
print(rez)

for s1 in "Hello world!":
    print(s1, end=" -- ")
    if s1 in string.ascii_lowercase:
        print("Small")
    elif s1 in string.ascii_uppercase:
        print("Capital")
    else:
        print("None char symbol")