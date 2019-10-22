#
bord = [1, 3, 5, -10]

print(bord)

index_1 = bord.index(5)
index_2 = bord.index(-10)
print(index_1, index_2)

# magic
bord[index_1], bord[index_2] = bord[index_2], bord[index_1]
print(bord)

ll = []
for i in range(10):
    ll.append(i)
print(ll)