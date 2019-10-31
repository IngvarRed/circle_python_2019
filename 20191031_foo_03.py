#
def info(ff):
    def inner(*args):
        print("call Func", ff.__name__)
        print("With arguments", args)
        rez = ff(*args)
        return rez

    return inner

@info
def add(x, y):
    return x + y


print(f(add)(2, 3))
print(f(print(2,3)))

print(add(2,3))