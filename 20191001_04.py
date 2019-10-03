for i in range(8):
    if i % 2 == 0:
        continue
    elif i == 5:
        break
    print(i)

i = 0
while True:
    print(f"i={i} and ", end="")
    if i == 9:
        break
    i += 1
