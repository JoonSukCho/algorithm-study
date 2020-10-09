
import sys

n, m = map(int, sys.stdin.readline().split())
matrix = [[0] * m for i in range(n)]

cnt = 0
for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        cnt += 1

        if n % 2 == 0:
            if i % 2 == 0:
                matrix[i - 1][j - 1] = cnt
            else:
                matrix[i - 1][m - j] = cnt

        else:
            if i % 2 == 0:
                matrix[i - 1][m - j] = cnt
            else:
                matrix[i - 1][j - 1] = cnt


for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
