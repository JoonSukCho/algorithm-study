import itertools

n = int(input())

a = []
b = []

for i in range(n):
    a.append(i + 1)

p = itertools.permutations(a)

for i in p:
    print(i)
