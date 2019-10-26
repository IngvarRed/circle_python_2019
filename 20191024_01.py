# 2d index

matrix = []

for i in range(5):
    matriy = []
    for j in range(5):
        matriy.append(i + j)
    matrix.append(matriy)

print(matrix)
print(matrix[2][4])
