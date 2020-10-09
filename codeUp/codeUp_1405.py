
import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(len(k)):
        a = j + i
        if a >= len(k):
            a = j - i
        print(k[a], end=' ')
    print()
