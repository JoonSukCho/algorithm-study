
import sys

n = int(sys.stdin.readline().strip())

w = []
h = []
rank_list = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    w.append(x)
    h.append(y)


for i in range(len(w)):
    k = 1
    for j in range(len(w)):
        if i == j:
            pass

        if w[i] < w[j] and h[i] < h[j]:
            k += 1

    rank_list.append(k)

print(' '.join(map(str, rank_list)))
