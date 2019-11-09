# decorate visualization of Func

def dec_area(ffunc):
    def inroom(*args, **kwargs):
        print(f'the name of the function is "{ffunc.__name__}" ')  # name of the function
        # the number of arguments and their types
        print('the number of arguments is ', len(args))
        for n, ttup in enumerate(args):
            print(f"arg[{n}] {ttup} is {type(ttup)}")
        return ffunc(*args, **kwargs)

    return inroom


@dec_area
def area2D(lx, ly):
    return lx * ly


my_area = dec_area(area2D)
print("*" * 30, "\n", my_area(2.0, 3))
