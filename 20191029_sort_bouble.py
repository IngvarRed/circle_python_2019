# sort bouble

import random

# random.seed(13)
list_lenght = 12
ll = []
for i in range(list_lenght):
    ll.append(random.randint(1, 50))
print(ll)

# sorting algorithm
changes = 1

while changes != 0:
    changes = 0
    for i in range(len(ll) - 1):
        if ll[i] > ll[i + 1]:
            ll[i], ll[i + 1] = ll[i + 1], ll[i]
            changes += 1
    print(f"Changes is {changes} and list {ll}")
