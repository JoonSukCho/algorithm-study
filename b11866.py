

import sys

n, k = map(int, sys.stdin.readline().split())

q = [i for i in range(1, n + 1)]


res = []

i = k - 1

while 1:
    res.append(q.pop(i))
    
    if not q:
        break

    i = (i + k - 1) % len(q)

print('<' +','.join(map(str, res)) + '>')