for i in range(3):
    print(f"i={i}")

# next
for i in range(3):
    for j in range(i+1):
        print("#", end="")
    print()

# next
for i in range(4):
    for j in range(i+1):
        print(f"j={j}, i={i}")
    print()