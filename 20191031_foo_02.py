#
def add(x, y):
    return x + y


def func(ff, a, b):
    rez = ff(a, b)
    return rez


print(func(add, 2, 3))


