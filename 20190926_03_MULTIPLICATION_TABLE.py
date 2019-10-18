""" MULTIPLICATION TABLE

    ТАБЛИЦЯ МНОЖЕННЯ

"""
i = 1
while i <= 10:
    j = 1
    line_t = []
    while j <= 10:
        line_t.append(i * j)
        j = j + 1
    print(line_t)
    i = i + 1

# another release

print("  |", end="")
for n in range(1, 10):
    print("  " + str(n), end="")
print()
for l in range(31):
    print("-", end="")
print()
for i in range(1, 10):
    print(str (i) + " |", end="")
    for j in range(1, 10):
        m = i * j
        if m <= 9:
            print("  " + str(m), end="")
        elif m > 9:
            print(" " + str(m), end="")
    print("")



