
import sys

pan = [[0 for col in range(19)] for row in range(19)]

n = int(sys.stdin.readline().strip())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    pan[x - 1][y - 1] = 1

for i in range(len(pan)):
    for j in range(len(pan)):
        print(pan[i][j], end=' ')
    print()
