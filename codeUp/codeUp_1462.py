
import sys

n = int(sys.stdin.readline().strip())

matrix = [[0] * n for i in range(n)]

a = 1
for i in range(n):
    for j in range(n):
        matrix[j][i] = a
        a += 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
