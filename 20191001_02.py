max_i = int(input("Input number >>"))
for item in range(max_i):
    print(item, end=", ")
print("next")

# next exsample
for i in range(8):
    if i % 2 == 0 :
        for item in range(4):
            print("**  ", end="")
    else:
        for item in range(4):
            print("  **", end="")
    print()