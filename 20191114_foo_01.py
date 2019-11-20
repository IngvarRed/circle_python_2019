foo = ['foo']
bar = foo
print(foo, bar)
print(id(foo), id(bar))
print('*'*30)

x = 5
L=[]

def foo(x, L=[]):
    L.append(x)

print(L)
foo(x)
print(L)

"""
CISAR
"""
import string

key = 13 # int(input('Enter key>>'))

str_arr = string.ascii_lowercase
str_arr2 = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
str_arr += string.ascii_uppercase
str_arr2 += string.ascii_uppercase[key:] + string.ascii_uppercase[:key]

print(str_arr)
print(str_arr2)

cliper_dict= {}
for k, v in zip(str_arr, str_arr2):
    cliper_dict[k] = v
print(cliper_dict)
phrase = "Hello world!" #input(">>")
ss = ""
for letter in phrase:
    if letter in cliper_dict:
        ss += cliper_dict[letter]
    else:
        ss += letter
print(">", ss)