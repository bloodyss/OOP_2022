import random
rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))

matrix = [[0 for _ in range(cols)] for _ in range(rows)]


for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:
            matrix[i][j] = random.randint(1, 10)
        elif i == 0:
            matrix[i][j] = matrix[i][j-1] + random.randint(1, 10)
        elif j == 0:
            matrix[i][j] = matrix[i-1][j] + random.randint(1, 10)
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1]) + random.randint(1, 10)

for row in matrix:
    print(row)
def f1(matrix, K):
    steps = 0
    rs = len(matrix)
    cs = len(matrix[0])

    r = 0
    c = cs - 1

    while r < rs and c >= 0:
        steps += 1
        if matrix[r][c] == K:
            return True, steps
        elif matrix[r][c] < K:
            r += 1
        else:
            c -= 1
    return False, steps

K = int(input("Введите число K: "))
found, steps  = f1(matrix, K)
print(found, steps)