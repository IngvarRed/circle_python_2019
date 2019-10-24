import os


def check(ll):
    # check if the list is sorted
    bord_ok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    if bord_ok == ll:
        print("Congratulations! You won!")
        key_chek = True
    else:
        key_chek = False
    return key_chek


def print_bord(ll):
    os.system("cls")  # for windows you need to use "cls" instead of "clear"
    for i in range(16):
        if ll[i] == 0:
            print("_", end="\t")
        else:
            print(ll[i], end="\t")
        if (i + 1) % 4 == 0:
            print("")
    print()


def check_move(move, bb):
    position = bb.index(move)
    if (position - 1 >= 0) and (bb[position - 1] == 0):
        new_bb = bb[position]
        bb[position] = bb[position - 1]
        bb[position - 1] = new_bb
    if (position - 4 >= 0) and (bb[position - 4] == 0):
        new_bb = bb[position]
        bb[position] = bb[position - 4]
        bb[position - 4] = new_bb
    if (position + 1 <= 15) and (bb[position + 1] == 0):
        new_bb = bb[position]
        bb[position] = bb[position + 1]
        bb[position + 1] = new_bb
    if (position + 4 <= 15) and (bb[position + 4] == 0):
        new_bb = bb[position]
        bb[position] = bb[position + 4]
        bb[position + 4] = new_bb

    return True


if __name__ == "__main__":
    print("You are playing the 15-th game")
    bord = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, 0]
    # bord = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15]
    while not check(bord):
        print_bord(bord)
        while True:
            your_try = int(input("Enter numb 1-15 >>"))
            if your_try in bord:
                if check_move(your_try, bord):
                    break
            else:
                print("Error! Enter a number from 1 to 15!")
