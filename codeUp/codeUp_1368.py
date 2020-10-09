
import sys

h, k, d = list(sys.stdin.readline().split())
h = int(h)
k = int(k)


if d == 'L':
    for i in range(h):
        print(' ' * i + '*' * k)
else:
    for i in range(h):
        print(' ' * (h - i - 1) + '*' * k)
