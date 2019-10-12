import string

ss = string.ascii_letters
print(ss)
ss2 = string.ascii_uppercase
print(ss2)
ss3 = string.digits
print(ss3)
ss4 = string.punctuation
print(ss4)

# for i in range(len(ss4)):
#     print(i, ss4[i], ord(ss4[i]))

for i in range(len(ss2)):
    print(ss2[i], ord(ss2[i]))

print()

for i in ss2:
    print(i, ord(i))