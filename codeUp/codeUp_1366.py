
import sys

n = int(sys.stdin.readline())

for i in range(n):
    print('*', end='')
print()


for i in range(1, n - 1):
    for j in range(n):
        if (j == 0) or (j == i) or (int(n / 2) == j) or (j == n - 1) or (j == n - i - 1) or (int(n / 2) == i):
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(n):
    print('*', end='')
print()
