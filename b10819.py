import itertools

n = int(input())
a = list(map(int, input().split()))

if n == len(a):
    pass

p = itertools.permutations(a)
total = []
maxA = 0

for i in p:
    x = 0
    y = 1
    maxA = 0
    while 1:
        maxA += abs(i[x] - i[y])
        if x == n - 2 and y == n - 1:
            total.append(maxA)
            break
        x += 1
        y += 1

print(max(total))

# 1 2 3 = 1-2 2-3 = 2
# 1 3 2 = 1-3 3-2 = 3
# 2 1 3 = 2-1 1-3 = 3
# 2 3 1 = 2-3 3-1 = 3
# 3 1 2 = 3-1 1-2 = 3
# 3 2 1 = 3-2 2-1 = 2
