import os

def check(ll):
    # check if the list is sorted
    return False
"""
x11 x12 x13 x14
x21 x22 x23 x24
x31 x32 x33 x34
x41 x42 x43   

X1[y,,,],
x2[y,,,]
"""


def print_bord(ll):
    os.system("clear") # for windows you need to use "cls" instead of "clear"
    print("15\t14\t13\t12\n11\t10\t9\t8\n7\t6\t5\t4\n3\t1\t2\t_")


def check_move(move, bb):
    return False

"""
x[i]
    y[j]
  if  = 0
"""


if __name__ == "__main__":
    print("You are playing the 15-th game")
    bord = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, 0]
    while not check(bord):
        print_bord(bord)
        while True:
            your_try = int(input("Enter numb 1-15 >>"))
            if check_move(your_try, bord):
                break