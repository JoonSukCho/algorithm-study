
import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    l = 0
    for j in range(len(k)):
        a = j + i
        if a >= len(k):
            a = l
            l += 1
        print(k[a], end=' ')
    print()
