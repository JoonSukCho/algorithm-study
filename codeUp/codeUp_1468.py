
import sys

n = int(sys.stdin.readline())
matrix = [[0] * n for i in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += 1
        if i % 2 == 0:
            matrix[i][j] = cnt
        else:
            matrix[i][n - j - 1] = cnt

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
