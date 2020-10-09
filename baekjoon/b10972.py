
import itertools


n = int(input())

s = list(map(int, input().split()))
a = []
b = []

if n == len(s):
    for i in range(n):
        a.append(i + 1)

    p = itertools.permutations(a)

    for i in p:
        i = list(i)
        b.append(i)
    b.append(-1)

    if s in b:
        print(b[b.index(s) + 1])
