#
def add(x, y ):
    return x + y

def min(x, y):
    return x - y

def func(ff, a, b):
    rez = ff(a, b)
    return rez


print(func(add, 2, 3 ))
print(func(min, 2, 3))
