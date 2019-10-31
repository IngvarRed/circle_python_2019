def my_foo2(x, *args, **kwargs):
    print(f"x={x}")
    print(args)
    print(kwargs)
    print("*" * 20)


my_foo2(5)
my_foo2(6, 5, 4)
my_foo2(5, 7, z=4, v=6)
