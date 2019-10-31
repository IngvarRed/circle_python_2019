def my_func(x, y, z=0):
    if z == 0:
        print("I got x =", x, "and  y=", y)
    else:
        print("I got x =", x, "and  y=", y, " z=", z)


print(my_func())
