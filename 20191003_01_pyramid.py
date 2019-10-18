# pyramid / tree
heigth = int(input("type heigth > "))
for i in range(heigth):
    for y in range(heigth - i):
        print(" ", end="")
    for j in range(i + 2):
        print("#", end="")
    print(" ", end="")
    for y in range(i + 2):
        print("#", end="")
    print()